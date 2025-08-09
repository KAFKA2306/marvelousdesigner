# Task Completion Workflow

## When Tasks Are Completed

Since this is a **documentation-only project** with no executable code, there are no traditional linting, formatting, or testing commands. However, there are important verification steps.

## Required Verification Steps

### 1. Content Verification
```bash
# Start local development server to verify changes
mkdocs serve
# → Check at http://127.0.0.1:8000
```

**Manual Verification Checklist:**
- [ ] New content displays correctly
- [ ] All internal links work
- [ ] Japanese text renders properly
- [ ] Navigation structure is intact
- [ ] Mobile view is functional
- [ ] Search functionality includes new content

### 2. Build Verification
```bash
# Test production build
mkdocs build
# → Check for any build errors
```

### 3. Git Workflow
```bash
# Add all changes
git add .

# Commit with proper attribution
git commit -m "[Action]: [Specific description]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to deploy (GitHub Pages auto-deploys)
git push origin main
```

## No Traditional Development Commands

### What This Project DOESN'T Have
- **No package managers**: No npm, pip, requirements.txt
- **No linting**: Markdown follows MkDocs conventions
- **No testing**: Manual content verification only
- **No compilation**: MkDocs handles all processing
- **No dependency management**: Only MkDocs and plugins

### What We DO Instead

#### Quality Assurance Through:
1. **Manual Review**: Content accuracy and completeness
2. **Local Testing**: MkDocs serve for real-time preview
3. **Build Testing**: MkDocs build to catch configuration errors
4. **Deployment Testing**: GitHub Pages automatic deployment verification

#### Content Quality Standards:
- All content must be in Japanese
- Beginner-accessible language
- Step-by-step instructions with time estimates
- Error recovery procedures included
- Cross-references to related content

## Task Types and Completion Criteria

### Documentation Tasks
**Completion Criteria:**
- Content written in proper Japanese
- Follows template structure
- All internal links functional
- Images (if any) display correctly
- Passes mkdocs build without errors

### Configuration Tasks (mkdocs.yml, etc.)
**Completion Criteria:**
- Configuration syntax valid
- Site builds successfully
- Navigation structure correct
- Plugins function properly
- Theme settings applied correctly

### Content Updates
**Completion Criteria:**
- Information accuracy verified
- Version numbers updated (if applicable)
- Related pages cross-referenced
- Changelog updated if significant

## Deployment Notes

- **Automatic Deployment**: GitHub Pages deploys automatically on push to main
- **No Manual Deployment**: No need to run mkdocs gh-deploy manually
- **Verification**: Check deployed site at production URL after push

## Emergency Procedures

### If Build Fails
```bash
# Check build errors
mkdocs build --verbose

# Fix configuration issues in mkdocs.yml
# Fix any broken markdown syntax
# Retry build
```

### If Deployment Fails
- Check GitHub Actions tab for deployment status
- Verify GitHub Pages settings in repository
- Check for any broken links or syntax errors

The key principle: **Manual verification replaces automated testing** in this documentation-focused project.