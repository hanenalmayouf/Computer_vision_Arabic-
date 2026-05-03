
import os

def path_fix_v2(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    content = content.replace("abspath('.');", "abspath('.'));")
    content = content.replace("abspath('slides');", "abspath('slides'));")
    
    with open(filepath, 'w') as f:
        f.write(content)

path_fix_v2('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
path_fix_v2('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
