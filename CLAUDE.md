# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Japanese-language VRChat garment creation guide** built with MkDocs. It provides comprehensive documentation for creating VRChat avatar clothing using Marvelous Designer and Unity, targeting complete beginners.

## Project Structure

```
/
├── mkdocs.yml              # MkDocs configuration
├── docs/                   # Main documentation content
│   ├── setup/             # Environment setup guides
│   ├── basics/            # Basic concepts and interface
│   ├── workflows/         # Step-by-step procedures
│   ├── garments/          # Clothing-specific tutorials
│   ├── physics/           # Physics simulation settings
│   ├── unity/             # Unity integration guides
│   └── resources/         # Links and community resources
├── design.md              # Technical design document
└── requirements.md        # Project requirements
```

## Development Commands

### Build and Serve Documentation
```bash
# Start development server (auto-reload on changes)
mkdocs serve

# Build static site for production
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

### Check Dependencies
```bash
# Show required packages for current configuration
mkdocs get-deps
```

## Content Guidelines

### Language and Audience
- **Language**: Japanese only - all content must be in Japanese
- **Target Audience**: Complete beginners to VRChat garment creation
- **Software Focus**: Marvelous Designer + Unity + VRChat SDK3

### Content Structure
Each garment guide follows this pattern:
- Difficulty level and time estimate
- Prerequisites and required materials
- Step-by-step instructions (5 main phases)
- Troubleshooting tips specific to that garment type
- Next steps for advancement

### Key Content Areas
1. **Software Setup**: Installation and first-time configuration
2. **Basic Concepts**: 3D modeling fundamentals for beginners
3. **Workflows**: Standardized procedures for avatar import, fitting, creation
4. **Garment Tutorials**: T-shirts → Skirts → Dresses → Advanced items
5. **Physics Configuration**: Fabric properties and simulation optimization
6. **Unity Integration**: VRChat SDK3 setup and avatar upload process

## Technical Configuration

### MkDocs Theme
- Uses Material theme with Japanese localization
- Pink color scheme with light/dark mode toggle
- Japanese font: Noto Sans JP
- Mobile-responsive design

### Key Plugins
- `search`: Japanese language search
- `git-revision-date-localized`: Japanese date formatting
- `minify`: HTML optimization

### Markdown Extensions
- Admonitions for tips/warnings
- Code highlighting
- Tabbed content
- Task lists
- Japanese table of contents

## Architecture Notes

This is a **documentation-only project** - no executable code. The architecture centers around:

1. **Hierarchical Learning Path**: Content progresses from basic setup to advanced techniques
2. **Modular Guide Structure**: Each clothing type is self-contained but references common workflows
3. **Cross-Reference System**: Heavy linking between related concepts across different sections
4. **Japanese UX Optimization**: Navigation and terminology designed specifically for Japanese users

## Important Context

- **No executable code**: This project contains only Markdown documentation and MkDocs configuration
- **Image-light approach**: Relies on detailed text descriptions rather than screenshots
- **Beginner-focused**: Every concept explained from first principles
- **Version-aware**: Tracks latest software versions (Marvelous Designer, Unity, VRChat SDK3)