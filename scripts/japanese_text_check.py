#!/usr/bin/env python3
"""
日本語テキスト品質チェックスクリプト

日本語技術文書特有の問題をチェックします:
- 敬語の一貫性
- 技術用語の統一
- 句読点の適切な使用
- 半角・全角の統一
- カタカナ表記の統一

使用方法:
  python scripts/japanese_text_check.py [--fix] [--verbose]
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Set
from dataclasses import dataclass


@dataclass
class TextIssue:
    file_path: str
    line_num: int
    issue_type: str
    message: str
    suggestion: str = ""
    severity: str = "warning"  # error, warning, info


class JapaneseTextChecker:
    def __init__(self, fix_mode: bool = False, verbose: bool = False):
        self.issues: List[TextIssue] = []
        self.fix_mode = fix_mode
        self.verbose = verbose
        
        # 技術用語の統一辞書
        self.tech_terms = {
            # VRChat関連
            'VRchat': 'VRChat',
            'VR Chat': 'VRChat', 
            'vrchat': 'VRChat',
            'VRチャット': 'VRChat',
            
            # ソフトウェア名
            'marvelous designer': 'Marvelous Designer',
            'MARVELOUS DESIGNER': 'Marvelous Designer',
            'マーベラスデザイナー': 'Marvelous Designer',
            'unity': 'Unity',
            'UNITY': 'Unity',
            'ユニティ': 'Unity',
            'github': 'GitHub',
            'Github': 'GitHub',
            'ギットハブ': 'GitHub',
            
            # 技術用語
            'ポリゴン': 'ポリゴン',
            'メッシュ': 'メッシュ', 
            'テクスチャ': 'テクスチャー',
            'マテリアル': 'マテリアル',
            'シェーダー': 'シェーダー',
            'ボーン': 'ボーン',
            'リギング': 'リギング',
            'スキニング': 'スキニング',
            'ウェイト': 'ウェイト',
            'ブレンドシェイプ': 'ブレンドシェイプ',
            
            # ファイル形式
            'FBX': 'FBX',
            'fbx': 'FBX',
            'PNG': 'PNG', 
            'png': 'PNG',
            'JPEG': 'JPEG',
            'jpeg': 'JPEG',
            'jpg': 'JPG',
        }
        
        # カタカナ表記統一
        self.katakana_variants = {
            'コンピュータ': 'コンピューター',
            'ユーザ': 'ユーザー',
            'フォルダ': 'フォルダー',
            'スライダ': 'スライダー',
            'プリセット': 'プリセット',
            'エクスポート': 'エクスポート',
            'インポート': 'インポート',
        }
        
        # 敬語パターン
        self.polite_patterns = [
            r'です。?$',
            r'ます。?$', 
            r'でしょう。?$',
            r'ください。?$',
        ]
        
        # 丁寧語パターン  
        self.casual_patterns = [
            r'だ。?$',
            r'である。?$',
            r'する。?$',
            r'だろう。?$',
        ]
    
    def log(self, message: str):
        """詳細モード時のログ出力"""
        if self.verbose:
            print(f"🔍 {message}")
    
    def add_issue(self, issue: TextIssue):
        """問題を追加"""
        self.issues.append(issue)
    
    def check_politeness_consistency(self, content: str, file_path: str):
        """敬語の一貫性をチェック"""
        lines = content.split('\n')
        polite_count = 0
        casual_count = 0
        
        for line_num, line in enumerate(lines, 1):
            # コードブロック内は除外
            if line.strip().startswith('```') or line.strip().startswith('    '):
                continue
                
            # 敬語パターンの検出
            for pattern in self.polite_patterns:
                if re.search(pattern, line):
                    polite_count += 1
                    break
            
            # 丁寧語パターンの検出
            for pattern in self.casual_patterns:
                if re.search(pattern, line):
                    casual_count += 1
                    self.add_issue(TextIssue(
                        file_path=file_path,
                        line_num=line_num,
                        issue_type='inconsistent_politeness',
                        message='敬語で統一されていない文末表現があります',
                        suggestion='「です・ます」調に統一してください',
                        severity='warning'
                    ))
                    break
    
    def check_tech_term_consistency(self, content: str, file_path: str) -> str:
        """技術用語の統一をチェック・修正"""
        fixed_content = content
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # コードブロック内は除外
            if line.strip().startswith('```') or line.strip().startswith('    '):
                continue
            
            original_line = line
            
            # 技術用語の統一
            for incorrect, correct in self.tech_terms.items():
                if incorrect in line:
                    self.add_issue(TextIssue(
                        file_path=file_path,
                        line_num=line_num,
                        issue_type='inconsistent_tech_term',
                        message=f'技術用語が統一されていません: {incorrect}',
                        suggestion=f'{correct} に統一してください',
                        severity='info'
                    ))
                    
                    if self.fix_mode:
                        line = line.replace(incorrect, correct)
            
            # カタカナ表記の統一
            for variant, standard in self.katakana_variants.items():
                if variant in line:
                    self.add_issue(TextIssue(
                        file_path=file_path,
                        line_num=line_num,
                        issue_type='katakana_variant',
                        message=f'カタカナ表記を統一してください: {variant}',
                        suggestion=f'{standard} に統一してください',
                        severity='info'
                    ))
                    
                    if self.fix_mode:
                        line = line.replace(variant, standard)
            
            # 修正があった場合は内容を更新
            if line != original_line:
                lines[line_num - 1] = line
        
        if self.fix_mode:
            fixed_content = '\n'.join(lines)
        
        return fixed_content
    
    def check_punctuation(self, content: str, file_path: str):
        """句読点の使用をチェック"""
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # コードブロック内は除外
            if line.strip().startswith('```') or line.strip().startswith('    '):
                continue
            
            # 読点の連続使用
            if re.search(r'、{2,}', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='excessive_comma',
                    message='読点（、）が連続して使用されています',
                    suggestion='不要な読点を削除してください',
                    severity='warning'
                ))
            
            # 句点の連続使用
            if re.search(r'。{2,}', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='excessive_period',
                    message='句点（。）が連続して使用されています',
                    suggestion='不要な句点を削除してください',
                    severity='warning'
                ))
            
            # 英語句読点の混在
            if re.search(r'[,;]\s*[ぁ-んァ-ヶ一-龯]', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='mixed_punctuation',
                    message='英語の句読点と日本語が混在しています',
                    suggestion='日本語部分では「、。」を使用してください',
                    severity='warning'
                ))
    
    def check_character_width(self, content: str, file_path: str) -> str:
        """半角・全角の統一をチェック・修正"""
        fixed_content = content
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # コードブロック内は除外
            if line.strip().startswith('```') or line.strip().startswith('    '):
                continue
                
            original_line = line
            
            # 全角数字を半角に
            full_width_numbers = '０１２３４５６７８９'
            half_width_numbers = '0123456789'
            translation_table = str.maketrans(full_width_numbers, half_width_numbers)
            
            if re.search(r'[０-９]', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='full_width_numbers',
                    message='全角数字が使用されています',
                    suggestion='半角数字に統一してください',
                    severity='info'
                ))
                
                if self.fix_mode:
                    line = line.translate(translation_table)
            
            # 全角英数字の検出（一部のケースで半角推奨）
            if re.search(r'[Ａ-Ｚａ-ｚ]', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='full_width_alphabet',
                    message='全角英字が使用されています',
                    suggestion='技術用語では半角英字を推奨します',
                    severity='info'
                ))
            
            # 半角カタカナの検出（全角推奨）
            if re.search(r'[ｧ-ﾝ]', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='half_width_katakana',
                    message='半角カタカナが使用されています',
                    suggestion='全角カタカナに統一してください',
                    severity='warning'
                ))
            
            # スペースの統一（文脈に応じて）
            # 日本語文中では全角スペース、英数字間では半角スペースを推奨
            if re.search(r'[ぁ-んァ-ヶ一-龯]\s+[ぁ-んァ-ヶ一-龯]', line):
                self.add_issue(TextIssue(
                    file_path=file_path,
                    line_num=line_num,
                    issue_type='space_in_japanese',
                    message='日本語文中に半角スペースがあります',
                    suggestion='日本語文中では全角スペース「　」を使用してください',
                    severity='info'
                ))
            
            # 修正があった場合は内容を更新
            if line != original_line:
                lines[line_num - 1] = line
        
        if self.fix_mode:
            fixed_content = '\n'.join(lines)
        
        return fixed_content
    
    def check_common_mistakes(self, content: str, file_path: str):
        """よくある日本語の間違いをチェック"""
        lines = content.split('\n')
        
        # よくある誤用パターン
        common_mistakes = [
            (r'〜', '～', '波ダッシュ（～）を使用してください'),
            (r'出来る', 'できる', 'ひらがな表記を推奨します'),
            (r'下さい', 'ください', 'ひらがな表記を推奨します'), 
            (r'致します', 'いたします', 'ひらがな表記を推奨します'),
            (r'事', 'こと', '「こと」はひらがな表記を推奨します'),
            (r'時', 'とき', '「とき」はひらがな表記を推奨します'),
            (r'様に', 'ように', '「ように」はひらがな表記を推奨します'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            # コードブロック内は除外
            if line.strip().startswith('```') or line.strip().startswith('    '):
                continue
            
            for pattern, correction, suggestion in common_mistakes:
                if re.search(pattern, line):
                    self.add_issue(TextIssue(
                        file_path=file_path,
                        line_num=line_num,
                        issue_type='common_mistake',
                        message=f'一般的でない表記: {pattern}',
                        suggestion=suggestion,
                        severity='info'
                    ))
    
    def check_file(self, file_path: Path) -> str:
        """単一ファイルの日本語テキストをチェック"""
        self.log(f"日本語テキストチェック: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.add_issue(TextIssue(
                file_path=str(file_path),
                line_num=0,
                issue_type='file_read_error',
                message=f'ファイル読み込みエラー: {str(e)}',
                severity='error'
            ))
            return content
        
        # 各種チェックを実行
        self.check_politeness_consistency(content, str(file_path))
        content = self.check_tech_term_consistency(content, str(file_path))
        self.check_punctuation(content, str(file_path))
        content = self.check_character_width(content, str(file_path))
        self.check_common_mistakes(content, str(file_path))
        
        return content
    
    def run_check(self, target_file: str = None) -> bool:
        """日本語テキストチェックを実行"""
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
        
        self.log(f"{len(target_files)}個のファイルをチェック中...")
        
        # 各ファイルをチェック
        for md_file in target_files:
            fixed_content = self.check_file(md_file)
            
            # 修正モードで変更があった場合は書き戻し
            if self.fix_mode:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    if fixed_content != original_content:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(fixed_content)
                        self.log(f"修正済み: {md_file}")
                except Exception as e:
                    self.add_issue(TextIssue(
                        file_path=str(md_file),
                        line_num=0,
                        issue_type='file_write_error', 
                        message=f'ファイル書き込みエラー: {str(e)}',
                        severity='error'
                    ))
        
        # レポート生成
        return self.generate_report()
    
    def generate_report(self) -> bool:
        """チェック結果レポートの生成"""
        if not self.issues:
            print("✅ 日本語テキストチェック: 問題は見つかりませんでした")
            return True
        
        print(f"\n🇯🇵 日本語テキストチェック結果")
        print(f"━━━━━━━━━━━━━━━━━━━━━━")
        
        # 重要度別の集計
        severity_counts = {'error': 0, 'warning': 0, 'info': 0}
        for issue in self.issues:
            severity_counts[issue.severity] += 1
        
        print(f"エラー: {severity_counts['error']}")
        print(f"警告:   {severity_counts['warning']}")
        print(f"情報:   {severity_counts['info']}")
        
        # 問題タイプ別の集計
        type_counts = {}
        for issue in self.issues:
            type_counts[issue.issue_type] = type_counts.get(issue.issue_type, 0) + 1
        
        print(f"\n📊 問題の内訳:")
        type_names = {
            'inconsistent_politeness': '敬語の不統一',
            'inconsistent_tech_term': '技術用語の不統一', 
            'katakana_variant': 'カタカナ表記の不統一',
            'excessive_comma': '読点の過剰使用',
            'excessive_period': '句点の過剰使用',
            'mixed_punctuation': '句読点の混在',
            'full_width_numbers': '全角数字',
            'full_width_alphabet': '全角英字',
            'half_width_katakana': '半角カタカナ',
            'space_in_japanese': '日本語文中のスペース',
            'common_mistake': '一般的でない表記',
            'file_read_error': 'ファイル読み込みエラー',
            'file_write_error': 'ファイル書き込みエラー'
        }
        
        for issue_type, count in sorted(type_counts.items()):
            type_name = type_names.get(issue_type, issue_type)
            print(f"  {type_name}: {count}個")
        
        # 詳細リスト（警告以上のみ）
        critical_issues = [i for i in self.issues if i.severity in ['error', 'warning']]
        if critical_issues:
            print(f"\n📋 詳細（警告・エラーのみ）:")
            current_file = None
            severity_icons = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}
            
            for issue in sorted(critical_issues, key=lambda x: (x.file_path, x.line_num)):
                if issue.file_path != current_file:
                    print(f"\n📁 {issue.file_path}")
                    current_file = issue.file_path
                
                icon = severity_icons[issue.severity]
                print(f"  {icon} {issue.line_num}行目: {issue.message}")
                if issue.suggestion and self.verbose:
                    print(f"     💡 提案: {issue.suggestion}")
        
        has_errors = severity_counts['error'] > 0
        if has_errors:
            print(f"\n❌ {severity_counts['error']}個のエラーが見つかりました")
        elif severity_counts['warning'] > 0:
            print(f"\n⚠️  {severity_counts['warning']}個の警告があります")
        else:
            print(f"\n ℹ️  {severity_counts['info']}個の情報があります")
        
        return not has_errors


def main():
    parser = argparse.ArgumentParser(
        description='日本語テキスト品質チェックツール',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--fix', action='store_true', help='自動修正可能な問題を修正')
    parser.add_argument('--file', type=str, help='チェック対象のファイルを指定')
    parser.add_argument('--verbose', action='store_true', help='詳細な情報を表示')
    
    args = parser.parse_args()
    
    checker = JapaneseTextChecker(fix_mode=args.fix, verbose=args.verbose)
    success = checker.run_check(args.file)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()