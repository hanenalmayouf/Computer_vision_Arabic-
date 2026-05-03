
import re
import os

PATCH_CODE = r"""
```{python}
#| echo: false
import matplotlib.pyplot as plt
import numpy as np
try:
    import matplotlib_inline.backend_inline
    matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
except:
    pass

# Use SVG and let the browser handle Arabic rendering automatically
plt.rcParams['svg.fonttype'] = 'none'

def fix_ar(text):
    # No reshaping or bidi needed for SVG mode with browser rendering
    return text

print("SVG-Native Arabic support enabled (Python level).")
```
"""

def inject_patch(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. YAML cleanup
    content = content.replace("fig-format: svg", "") # Remove from YAML to avoid conflict
    
    # 2. Clean previous patches
    content = re.sub(r"```{python}\n#\| echo: false\n.*?patch_matplotlib.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r"```{python}\n#\| echo: false\n.*?SVG-Native.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r"```{python}\n#\| echo: false\n.*?SVG-based.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r"```{python}\n#\| echo: false\n.*?SVG-Native.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r"```{python}\n#\| echo: false\n.*?_patched_final.*?```", "", content, flags=re.DOTALL)

    # 3. Inject new patch
    if "---" in content:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = "---" + parts[1] + "---" + PATCH_CODE + parts[2]
            
    with open(filepath, 'w') as f:
        f.write(content)

inject_patch('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
inject_patch('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
