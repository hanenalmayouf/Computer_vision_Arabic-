
import re
import os

def restore_syntax(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        # If line ends with a string literal and looks like a function call that was cut off
        if re.search(r"['\"]\s*$", line.strip()) and "(" in line and ")" not in line:
            line = line.rstrip() + ")\n"
        # Specific fixes for common patterns
        if "color='#1C355E'" in line and "')" not in line:
            line = line.replace("color='#1C355E'", "color='#1C355E')")
        if "set_color('#1C355E'" in line and "')" not in line:
            line = line.replace("set_color('#1C355E'", "set_color('#1C355E')")
        if "set_visible(False" in line and "False)" not in line:
            line = line.replace("set_visible(False", "set_visible(False)")
            
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

restore_syntax('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
restore_syntax('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
