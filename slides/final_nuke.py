
import os

def final_nuke(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if 'matplotlib.axes.Axes' in line or 'patch_matplotlib' in line or '_patched_' in line:
            continue
        new_lines.append(line)
        
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

final_nuke('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
final_nuke('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
