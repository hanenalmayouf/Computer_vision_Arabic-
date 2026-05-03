
import re
import os

PATCH_CODE = r"""
```{python}
#| echo: false
#| output: false
import matplotlib.pyplot as plt
try:
    import matplotlib_inline.backend_inline
    matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
except:
    pass
plt.rcParams['svg.fonttype'] = 'none'

def fix_ar(text):
    return text
```
"""

def inject_silent_patch(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Inject after YAML
    if "---" in content:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = "---" + parts[1] + "---" + PATCH_CODE + parts[2]
            
    with open(filepath, 'w') as f:
        f.write(content)

inject_silent_patch('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
inject_silent_patch('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
