
import os
import re
import shutil

# List of all files to process
slides_files = [
    'Ultralytics_Foundations_1_Tasks_Inference.qmd',
    'Ultralytics_Foundations_2_Real_World_Use_Cases.qmd',
    'Ultralytics_Foundations_3_Custom_Data_Training.qmd',
    'Ultralytics_Foundations_4_Evaluation_Deployment.qmd',
    'HuggingFace_CV_Part5.qmd',
    'Image_Foundations.qmd'
]

BASE_DIR = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides'
DOCS_DIR = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/docs'

SILENT_PATCH = r"""
```{python}
#| echo: false
#| output: false
import matplotlib.pyplot as plt
try:
    import matplotlib_inline.backend_inline
    matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
except:
    pass
plt.rcParams['svg.fonttype'] = 'none'

def fix_ar(text):
    return text
```
"""

def process_files():
    for filename in slides_files:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} - not found.")
            continue
            
        with open(filepath, 'r') as f:
            content = f.read()
            
        # 1. Remove any old patches or technical printouts
        content = re.sub(r'print\("SVG-Native.*?\)\n', '', content)
        content = re.sub(r'print\("Arabic SVG support.*?\)\n', '', content)
        
        # 2. Inject Silent Patch after YAML
        if "---" in content:
            parts = content.split("---", 2)
            if len(parts) >= 3:
                if "matplotlib_inline.backend_inline" not in parts[2]:
                    content = "---" + parts[1] + "---" + SILENT_PATCH + parts[2]
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched {filename}")

def deploy_assets():
    docs_slides_dir = os.path.join(DOCS_DIR, 'slides')
    if not os.path.exists(docs_slides_dir):
        os.makedirs(docs_slides_dir)
    
    # Copy all .html files and their associated _files directories
    for item in os.listdir(BASE_DIR):
        src_path = os.path.join(BASE_DIR, item)
        dst_path = os.path.join(docs_slides_dir, item)
        
        if item.endswith('.html'):
            shutil.copy2(src_path, dst_path)
            
        if item.endswith('_files'):
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)
            
        if item in ['assets', 'slides_template', 'outputs']:
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(src_path, dst_path)
            
        if item.endswith('.png') or item.endswith('.jpg') or item.endswith('.svg'):
             shutil.copy2(src_path, dst_path)

    print("Fully deployed slides, dependencies, and assets to docs/slides/")

