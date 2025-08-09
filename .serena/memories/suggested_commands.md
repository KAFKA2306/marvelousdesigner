# Suggested Commands

## MkDocs Development Commands

### Core Development Workflow
```bash
# Start development server (auto-reload on changes)
mkdocs serve
# → Serves at http://127.0.0.1:8000

# Build static site for production
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy

# Show required packages for current configuration
mkdocs get-deps
```

### Git Workflow
```bash
# Standard commit with Claude Code attribution
git add .
git commit -m "[Action]: [Specific update description]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to trigger GitHub Pages deployment
git push origin main
```

### File System Navigation
```bash
# List project structure
ls -la

# Navigate to docs directory
cd docs/

# Find specific files
find . -name "*.md" | head -10

# Search content (use ripgrep if available)
rg "pattern" --type md

# Check current working directory
pwd
```

### System Information
```bash
# Check MkDocs version
mkdocs --version

# Check Python version
python3 --version

# Check Git status
git status

# Check current branch
git branch
```

## Important Notes

- **No package managers**: This is a documentation-only project with no executable code
- **No testing**: Content verification is done manually through MkDocs serve
- **No linting**: Markdown follows MkDocs Material conventions
- **No build process**: MkDocs handles all build operations
- **Auto-deployment**: GitHub Pages automatically deploys on push to main branch

## Development Environment

The project runs on:
- **System**: Linux (WSL2)
- **MkDocs Version**: 1.6.1
- **Python Version**: 3.10
- **Theme**: Material (Japanese localized)

## File Structure Navigation

```
docs/                    # All content files
├── setup/              # Environment setup guides
├── basics/             # Foundation knowledge
├── workflows/          # Core procedures
├── garments/           # Clothing tutorials
├── physics/            # Simulation settings
├── unity/              # VRChat integration
└── resources/          # Links and community

mkdocs.yml              # Site configuration
README.md               # Project information
CLAUDE.md               # AI development guidance
```
