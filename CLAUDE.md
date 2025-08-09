# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Japanese-language VRChat garment creation guide** built with MkDocs. It provides comprehensive documentation for creating VRChat avatar clothing using Marvelous Designer and Unity, targeting complete beginners.

## Development Commands

### MkDocs Operations
```bash
# Start development server (auto-reload on changes)
mkdocs serve

# Build static site for production
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy

# Show required packages for current configuration
mkdocs get-deps
```

## Project Architecture

This is a **documentation-only project** with no executable code. The system is designed around:

### Content Organization
```
docs/
├── index.md                    # Welcome page with learning paths
├── setup/                      # Environment setup (3 files)
│   ├── software-check.md       # Installation verification
│   ├── md-first-launch.md      # Marvelous Designer first run
│   └── unity-vrchat-setup.md   # Unity + VRChat SDK setup
├── basics/                     # Foundational concepts
│   └── md-interface.md         # Marvelous Designer interface
├── workflows/                  # Core procedures (4 files)
│   ├── avatar-import.md        # FBX avatar import process
│   └── garment-fitting.md      # PZIP garment adaptation
├── garments/                   # Clothing tutorials (2+ files)
│   ├── t-shirt.md              # Beginner: basic shirt creation
│   └── skirt.md                # Intermediate: pleats and flares
├── physics/                    # Simulation settings (2 files)
│   ├── fabric-properties.md    # Material physics configuration
│   └── optimization.md         # Performance tuning
├── unity/                      # VRChat integration (2 files)
│   ├── project-setup.md        # Unity project configuration
│   └── avatar-upload.md        # VRChat avatar upload
└── resources/                  # Links and community info
```

### Learning Architecture
1. **Progressive Difficulty**: Content flows from basic setup → simple creation → complex garments → optimization
2. **Modular Structure**: Each section can be referenced independently while maintaining learning flow
3. **Cross-Reference Network**: Heavy internal linking between related concepts across sections
4. **Japanese-First Design**: All terminology, navigation, and explanations optimized for Japanese beginners

### Content Design Patterns
- **Standardized Tutorial Format**: Each garment follows consistent 5-phase structure (design → placement → simulation → adjustment → export)
- **Time Estimates**: Realistic completion times for each section (15min - 12 hours)
- **Difficulty Indicators**: Clear skill level markers for each tutorial
- **Error Prevention**: Proactive warnings about common mistakes before they occur

## MkDocs Configuration

### Theme Features
- Material theme with Japanese language support (`language: ja`)
- Dual color scheme (light/dark) with pink primary colors
- Japanese fonts: Noto Sans JP for text, Roboto Mono for code
- Custom HTML template in `overrides/main.html` for Google verification

### Key Plugins
```yaml
plugins:
  - search:
      lang: ja                          # Japanese search indexing
  - git-revision-date-localized:
      type: date
      locale: ja                        # Japanese date formatting
      timezone: Asia/Tokyo
```

### Critical Markdown Extensions
- `admonition` + `pymdownx.details`: Collapsible tips/warnings
- `pymdownx.tabbed`: Multiple learning path presentations
- `pymdownx.superfences`: Code blocks with syntax highlighting
- `toc`: Japanese table of contents generation
- `pymdownx.tasklist`: Interactive checklists for progress tracking

## Content Guidelines

### Language Requirements
- **Japanese Only**: All content must be in Japanese
- **Beginner-Friendly**: No assumed prior knowledge of 3D modeling or VRChat
- **Natural Phrasing**: Avoid direct translations; use naturally Japanese explanations
- **Consistent Terminology**: Standard Japanese terms for technical concepts

### Writing Patterns
- **Question-Based Sections**: Address common anxieties ("私にもできるかな？")
- **Step-by-Step Instructions**: Numbered procedures with time estimates
- **Safety-First Approach**: Always explain how to undo/recover from errors
- **Version Awareness**: Track specific software versions (current: MD 2025, Unity 2022.3.22f1, VRChat SDK3 v3.8.2)

### Structure Requirements
Each tutorial must include:
- Difficulty level and time estimate
- Prerequisites and file requirements
- 5-phase step-by-step process
- Common troubleshooting points
- Next learning steps

## Technical Details

### File Organization
- `mkdocs.yml`: Complete site configuration with Japanese localization
- `docs/javascripts/extra.js`: Custom JavaScript for enhanced UX
- `docs/stylesheets/extra.css`: Custom CSS for Japanese-optimized design
- `site/`: Generated static files (auto-built)
- `overrides/`: Template customizations

### External Dependencies
- Google Analytics integration (configured but anonymized ID)
- GitHub Pages deployment ready
- Social media links (GitHub repository)

### Development Workflow
This project requires no compilation or testing. Changes to `.md` files in `docs/` are immediately reflected via `mkdocs serve`. The content architecture supports both sequential learning (beginner path) and reference-style access (experienced users jumping to specific sections).
