# Code Style and Conventions

## Documentation Format
This is a **documentation-only project** with no executable code. All content follows MkDocs Material theme conventions.

## Markdown Style Guidelines

### Page Structure Template
```markdown
# Page Title in Japanese

!!! info "ページ情報"
    **所要時間**: XX分 | **難易度**: 初心者向け | **重要度**: 必須

## 段階的実装
!!! example "ステップ 1-2: 具体的作業"
    詳細手順

!!! tip "実践のコツ"
    効率化・品質向上アドバイス

??? question "「よくある問題」"
    **対処法**: 詳細解決策

!!! success "チェックリスト"
    - [ ] 確認項目

## 🌟 次のステップ
[関連ページ](link.md){ .md-button .md-button--primary }
```

### Language Requirements
- **Japanese Only**: All content must be in Japanese
- **Beginner-Friendly**: No assumed prior knowledge
- **Natural Phrasing**: Avoid direct translations; use naturally Japanese explanations
- **Consistent Terminology**: Standard Japanese terms for technical concepts

### Content Conventions

#### Admonition Usage
- `!!! info`: Basic information blocks
- `!!! tip`: Practical advice and tips
- `!!! warning`: Important cautions
- `??? question`: Collapsible FAQ items
- `!!! success`: Checklists and completion markers

#### Time and Difficulty Indicators
- Always include estimated completion time
- Use consistent difficulty levels: 初心者向け, 中級者向け, 上級者向け
- Mark importance: 必須, 推奨, オプション

#### Navigation Patterns
- Use emoji prefixes consistently (🌟, 🛠️, 📖, etc.)
- Include "次のステップ" (Next Steps) sections
- Cross-reference related content extensively

## File Organization Conventions

### Directory Structure
```
docs/
├── setup/              # 環境設定 (Environment Setup)
├── basics/             # 基礎知識 (Foundation Knowledge)
├── workflows/          # 作業手順 (Core Procedures)
├── garments/           # 衣装別制作ガイド (Garment Tutorials)
├── physics/            # 物理設定 (Physics Settings)
├── unity/              # Unity統合 (Unity Integration)
└── resources/          # リソース (Resources & Community)
```

### Filename Conventions
- Use kebab-case: `file-name.md`
- Japanese concepts in English filenames: `garment-fitting.md`
- Descriptive names that match content

### Content Flow Design
1. **Progressive Difficulty**: Content flows from basic setup → simple creation → complex garments → optimization
2. **Modular Structure**: Each section can be referenced independently while maintaining learning flow
3. **Cross-Reference Network**: Heavy internal linking between related concepts across sections

## MkDocs Configuration Standards

### Theme Settings
- Language: `ja` (Japanese)
- Primary color: `pink`
- Font: `Noto Sans JP` for text, `Roboto Mono` for code
- Features: navigation tabs, search, code copy, dark mode toggle

### Plugin Requirements
- `search` with Japanese language support
- `git-revision-date-localized` for Japanese date formatting
- Markdown extensions: admonition, tabbed content, task lists

## Quality Standards

### Technical Quality Checklist
- [ ] Latest software version compatibility verified
- [ ] All links functional
- [ ] Mobile responsive design
- [ ] Japanese fonts display correctly
- [ ] Search functionality works in Japanese

### Content Quality Checklist
- [ ] Complete beginners can follow independently
- [ ] No missing steps or assumptions
- [ ] Natural Japanese language usage
- [ ] Technical terms properly explained
- [ ] Error recovery procedures included

## Writing Patterns
- **Question-Based Sections**: Address common anxieties ("私にもできるかな？")
- **Step-by-Step Instructions**: Numbered procedures with time estimates
- **Safety-First Approach**: Always explain how to undo/recover from errors
- **Version Awareness**: Track specific software versions (MD 2025, Unity 2022.3.22f1, VRChat SDK3 v3.8.2)
