
import re
import os

def clean_qmd(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove all double/triple fix_ar wraps
    # e.g. fix_ar(fix_ar('...')) -> fix_ar('...')
    while "fix_ar(fix_ar(" in content:
        content = re.sub(r"fix_ar\(fix_ar\((.*?)\)\)", r"fix_ar(\1)", content)

    # 2. Remove all fix_ar calls inside strings (from my previous buggy script)
    # e.g. '... fix_ar("...") ...'
    content = content.replace('fix_ar("', '"')
    content = content.replace('")', '"')

    # 3. Standardize the fix_ar function definition
    # Remove all existing definitions
    content = re.sub(r"import arabic_reshaper.*?return get_display\(arabic_reshaper\.reshape\(text\)\)", "", content, flags=re.DOTALL)
    
    # 4. Add the definition ONCE at the top of the first Python block
    # We'll find the first ```{python}
    def add_definition(match):
        return match.group(0) + "\nimport matplotlib.pyplot as plt\nimport arabic_reshaper\nfrom bidi.algorithm import get_display\ndef fix_ar(text):\n    if not text: return \"\"\n    return get_display(arabic_reshaper.reshape(text))\n"

    content = re.sub(r"```{python}", add_definition, content, count=1)

    with open(filepath, 'w') as f:
        f.write(content)

clean_qmd('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
clean_qmd('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
