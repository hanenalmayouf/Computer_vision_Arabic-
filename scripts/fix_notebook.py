import json
import os

notebook_path = r"c:\Users\nayef\Downloads\ultralytics\labs\04_evaluation.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Replacements
replacements = {
    'weights/yolo26n.pt': 'yolo26n.pt',
    'yolo26s.pt': 'yolo26n.pt'
}

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        new_source = []
        for line in cell['source']:
            for old, new in replacements.items():
                line = line.replace(old, new)
            new_source.append(line)
        cell['source'] = new_source

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("Notebook updated successfully.")
