import json
import os

def update_notebook(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # 1. Add imports to the setup cell
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if 'import numpy' in source:
                new_lines = []
                for line in cell['source']:
                    new_lines.append(line)
                    if 'PIL' in line and 'import os' not in source:
                        new_lines.append("import os\n")
                        new_lines.append("import requests\n")
                cell['source'] = new_lines
                break

    # 2. Update image loading cell
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if 'image_file_path = "horse.png"' in source and 'requests' not in source:
                cell['source'] = [
                    'image_file_path = "horse.png"\n',
                    '\n',
                    '# Download the image if it doesn\'t exist\n',
                    'if not os.path.exists(image_file_path):\n',
                    '    url = f"https://raw.githubusercontent.com/NaifMersal/cv-for-developers-ultralytics/main/labs/{image_file_path}"\n',
                    '    r = requests.get(url)\n',
                    '    with open(image_file_path, "wb") as f:\n',
                    '        f.write(r.content)\n',
                    '\n',
                    'img = Image.open(image_file_path)\n',
                    'arr = np.asarray(img)  # doesn\'t create a copy of the array (read-only)\n',
                    '# arr = np.array(img)  # creates a copy of the array (read and write)'
                ]
                break
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print(f"Updated {file_path}")

if __name__ == "__main__":
    base = "c:/Users/nayef/Downloads/ultralytics/labs"
    update_notebook(os.path.join(base, "00_images.ipynb"))
    update_notebook(os.path.join(base, "exercises/00_images_exercises.ipynb"))
