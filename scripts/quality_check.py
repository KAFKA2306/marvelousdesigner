#!/usr/bin/env python3
"""
MkDocs文書品質チェックスクリプト（ローカル実行用）

検出するエラー:
- 改行ずれ（連続改行、不適切な改行）
- Markdownが適用されていない箇所
- HTMLタグ内でMarkdownが崩れる
- *や-が変換されていない
- 改行されない問題

使用方法:
  python scripts/quality_check.py [--fix] [--file=path/to/file.md]
  
オプション:
  --fix: 自動修正可能な問題を修正
  --file: 特定のファイルのみチェック
  --verbose: 詳細な情報を表示
"""

import os
import re
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    import markdown
    from pymdownx import superfences, details, tabbed, tasklist, highlight
except ImportError:
    markdown = None


@dataclass
class Issue:
    type: str
    file: str
    line: int
    message: str
    severity: str
    suggestion: str = ""


class DocumentQualityChecker:
    def __init__(self, fix_mode: bool = False, verbose: bool = False):
        self.issues: List[Issue] = []
        self.fix_mode = fix_mode
        self.verbose = verbose
        self.stats = {'error': 0, 'warning': 0, 'info': 0, 'fixed': 0}
        
    def log(self, message: str):
        """詳細モード時のログ出力"""
        if self.verbose:
            print(f"🔍 {message}")
    
    def add_issue(self, issue: Issue):
        """問題を追加し統計を更新"""
        self.issues.append(issue)
        self.stats[issue.severity] += 1
        
    def check_line_breaks(self, content: str, filepath: str) -> str:
        """改行ずれの検出と修正"""
        lines = content.split('\n')
        fixed_lines = []
        
        # 連続する空行の処理
        empty_count = 0
        for i, line in enumerate(lines):
            if line.strip() == '':
                empty_count += 1
                if empty_count <= 2:  # 最大2行の空行を許可
                    fixed_lines.append(line)
            else:
                if empty_count >= 3:
                    self.add_issue(Issue(
                        type='excessive_blank_lines',
                        file=filepath,
                        line=i - empty_count + 1,
                        message=f'{empty_count}行の連続空行があります',
                        severity='warning',
                        suggestion='空行は最大2行に削減'
                    ))
                    # 修正モードでは既に削減済み
                    
                empty_count = 0
                fixed_lines.append(line)
        
        # 行末スペースの処理
        for i, line in enumerate(fixed_lines):
            if line.rstrip() != line:
                self.add_issue(Issue(
                    type='trailing_whitespace',
                    file=filepath,
                    line=i + 1,
                    message='行末に不要なスペースがあります',
                    severity='error',
                    suggestion='行末スペースを削除'
                ))
                if self.fix_mode:
                    fixed_lines[i] = line.rstrip()
                    self.stats['fixed'] += 1
        
        # リスト構造の検証
        self._check_list_formatting(fixed_lines, filepath)
        
        return '\n'.join(fixed_lines)
    
    def _check_list_formatting(self, lines: List[str], filepath: str):
        """リスト項目の書式チェック"""
        for i, line in enumerate(lines):
            # リスト項目の検出
            list_match = re.match(r'^(\s*)([-*+])\s+(.+)', line)
            if list_match:
                indent, marker, content = list_match.groups()
                
                # 前の行との関係をチェック
                if i > 0:
                    prev_line = lines[i-1].strip()
                    if prev_line and not prev_line.endswith(':') and not re.match(r'^[\s]*[-*+]\s', prev_line):
                        self.add_issue(Issue(
                            type='list_spacing',
                            file=filepath,
                            line=i + 1,
                            message='リスト項目の前に空行が推奨されます',
                            severity='info',
                            suggestion='リスト前に空行を追加'
                        ))
                
                # 次の行との関係をチェック
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    if (next_line.strip() and 
                        not re.match(r'^[\s]*[-*+]\s', next_line) and 
                        not next_line.startswith(indent + '  ')):
                        self.add_issue(Issue(
                            type='list_continuation',
                            file=filepath,
                            line=i + 2,
                            message='リスト項目の継続行のインデントが不適切です',
                            severity='warning',
                            suggestion=f'継続行は{len(indent) + 2}スペースでインデント'
                        ))
    
    def check_markdown_syntax(self, content: str, filepath: str) -> str:
        """Markdown記法の問題検出と修正"""
        fixed_content = content
        
        # 強調記法の問題
        # 単独の*で囲まれた文字列（**bold**や***italic***は除外）
        emphasis_pattern = r'(?<!\*)(?<!\s)\*([^*\n\s][^*\n]*[^*\n\s])\*(?!\*)(?!\s)'
        matches = list(re.finditer(emphasis_pattern, content))
        
        for match in reversed(matches):  # 後ろから処理して位置ずれを防ぐ
            if not self._is_in_code_or_html(content, match.start()):
                line_num = content[:match.start()].count('\n') + 1
                self.add_issue(Issue(
                    type='emphasis_formatting',
                    file=filepath,
                    line=line_num,
                    message=f'強調記法が適切でない可能性: {match.group()}',
                    severity='warning',
                    suggestion='前後にスペースを追加するか**太字**に変更'
                ))
                
                if self.fix_mode:
                    # スペースを追加して修正
                    replacement = f' *{match.group(1)}* '
                    fixed_content = (fixed_content[:match.start()] + 
                                   replacement + 
                                   fixed_content[match.end():])
                    self.stats['fixed'] += 1
        
        # リスト記法の問題
        self._check_list_markers(content, filepath)
        
        return fixed_content
    
    def _check_list_markers(self, content: str, filepath: str):
        """リストマーカーの一貫性チェック"""
        lines = content.split('\n')
        current_list_markers = {}  # インデントレベル -> マーカー
        
        for i, line in enumerate(lines):
            list_match = re.match(r'^(\s*)([-*+])\s', line)
            if list_match:
                indent_level = len(list_match.group(1))
                marker = list_match.group(2)
                
                if indent_level in current_list_markers:
                    if current_list_markers[indent_level] != marker:
                        self.add_issue(Issue(
                            type='inconsistent_list_marker',
                            file=filepath,
                            line=i + 1,
                            message=f'リストマーカーが一貫していません: {marker} (期待: {current_list_markers[indent_level]})',
                            severity='warning',
                            suggestion=f'マーカーを{current_list_markers[indent_level]}に統一'
                        ))
                else:
                    current_list_markers[indent_level] = marker
    
    def check_html_markdown_conflicts(self, content: str, filepath: str) -> str:
        """HTMLタグ内のMarkdown問題検出"""
        fixed_content = content
        
        # HTMLタグ内のMarkdown記法を検出
        html_pattern = r'<([a-zA-Z][^>]*)>(.*?)</\1>'
        matches = re.finditer(html_pattern, content, re.DOTALL)
        
        for match in matches:
            tag_name = match.group(1).split()[0]  # 属性を除く
            tag_content = match.group(2)
            
            # HTMLタグ内でMarkdown記法をチェック
            if re.search(r'[*_`#]', tag_content) and tag_name.lower() not in ['code', 'pre']:
                line_num = content[:match.start()].count('\n') + 1
                self.add_issue(Issue(
                    type='html_markdown_conflict',
                    file=filepath,
                    line=line_num,
                    message=f'HTMLタグ<{tag_name}>内にMarkdown記法があります',
                    severity='error',
                    suggestion='HTMLタグ内ではHTMLエンティティを使用するか、md_in_html拡張を確認'
                ))
        
        return fixed_content
    
    def check_line_length_and_breaks(self, content: str, filepath: str) -> str:
        """行の長さと改行の問題チェック"""
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # 日本語文書では100文字を基準とする
            if len(line) > 100:
                # コードブロック、表、URL行は除外
                if (not line.strip().startswith('|') and 
                    not line.strip().startswith('    ') and
                    not line.strip().startswith('```') and
                    not re.search(r'https?://', line)):
                    self.add_issue(Issue(
                        type='long_line',
                        file=filepath,
                        line=i + 1,
                        message=f'行が長すぎます ({len(line)}文字)',
                        severity='info',
                        suggestion='自然な区切りで改行を追加'
                    ))
            
            # 日本語句読点後の改行チェック
            if re.search(r'[。！？]\s*[^\s\n]', line):
                self.add_issue(Issue(
                    type='missing_sentence_break',
                    file=filepath,
                    line=i + 1,
                    message='文末記号の後に適切な区切りがありません',
                    severity='info',
                    suggestion='文末記号の後に改行または適切なスペースを追加'
                ))
        
        return content
    
    def _is_in_code_or_html(self, content: str, position: int) -> bool:
        """指定位置がコードブロックやHTMLタグ内かどうか判定"""
        before_content = content[:position]
        current_line = before_content.split('\n')[-1]
        
        # インラインコード
        if current_line.count('`') % 2 == 1:
            return True
        
        # コードブロック
        lines_before = before_content.split('\n')
        code_block_count = 0
        for line in lines_before:
            if line.strip().startswith('```'):
                code_block_count += 1
        if code_block_count % 2 == 1:
            return True
        
        # HTMLタグ内（簡易判定）
        if '<' in current_line and current_line.rfind('<') > current_line.rfind('>'):
            return True
        
        return False
    
    def check_file(self, filepath: Path) -> bool:
        """単一ファイルの品質チェック"""
        self.log(f"チェック中: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except Exception as e:
            self.add_issue(Issue(
                type='file_read_error',
                file=str(filepath),
                line=0,
                message=f'ファイル読み込みエラー: {str(e)}',
                severity='error'
            ))
            return False
        
        # 各チェックを実行
        content = original_content
        content = self.check_line_breaks(content, str(filepath))
        content = self.check_markdown_syntax(content, str(filepath))
        content = self.check_html_markdown_conflicts(content, str(filepath))
        content = self.check_line_length_and_breaks(content, str(filepath))
        
        # 修正内容がある場合は書き戻し
        if self.fix_mode and content != original_content:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.log(f"修正済み: {filepath}")
            except Exception as e:
                self.add_issue(Issue(
                    type='file_write_error',
                    file=str(filepath),
                    line=0,
                    message=f'ファイル書き込みエラー: {str(e)}',
                    severity='error'
                ))
                return False
        
        return True
    
    def check_mkdocs_build(self):
        """MkDocsビルドと生成されたHTMLの品質チェック"""
        self.log("MkDocsビルドを実行中...")
        
        try:
            result = subprocess.run(
                ['mkdocs', 'build', '--clean'], 
                capture_output=True, 
                text=True,
                timeout=300  # 5分でタイムアウト
            )
            
            if result.returncode != 0:
                self.add_issue(Issue(
                    type='build_error',
                    file='mkdocs.yml',
                    line=0,
                    message=f'MkDocsビルドエラー: {result.stderr}',
                    severity='error',
                    suggestion='mkdocs.ymlの設定とMarkdownファイルの構文を確認'
                ))
                return False
            
            # ビルド成功時のHTML品質チェック
            self._check_generated_html()
            return True
            
        except subprocess.TimeoutExpired:
            self.add_issue(Issue(
                type='build_timeout',
                file='mkdocs.yml',
                line=0,
                message='MkDocsビルドがタイムアウトしました',
                severity='error'
            ))
            return False
        except FileNotFoundError:
            self.add_issue(Issue(
                type='mkdocs_not_found',
                file='mkdocs.yml',
                line=0,
                message='mkdocsコマンドが見つかりません',
                severity='error',
                suggestion='pip install mkdocs mkdocs-material'
            ))
            return False
    
    def _check_generated_html(self):
        """生成されたHTMLの品質チェック"""
        if not BeautifulSoup:
            self.log("BeautifulSoup4がインストールされていません。HTMLチェックをスキップします。")
            return
        
        site_dir = Path('site')
        if not site_dir.exists():
            return
        
        self.log("生成されたHTMLをチェック中...")
        
        for html_file in site_dir.rglob('*.html'):
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # 空のリスト項目
                empty_lists = soup.find_all('li', string=lambda x: not x or not x.strip())
                if empty_lists:
                    self.add_issue(Issue(
                        type='empty_list_item',
                        file=str(html_file.relative_to('site')),
                        line=0,
                        message=f'{len(empty_lists)}個の空のリスト項目があります',
                        severity='warning',
                        suggestion='Markdownファイルのリスト項目を確認'
                    ))
                
                # 変換されていないMarkdown記法
                text_content = soup.get_text()
                if re.search(r'(?<!\*)\*[^*\s][^*]*[^*\s]\*(?!\*)', text_content):
                    self.add_issue(Issue(
                        type='unconverted_emphasis',
                        file=str(html_file.relative_to('site')),
                        line=0,
                        message='変換されていない強調記法があります',
                        severity='warning',
                        suggestion='Markdownファイルの強調記法を確認'
                    ))
                
            except Exception as e:
                self.add_issue(Issue(
                    type='html_check_error',
                    file=str(html_file),
                    line=0,
                    message=f'HTML解析エラー: {str(e)}',
                    severity='warning'
                ))
    
    def generate_report(self) -> bool:
        """結果レポートの生成"""
        print(f"\n📊 文書品質チェック結果")
        print(f"━━━━━━━━━━━━━━━━━━━━")
        print(f"エラー:   {self.stats['error']}")
        print(f"警告:     {self.stats['warning']}")  
        print(f"情報:     {self.stats['info']}")
        
        if self.fix_mode:
            print(f"修正済み: {self.stats['fixed']}")
        
        if not self.issues:
            print(f"\n✅ 問題は見つかりませんでした！")
            return True
        
        # 問題をファイル別、行番号順にソート
        self.issues.sort(key=lambda x: (x.file, x.line, x.severity))
        
        current_file = None
        severity_icons = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}
        
        for issue in self.issues:
            if issue.file != current_file:
                print(f"\n📁 {issue.file}")
                current_file = issue.file
            
            icon = severity_icons[issue.severity]
            line_info = f":{issue.line}" if issue.line > 0 else ""
            print(f"  {icon} {line_info} {issue.message}")
            
            if issue.suggestion and self.verbose:
                print(f"     💡 提案: {issue.suggestion}")
        
        # GitHub Actions用のアノテーション出力
        if os.getenv('GITHUB_ACTIONS'):
            print(f"\n🔧 GitHub Actionsアノテーション:")
            for issue in self.issues:
                level = 'error' if issue.severity == 'error' else 'warning'
                print(f"::{level} file={issue.file},line={issue.line}::{issue.message}")
        
        has_errors = self.stats['error'] > 0
        if has_errors:
            print(f"\n❌ 品質チェックで{self.stats['error']}個のエラーが見つかりました")
        else:
            print(f"\n⚠️  警告または情報レベルの問題があります")
        
        return not has_errors
    
    def run_full_check(self, target_file: str = None):
        """完全な品質チェックを実行"""
        docs_dir = Path('docs')
        if not docs_dir.exists():
            print("❌ docsディレクトリが見つかりません")
            return False
        
        # 対象ファイルの決定
        if target_file:
            target_files = [Path(target_file)]
            if not target_files[0].exists():
                print(f"❌ 指定されたファイルが見つかりません: {target_file}")
                return False
        else:
            target_files = list(docs_dir.rglob('*.md'))
        
        print(f"🔍 {len(target_files)}個のMarkdownファイルをチェックします...")
        
        # 各ファイルをチェック
        success = True
        for md_file in target_files:
            if not self.check_file(md_file):
                success = False
        
        # MkDocsビルドチェック（個別ファイル指定時は除く）
        if not target_file:
            build_success = self.check_mkdocs_build()
            success = success and build_success
        
        # レポート生成
        report_success = self.generate_report()
        
        return success and report_success


def main():
    parser = argparse.ArgumentParser(
        description='MkDocs文書品質チェックツール',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python scripts/quality_check.py                    # 全ファイルをチェック
  python scripts/quality_check.py --fix              # 自動修正を有効にして全チェック
  python scripts/quality_check.py --file=docs/index.md  # 特定ファイルのみチェック
  python scripts/quality_check.py --verbose          # 詳細情報を表示
        """)
    
    parser.add_argument('--fix', action='store_true', 
                       help='自動修正可能な問題を修正')
    parser.add_argument('--file', type=str,
                       help='チェック対象のファイルを指定')
    parser.add_argument('--verbose', action='store_true',
                       help='詳細な情報を表示')
    
    args = parser.parse_args()
    
    # 品質チェッカーを初期化
    checker = DocumentQualityChecker(
        fix_mode=args.fix,
        verbose=args.verbose
    )
    
    # チェック実行
    success = checker.run_full_check(args.file)
    
    # 終了コード
    exit_code = 0 if success else 1
    sys.exit(exit_code)


if __name__ == '__main__':
    main()