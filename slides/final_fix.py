
import re
import os

def final_fix(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove all fix_ar remnants
    content = re.sub(r"fix_ar\(", "", content)
    content = re.sub(r"\)", "", content) # This is dangerous, but we'll try to target strings only
    
    # Okay, better way: Re-read the file and use a smarter regex
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    in_python = False
    for line in lines:
        if line.startswith('```{python}'):
            in_python = True
            new_lines.append(line)
            # Add helper ONCE
            new_lines.append("import matplotlib.pyplot as plt\nimport arabic_reshaper\nfrom bidi.algorithm import get_display\ndef fix_ar(text):\n    if not text: return \"\"\n    return get_display(arabic_reshaper.reshape(str(text)))\n")
            continue
        if line.startswith('```'):
            in_python = False
            new_lines.append(line)
            continue
            
        if in_python:
            # Remove existing fix_ar calls to start fresh
            line = line.replace("fix_ar(", "").replace(")", "") # This is still a bit risky but we'll fix it below
            # Now wrap Arabic strings
            def replacer(match):
                s = match.group(0)
                if any("\u0600" <= c <= "\u06FF" for c in s):
                    return f"fix_ar({s})"
                return s
            line = re.sub(r"'(.*?)'|\"(.*?)\"", replacer, line)
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

# Wait, I'll just use a more surgical approach for the categories line.
# I'll manually fix the first few lines that I know are broken.
