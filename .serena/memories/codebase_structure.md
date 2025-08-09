# Codebase Structure

## Project Architecture
This is a **documentation-only project** with no executable code. The system is designed around content organization and user experience rather than code architecture.

## Root Directory Structure
```
/home/kafka/unity/marvelousdesigner/
├── README.md                          # Project marketing/overview
├── CLAUDE.md                          # AI development guidance
├── mkdocs.yml                         # Site configuration
├── tasks.md                           # Development task tracking
├── requirements.md                    # Project requirements
├── design.md                          # Documentation design
├── docs/                              # All content files
├── site/                              # Generated static files (auto-built)
├── overrides/                         # Theme customizations
└── .github/                           # GitHub configuration
```

## Content Organization (docs/)

### Learning Path Architecture
The content follows a progressive learning structure:

```
docs/
├── index.md                           # Welcome page with learning paths
├── setup/                             # Environment setup (3 files)
│   ├── software-check.md              # Installation verification
│   ├── md-first-launch.md             # Marvelous Designer first run
│   └── unity-vrchat-setup.md          # Unity + VRChat SDK setup
├── basics/                            # Foundational concepts (2-6 files)
│   ├── md-interface.md                # Marvelous Designer interface
│   ├── ai-features.md                 # AI feature guide (NEW)
│   └── [4 additional files planned]   # Basic concepts, terminology
├── workflows/                         # Core procedures (5-6 files)
│   ├── avatar-import.md               # FBX avatar import process
│   ├── garment-fitting.md             # PZIP garment adaptation
│   ├── modular-garments.md            # Modular system (NEW)
│   ├── avatar-modification.md         # Avatar modification (NEW)
│   └── common-issues.md               # Troubleshooting (NEW)
├── garments/                          # Clothing tutorials (3-6 files)
│   ├── t-shirt.md                     # Beginner: basic shirt creation
│   ├── skirt.md                       # Intermediate: pleats and flares (NEW)
│   ├── dress.md                       # Advanced: complex structures (NEW)
│   └── [3 additional types planned]   # Casual, one-piece, swimwear
├── physics/                           # Simulation settings (2-4 files)
│   ├── fabric-properties.md           # Material physics (NEW)
│   ├── optimization.md                # Performance tuning (NEW)
│   └── [2 additional files planned]   # Detailed simulation settings
├── unity/                             # VRChat integration (2-4 files)
│   ├── project-setup.md               # Unity project configuration (NEW)
│   ├── avatar-upload.md               # VRChat avatar upload
│   └── [2 additional files planned]   # SDK3 details, testing
├── resources/                         # Links and community (5 files)
│   ├── useful-links.md                # Curated links (NEW)
│   ├── clo-set-connect.md             # Platform integration (NEW)
│   ├── community.md                   # Community info (NEW)
│   ├── advanced-resources.md          # Advanced learning (NEW)
│   └── update-log.md                  # Change history (NEW)
├── stylesheets/
│   └── extra.css                      # Custom CSS for Japanese UI
└── javascripts/
    └── extra.js                       # UX enhancements
```

## Implementation Status
- **Completed**: 32/36 files (89%)
- **Production Ready**: Core learning path fully functional
- **Remaining**: 4 files (mostly optional enhancements)

## Key Architectural Decisions

### 1. Progressive Difficulty Design
```
🌱 Setup (3h) → 🌿 Basic Skills (15h) → 🌳 Advanced Techniques (30h)
```

### 2. Modular but Connected
- Each section can be referenced independently
- Heavy cross-referencing maintains learning flow
- Multiple entry points for different user needs

### 3. Japanese-First Architecture
- All navigation in Japanese
- Content structure follows Japanese learning preferences
- Cultural context integration throughout

### 4. VRChat-Specific Focus
- Every tutorial ends with VRChat implementation
- Performance optimization emphasized
- Real-world usage scenarios prioritized

## Technical Infrastructure

### MkDocs Configuration (mkdocs.yml)
- **Theme**: Material with Japanese localization
- **Plugins**: Search (ja), git-revision-date-localized
- **Extensions**: Admonitions, tabs, task lists, code highlighting
- **Colors**: Pink theme (matches VRChat aesthetic)
- **Fonts**: Noto Sans JP, Roboto Mono

### GitHub Integration
- **Pages**: Automatic deployment from main branch
- **Actions**: Built-in MkDocs deployment workflow
- **Issues**: Community feedback and bug reports

### Content Management
- **No CMS**: Direct markdown file editing
- **Version Control**: Git-based content versioning
- **Collaboration**: GitHub-based contribution workflow

## File Naming Conventions
- Kebab-case filenames: `avatar-import.md`
- Descriptive names matching content purpose
- English filenames for Japanese content (accessibility)
- Directory names reflect content categories

## Content Templates and Standards
Each major content type follows standardized templates:
- Time estimates and difficulty levels
- Step-by-step instruction format
- Troubleshooting sections
- Progress checklists
- Cross-references to related content

## Development Workflow
1. **Edit**: Direct markdown file editing
2. **Preview**: `mkdocs serve` for real-time preview
3. **Test**: `mkdocs build` to verify syntax
4. **Deploy**: Git push triggers automatic GitHub Pages deployment
