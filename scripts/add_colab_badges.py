import json
import os

repo_base = "https://colab.research.google.com/github/hanenalmayouf/Computer_vision_Arabic-/blob/main/labs/"

labs = [
    "00_images.ipynb",
    "01_tasks_inference_ar.ipynb",
    "02_solutions_expanded.ipynb",
    "02b_video_engineering.ipynb",
    "03_custom_training.ipynb",
    "04a_roi_evaluation.ipynb",
    "04b_evaluation_technical.ipynb",
    "05_huggingface_cv_ar.ipynb"
]

labs_dir = "/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/"

for lab in labs:
    path = os.path.join(labs_dir, lab)
    if not os.path.exists(path):
        print(f"Skipping {lab}, not found.")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Find first markdown cell
    for cell in data['cells']:
        if cell['cell_type'] == 'markdown':
            source = cell['source']
            colab_link = f"{repo_base}{lab}"
            badge_md = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link})\n\n"
            
            # Check if badge already exists
            if any("colab-badge.svg" in line for line in source):
                print(f"Badge already exists in {lab}.")
                break
                
            # Insert badge after <div dir="rtl"> if present, otherwise at top
            inserted = False
            for i, line in enumerate(source):
                if '<div dir="rtl">' in line:
                    source.insert(i + 1, "\n")
                    source.insert(i + 2, badge_md)
                    inserted = True
                    break
            
            if not inserted:
                source.insert(0, badge_md)
            
            cell['source'] = source
            print(f"Added badge to {lab}.")
            
            with open(path, 'w', encoding='utf-8') as f_out:
                json.dump(data, f_out, ensure_ascii=False, indent=1)
            break
