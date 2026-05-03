
import re
import os

def final_clean(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove double wrapping recursively
    # fix_ar(fix_ar('...')) -> fix_ar('...')
    for _ in range(3):
        content = re.sub(r"fix_ar\(fix_ar\((.*?)\)\)", r"fix_ar(\1)", content)
        content = re.sub(r"fix_ar\(x\) for x in \[fix_ar\((.*?)\)\]", r"fix_ar(x) for x in [\1]", content)

    # Remove unnecessary wraps on non-arabic strings
    # e.g. fix_ar('center'), fix_ar('left'), fix_ar('bold'), fix_ar('white')
    content = content.replace("fix_ar('center')", "'center'")
    content = content.replace("fix_ar('left')", "'left'")
    content = content.replace("fix_ar('bold')", "'bold'")
    content = content.replace("fix_ar('white')", "'white'")
    content = content.replace('fix_ar("center")', '"center"')
    content = content.replace('fix_ar("left")', '"left"')
    content = content.replace('fix_ar("bold")', '"bold"')
    content = content.replace('fix_ar("white")', '"white"')

    with open(filepath, 'w') as f:
        f.write(content)

final_clean('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
final_clean('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
