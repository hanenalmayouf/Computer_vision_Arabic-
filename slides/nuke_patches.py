
import re
import os

def nuke_patches(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all Python blocks
    blocks = re.split(r'(```{python}.*?```)', content, flags=re.DOTALL)
    
    new_blocks = []
    for block in blocks:
        if block.startswith('```{python}'):
            # If it's a PATCH block (contains our logic but NOT the actual plot data)
            if 'patch_matplotlib' in block or 'arabic_reshaper' in block or 'fix_ar' in block or 'SVG-Native' in block:
                # NUKE IT
                continue
        new_blocks.append(block)
    
    new_content = "".join(new_blocks)
    with open(filepath, 'w') as f:
        f.write(new_content)

nuke_patches('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
nuke_patches('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
