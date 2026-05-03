
import re
import os

def fix_colors(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # In regular slides (white background), we want Navy text (#1C355E)
    # In .sdaia-dark slides (dark background), we want White text (#FFFFFF)
    
    # Let's start by fixing all #FFFFFF in Python blocks back to #1C355E 
    # UNLESS the slide has .sdaia-dark
    
    blocks = re.split(r'(## .*?\n|# .*?\n)', content)
    
    new_blocks = []
    current_slide_is_dark = False
    
    for block in blocks:
        if block.startswith('#') or block.startswith('##'):
            if ".sdaia-dark" in block:
                current_slide_is_dark = True
            else:
                current_slide_is_dark = False
            new_blocks.append(block)
            continue
            
        # If it's a Python block inside this section
        if current_slide_is_dark:
            # Keep or set to White
            pass
        else:
            # Set to Navy
            if '```{python}' in block:
                block = block.replace('#FFFFFF', '#1C355E')
                block = block.replace('#ffffff', '#1C355E')
                block = block.replace('white', '#1C355E') # Careful with this
        
        new_blocks.append(block)

    new_content = "".join(new_blocks)
    with open(filepath, 'w') as f:
        f.write(new_content)

fix_colors('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
fix_colors('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
