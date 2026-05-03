
import os
import re

def clean_ghost_slides(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove all python blocks at the very beginning (after YAML)
    # until the first markdown header or text
    if "---" in content:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            yaml = parts[1]
            rest = parts[2]
            
            # Remove leading python blocks in the 'rest' part
            rest = re.sub(r"^\s*```{python}.*?```", "", rest, flags=re.DOTALL)
            rest = re.sub(r"^\s*```{python}.*?```", "", rest, flags=re.DOTALL) # Twice for safety
            
            content = "---" + yaml + "---" + rest
            
    with open(filepath, 'w') as f:
        f.write(content)

clean_ghost_slides('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
clean_ghost_slides('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
