
import re
import os

def fix_ar_content(block):
    # Regex for strings containing Arabic characters
    # This targets strings like '...' or "..." that have at least one Arabic char
    def replacer(match):
        s = match.group(0)
        # Check if it has Arabic
        if any("\u0600" <= c <= "\u06FF" for c in s):
            # Avoid double wrapping
            if match.start() > 7 and block[match.start()-7:match.start()] == "fix_ar(":
                return s
            return f"fix_ar({s})"
        return s

    # Match single and double quoted strings
    # Handles escaped quotes too
    pattern = r"'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\""
    return re.sub(pattern, replacer, block)

def process_qmd(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Split by code blocks
    parts = re.split(r'(```{python}.*?```)', content, flags=re.DOTALL)
    
    new_parts = []
    for part in parts:
        if part.startswith('```{python}'):
            # 1. Add helper function if Matplotlib is used
            if "import matplotlib" in part and "def fix_ar" not in part:
                part = part.replace("import matplotlib.pyplot as plt", 
                                      "import matplotlib.pyplot as plt\nimport arabic_reshaper\nfrom bidi.algorithm import get_display\ndef fix_ar(text):\n    if not text: return \"\"\n    return get_display(arabic_reshaper.reshape(text))")
            
            # 2. Wrap Arabic strings in fix_ar()
            part = fix_ar_content(part)
            
        new_parts.append(part)
    
    new_content = "".join(new_parts)
    
    with open(filepath, 'w') as f:
        f.write(new_content)

process_qmd('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
process_qmd('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
