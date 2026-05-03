
import os

def final_syntax_fix(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix specific multiline patterns
    content = content.replace("color='#dc3545')\n\nax.set_", "color='#dc3545'))\n\nax.set_")
    content = content.replace("color='#E07B39', lw=1.2)\n\nax.set_", "color='#E07B39', lw=1.2))\n\nax.set_")
    
    # Brute force fix for specific lines
    lines = content.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        if "arrowprops=dict" in line and i < len(lines)-1:
            if lines[i+1].strip().startswith("ax.set") or lines[i+1].strip() == "":
                if line.count('(') > line.count(')'):
                    line = line.rstrip() + ')'
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    with open(filepath, 'w') as f:
        f.write(content)

final_syntax_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
final_syntax_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
