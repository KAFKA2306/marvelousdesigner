# Marvelous Designer Critical Issues Technical Investigation

## Investigation Summary
Conducted comprehensive research into three workflow-blocking issues affecting VRChat garment creation in Marvelous Designer 2025. Successfully enhanced documentation with actionable technical solutions.

## Critical Issues Investigated

### Issue 1: Fitting Suit Auto-Generation Error
**Error**: "配置点をアバターに合わせることができませんでした。AまたはTポーズでのみ正常に動作します"
**Context**: Users report T-pose compliance but continued failures

**Key Findings**:
- MD 2025 strict T-pose validation: arms exactly horizontal (90°), palms down
- A-pose alternative: arms 30-45° below horizontal often works better
- Version 2024.0.149+ has known custom avatar arrangement point bugs
- Auto-mapping supports DAZ Genesis 8/9, Mixamo, Metahuman
- Manual workaround: Avatar Editor → IK Mapping → manual joint connection

**Critical Requirements**:
- Avatar height under 2 meters
- No duplicate joint names in FBX
- Bone naming must match MD standards
- "Automatically Add Arrangement Points" checkbox during import

### Issue 2: EveryWear Rigging Transfer Failure
**Error**: "failed to transfer the avatar's rigging information to the garment"
**Context**: Connected to fitting suit problems, cascade failure

**Key Findings**:
- EveryWear requires successful fitting suit creation as prerequisite
- Only works with 2D pattern-based garments
- Custom garments need "Garment Fitting Suite" present
- VRChat specific: Upper Chest bone must NOT be assigned

**Recovery Strategies**:
- Manual rigging via OBJ export → Blender weight painting → FBX re-import
- Bone hierarchy validation: Shoulder must be direct child of Chest
- MD restart often resolves "EveryWear refuses to open" errors

### Issue 3: Unity Modular Avatar Integration
**Error**: Outfit doesn't follow rig in Unity/Modular Avatar setup
**Context**: Final failure point due to missing/corrupted rigging

**Key Findings**:
- Skinned Mesh Renderer configuration critical
- Optimized meshes use bone names, non-optimized use bone order
- Modular Avatar Armature Link requires exact bone name matching
- "Align Rotation" checkbox often needs to be unchecked

**Workflow Optimization**:
- MD OBJ export → Blender skeleton transfer → weight painting → Unity
- VRCFury Linking Clothes as alternative to Modular Avatar
- Performance rating validation essential

## Documentation Enhancement Strategy

### Enhanced Sections in common-issues.md:
1. **VRChat アバター・衣装統合の重大エラー** - New major section
2. Three detailed troubleshooting entries with:
   - Diagnostic checklists
   - Step-by-step recovery procedures
   - Version-specific considerations
   - Alternative workflows

### Writing Approach:
- Maintained Japanese beginner-friendly tone
- Used technical accuracy with accessibility
- Provided both automatic and manual solutions
- Included prevention strategies

## Future Documentation Implications

### Workflow Documentation Updates Needed:
- Avatar import procedure enhancement
- T-pose/A-pose preparation guide
- Manual rigging fallback procedures
- Unity integration best practices

### Training Content Opportunities:
- Video tutorials for manual arrangement point setup
- Blender-MD-Unity pipeline documentation
- Troubleshooting workflow diagrams

## Research Sources Utilized:
- Marvelous Designer official support forums
- CLO SET Connect community posts
- Unity documentation on rigging
- VRChat creator documentation
- Modular Avatar technical guides

## Token Efficiency Lessons:
- Web search yielded comprehensive technical details
- Existing documentation structure provided perfect integration point
- Strategic regex replacement preserved formatting while adding substantial content
- Research-first approach prevented redundant investigation rounds
