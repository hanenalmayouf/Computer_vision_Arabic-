
import os

def brute_force_fix(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Fix broken ax.plot and ax.bar calls
    content = content.replace("color='#1C355E'), linewidth", "color='#1C355E', linewidth")
    content = content.replace("color='#1C355E'), alpha", "color='#1C355E', alpha")
    content = content.replace("color='#00C9A7'), linewidth", "color='#00C9A7', linewidth")
    
    # Fix missing closing parentheses at end of lines
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if ('ax.plot(' in line or 'ax.bar(' in line or 'ax.barh(' in line or 'ax.text(' in line or 'ax.annotate(' in line) and line.count('(') > line.count(')'):
            if not line.strip().endswith(')'):
                line = line.rstrip() + ')'
        new_lines.append(line)
        
    content = '\n'.join(new_lines)
    
    with open(filepath, 'w') as f:
        f.write(content)

brute_force_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
brute_force_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
