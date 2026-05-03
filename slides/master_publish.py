
import os
import re

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
                # Check if already patched to avoid duplicates
                if "matplotlib_inline.backend_inline" not in parts[2]:
                    content = "---" + parts[1] + "---" + SILENT_PATCH + parts[2]
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Patched {filename}")

def create_index():
    index_html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منهج الرؤية الحاسوبية - SDAIA</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #f0f4f8; margin: 0; padding: 0; color: #1C355E; }
        header { background: linear-gradient(135deg, #1C355E, #00C9A7); color: white; padding: 3rem 1rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .container { max-width: 1000px; margin: 2rem auto; padding: 1rem; }
        h1 { margin: 0; font-size: 2.5rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
        .card { background: white; border-radius: 15px; padding: 1.5rem; transition: 0.3s; text-decoration: none; color: inherit; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #eee; display: flex; flex-direction: column; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); border-color: #00C9A7; }
        .card h3 { margin: 0 0 0.5rem 0; color: #1C355E; }
        .card p { margin: 0; font-size: 0.9rem; color: #666; line-height: 1.4; }
        .badge { display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; margin-bottom: 1rem; background: #e0f2f1; color: #00796b; width: fit-content; }
        .footer { text-align: center; padding: 2rem; color: #888; font-size: 0.8rem; }
        img.logo { width: 120px; margin-bottom: 1rem; }
    </style>
</head>
<body>
    <header>
        <img src="slides/slides_template/assets/sdaia.svg" alt="SDAIA" class="logo">
        <h1>منهج الرؤية الحاسوبية الاحترافي</h1>
        <p>مسار تطوير الأنظمة باستخدام YOLO و HuggingFace</p>
    </header>
    
    <div class="container">
        <div class="grid">
            <a href="slides/Image_Foundations.html" class="card">
                <span class="badge">الأساسيات</span>
                <h3>0. أساسيات الصورة الرقمية</h3>
                <p>كيف يفهم الكمبيوتر البيكسلات والألوان والقنوات.</p>
            </a>
            <a href="slides/Ultralytics_Foundations_1_Tasks_Inference.html" class="card">
                <span class="badge">YOLO Part 1</span>
                <h3>1. المهام والاستدلال</h3>
                <p>البداية مع YOLO: الاكتشاف، التصنيف، والتجزئة.</p>
            </a>
            <a href="slides/Ultralytics_Foundations_2_Real_World_Use_Cases.html" class="card">
                <span class="badge">YOLO Part 2</span>
                <h3>2. تطبيقات العالم الحقيقي</h3>
                <p>سيناريوهات عملية لاستخدام الرؤية الحاسوبية في الصناعة.</p>
            </a>
            <a href="slides/Ultralytics_Foundations_3_Custom_Data_Training.html" class="card">
                <span class="badge">YOLO Part 3</span>
                <h3>3. تدريب النماذج المخصصة</h3>
                <p>كيف تدرب YOLO على بياناتك الخاصة وحل مشاكلك الفريدة.</p>
            </a>
            <a href="slides/Ultralytics_Foundations_4_Evaluation_Deployment.html" class="card">
                <span class="badge">YOLO Part 4</span>
                <h3>4. التقييم والنشر</h3>
                <p>قياس الدقة ونقل النموذج لمرحلة الإنتاج (Deployment).</p>
            </a>
            <a href="slides/HuggingFace_CV_Part5.html" class="card">
                <span class="badge">HuggingFace</span>
                <h3>5. نظام HuggingFace للرؤية</h3>
                <p>استكشاف CLIP و SAM ونماذج لغة الرؤية المتطورة.</p>
            </a>
        </div>
    </div>

    <div class="footer">
        © 2026 جميع الحقوق محفوظة لـ سدايا (SDAIA)
    </div>
</body>
</html>
"""
    # Write to the root docs folder
    docs_dir = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/docs'
    if not os.path.exists(docs_dir): os.makedirs(docs_dir)
    
    with open(os.path.join(docs_dir, 'index.html'), 'w') as f:
        f.write(index_html)
    print("Created index.html in docs/")

if __name__ == "__main__":
    process_files()
    create_index()
