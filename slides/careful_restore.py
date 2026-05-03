
import re
import os

def careful_restore(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    new_lines = []
    in_python = False
    for line in lines:
        if line.startswith('```{python}'): in_python = True
        if line.startswith('```'): in_python = False
        
        if in_python:
            # Fix patterns like color='#...'), 
            line = line.replace("'), ", "', ")
            
            # Fix lines that should end with ) but don't
            # Looking for common terminal arguments
            if re.search(r"(label='[^']*'|color='#?[0-9A-Fa-f]*'|alpha=[0-9.]+|linewidth=[0-9.]+)\s*$", line.strip()) and line.count('(') > line.count(')'):
                line = line.rstrip() + ")\n"
                
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

careful_restore('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
careful_restore('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
