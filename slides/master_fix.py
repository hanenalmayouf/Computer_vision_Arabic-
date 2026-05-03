
import re
import os

def master_fix(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Translate remaining Arabic in plots
    translations = {
        'أفضل F1 عند conf=': 'Best F1 at conf=',
        'الدرجة (%)': 'Score (%)',
        'عتبة الثقة (Confidence Threshold)': 'Confidence Threshold',
        'إجمالي الخسارة المالية ($)': 'Total Financial Loss ($)',
        'عتبة القرار (Decision Threshold)': 'Decision Threshold',
        'أقل خسارة عند': 'Min loss at',
        'الحقيقة (GT)': 'Ground Truth (GT)',
        'التوقع': 'Prediction',
        'الضبط (Precision)': 'Precision',
        'الاستدعاء (Recall)': 'Recall',
        'مقياس F1': 'F1 Score',
        'الدقة المتوازنة': 'Balanced Accuracy',
        'الدرجة': 'Score',
        'أفضل F1': 'Best F1',
        'منطقة الربح': 'Profit Zone',
        'منطقة الخسارة': 'Loss Zone'
    }
    for ar, en in translations.items():
        content = content.replace(ar, en)

    # 2. Fix indentation and syntax errors in ax.text and ax.annotate
    # We'll look for ), followed by an indented line
    content = re.sub(r',\)\n\s+', ',\n            ', content)
    
    # Fix misplaced closing parentheses
    content = re.sub(r"color='#?[A-Fa-f0-9]*'\),", "color='#1C355E',", content)
    
    # Fix unmatched parentheses in common plotting calls
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if ('ax.' in line) and line.count('(') > line.count(')'):
            if not line.strip().endswith(',') and not line.strip().endswith('('):
                line = line.rstrip() + ')'
        new_lines.append(line)
    content = '\n'.join(new_lines)

    with open(filepath, 'w') as f:
        f.write(content)

master_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
master_fix('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
