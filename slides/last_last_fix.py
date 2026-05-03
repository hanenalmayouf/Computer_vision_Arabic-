
import os

def last_last_fix(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix the specific ax.annotate and ax.axis issues
    content = content.replace('connectionstyle="arc3,rad=0.2")', 'connectionstyle="arc3,rad=0.2"))')
    content = content.replace("'equal'; ax.axis('off')", "'equal'); ax.axis('off')")
    
    with open(filepath, 'w') as f:
        f.write(content)

last_last_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
last_last_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