def create_index():
    repo_url = "https://colab.research.google.com/github/hanenalmayouf/Computer_vision_Arabic-/blob/main/labs/"
    
    index_html = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SDAIA | منهج الرؤية الحاسوبية</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {{ --primary: #1e293b; --accent: #38bdf8; --bg: #f8fafc; --text: #0f172a; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--bg); margin: 0; padding: 0; color: var(--text); line-height: 1.6; }}
        header {{ background: var(--primary); color: white; padding: 4rem 1rem; text-align: center; border-bottom: 4px solid var(--accent); }}
        .container {{ max-width: 800px; margin: 2rem auto; padding: 1rem; }}
        h1 {{ margin: 0; font-size: 2.5rem; font-weight: 800; color: var(--accent); }}
        header p {{ font-size: 1.1rem; opacity: 0.8; margin-top: 0.5rem; }}
        .module {{ background: white; border-radius: 16px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; }}
        .module h3 {{ margin: 0 0 0.5rem 0; color: var(--primary); font-size: 1.5rem; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }}
        .module p {{ margin: 0.5rem 0 1.5rem 0; color: #64748b; font-size: 1rem; }}
        .link-list {{ display: flex; flex-direction: column; gap: 10px; }}
        .link-item {{ display: flex; align-items: center; gap: 10px; text-decoration: none; padding: 12px 18px; border-radius: 10px; font-weight: 600; transition: 0.2s; }}
        .link-slides {{ background: #f1f5f9; color: var(--primary); }}
        .link-slides:hover {{ background: #e2e8f0; }}
        .link-lab {{ background: #f0f9ff; color: #0369a1; }}
        .link-lab:hover {{ background: #e0f2fe; }}
        .footer {{ text-align: center; padding: 3rem; color: #94a3b8; font-size: 0.85rem; }}
        img.logo {{ width: 140px; margin-bottom: 1.5rem; }}
    </style>
</head>
<body>
    <header>
        <img src="slides/slides_template/assets/sdaia.svg" alt="SDAIA" class="logo">
        <h1>Ultralytics & Computer Vision For Developers</h1>
        <p>فهرس الدورة التعليمية المطور - سدايا</p>
    </header>
    
    <div class="container">
        
        <div class="module">
            <h3>🖼️ Preparatory Module</h3>
            <p>How computers perceive images: pixels, color channels, and coordinate systems.</p>
            <div class="link-list">
                <a href="slides/Image_Foundations.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}00_images.ipynb" class="link-item link-lab" target="_blank">Lab: Images as N-Dimensional Arrays</a>
            </div>
        </div>

        <div class="module">
            <h3>🚀 Part 1: Tasks & Inference</h3>
            <p>Discover what YOLO can do out of the box: Detection, Segmentation, Classification, and Pose.</p>
            <div class="link-list">
                <a href="slides/Ultralytics_Foundations_1_Tasks_Inference.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}01_tasks_inference_ar.ipynb" class="link-item link-lab" target="_blank">Lab: YOLO Tasks & Inference</a>
            </div>
        </div>

        <div class="module">
            <h3>🔍 Part 2: Use Cases & Solutions</h3>
            <p>Beyond bounding boxes: actionable insights, region analytics, and heatmaps.</p>
            <div class="link-list">
                <a href="slides/Ultralytics_Foundations_2_Real_World_Use_Cases.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}02_solutions_expanded.ipynb" class="link-item link-lab" target="_blank">Lab: Real-World Solutions</a>
            </div>
        </div>

        <div class="module">
            <h3>🎥 Part 2B: Video Engineering (BONUS)</h3>
            <p>Handling RTSP, Concurrency, Threading, and real-time streaming.</p>
            <div class="link-list">
                <a href="slides/Ultralytics_Foundations_2_Real_World_Use_Cases.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}02b_video_engineering.ipynb" class="link-item link-lab" target="_blank">BONUS Lab: Async Video Streaming</a>
            </div>
        </div>

        <div class="module">
            <h3>🛠️ Part 3: Custom Data & Training</h3>
            <p>Teaching the model your custom data: fine-tuning on COCO8.</p>
            <div class="link-list">
                <a href="slides/Ultralytics_Foundations_3_Custom_Data_Training.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}03_custom_training.ipynb" class="link-item link-lab" target="_blank">Lab: Custom Training</a>
            </div>
        </div>

        <div class="module">
            <h3>📊 Part 4: Evaluation & Deployment</h3>
            <p>Understanding metrics (mAP, IoU, ROI) and exporting for production.</p>
            <div class="link-list">
                <a href="slides/Ultralytics_Foundations_4_Evaluation_Deployment.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}04a_roi_evaluation.ipynb" class="link-item link-lab" target="_blank">Lab 4A: ROI-Driven Evaluation</a>
                <a href="{repo_url}04b_evaluation_technical.ipynb" class="link-item link-lab" target="_blank">Lab 4B: Technical Metrics & Diagnosis</a>
            </div>
        </div>

        <div class="module">
            <h3>🤗 Part 5: HuggingFace for CV</h3>
            <p>Expanding your toolkit: SAM 3, visual embeddings, and Vision LLMs.</p>
            <div class="link-list">
                <a href="slides/HuggingFace_CV_Part5.html" class="link-item link-slides">Presentation Slides</a>
                <a href="{repo_url}05_huggingface_cv_ar.ipynb" class="link-item link-lab" target="_blank">Lab 5: HuggingFace for CV</a>
            </div>
        </div>

    </div>

    <div class="footer">
        © 2026 SDAIA - All rights reserved.
    </div>
</body>
</html>
"""
    if not os.path.exists(DOCS_DIR): os.makedirs(DOCS_DIR)
    with open(os.path.join(DOCS_DIR, 'index.html'), 'w') as f:
        f.write(index_html)
    # Also write to root index.html to be absolutely sure
    root_index = os.path.join('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/', 'index.html')
    with open(root_index, 'w') as f:
        # For root index, slides are in docs/slides/
        f.write(index_html.replace('href="slides/', 'href="docs/slides/'))

    print("Created index.html in docs/ and root.")

if __name__ == "__main__":
    process_files()
    deploy_assets()
    create_index()
