
import re
import os

def strip_fix_ar(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove fix_ar(...) wrapping but keep the inner content
    # This regex looks for fix_ar('...') or fix_ar("...")
    # It handles nested ones too if run multiple times
    for _ in range(5):
        content = re.sub(r"fix_ar\((['\"])(.*?)\1\)", r"\1\2\1", content)
    
    # 2. Fix the mess-ups like fix_ar(')
    content = content.replace("fix_ar(')", "'")
    content = content.replace('fix_ar(")', '"')
    content = content.replace("fix_ar('", "'")
    content = content.replace('fix_ar("', '"')
    content = content.replace("')", "'")
    content = content.replace('")', '"')
    content = content.replace("fix_ar(", "") # Final fallback
    
    # 3. Remove all fix_ar function definitions
    content = re.sub(r"import arabic_reshaper.*?return get_display\(arabic_reshaper\.reshape\(text\)\)", "", content, flags=re.DOTALL)
    content = re.sub(r"import arabic_reshaper.*?return get_display\(reshaped_text\)", "", content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

strip_fix_ar('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
strip_fix_ar('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
