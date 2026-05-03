
import re
import os

def thorough_clean(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove all python blocks that look like our patch
    # We'll search for blocks containing 'arabic_reshaper'
    content = re.sub(r"```{python}\n#\| echo: false\n.*?arabic_reshaper.*?```", "", content, flags=re.DOTALL)
    
    # 2. Also remove any other blocks that might have been injected previously
    content = re.sub(r"```{python}\nimport matplotlib\.pyplot as plt\nimport arabic_reshaper.*?```", "", content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

thorough_clean('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
thorough_clean('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
