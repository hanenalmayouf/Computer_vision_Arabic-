
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
    repo_url = "https://colab.research.google.com/github/hanenalmayouf/Computer_vision_Arabic-/blob/main/labs/"
    
    index_html = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منهج الرؤية الحاسوبية - SDAIA</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #f0f4f8; margin: 0; padding: 0; color: #1C355E; }}
        header {{ background: linear-gradient(135deg, #1C355E, #00C9A7); color: white; padding: 4rem 1rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
        .container {{ max-width: 900px; margin: 2rem auto; padding: 1rem; }}
        h1 {{ margin: 0; font-size: 2.5rem; font-weight: 800; }}
        .module {{ background: white; border-radius: 20px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #eef2f7; }}
        .module h3 {{ margin: 0 0 0.5rem 0; color: #1C355E; font-size: 1.6rem; display: flex; align-items: center; gap: 10px; }}
        .module p {{ margin: 0 0 1.5rem 0; color: #546e7a; line-height: 1.6; font-size: 1rem; }}
        .link-group {{ display: flex; flex-direction: column; gap: 12px; }}
        .link-item {{ display: flex; align-items: center; gap: 12px; text-decoration: none; padding: 12px 20px; border-radius: 12px; transition: 0.3s; font-weight: 700; font-size: 0.95rem; }}
        .link-slides {{ background: #f1f5f9; color: #1C355E; }}
        .link-slides:hover {{ background: #e2e8f0; }}
        .link-lab {{ background: #e0f2f1; color: #00796b; }}
        .link-lab:hover {{ background: #b2dfdb; }}
        .badge {{ display: inline-block; padding: 4px 10px; border-radius: 10px; font-size: 0.75rem; background: #00C9A7; color: white; margin-bottom: 10px; }}
        .footer {{ text-align: center; padding: 3rem; color: #94a3b8; font-size: 0.85rem; }}
        img.logo {{ width: 130px; margin-bottom: 1.5rem; }}
    </style>
</head>
<body>
    <header>
        <img src="slides/slides_template/assets/sdaia.svg" alt="SDAIA" class="logo">
        <h1>منهج الرؤية الحاسوبية الاحترافي</h1>
        <p>فهرس المنهج: محاضرات ومعامل تطبيقية</p>
    </header>
    
    <div class="container">
        
        <!-- Module 0 -->
        <div class="module">
            <span class="badge">الوحدة التمهيدية</span>
            <h3>🖼️ أساسيات الصورة الرقمية</h3>
            <p>كيف يفهم الكمبيوتر الصور، البكسلات، القنوات اللونية، وأنظمة الإحداثيات.</p>
            <div class="link-group">
                <a href="slides/Image_Foundations.html" class="link-item link-slides">📂 عرض المحاضرة (Slides)</a>
                <a href="{repo_url}00_images.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل: الصور كمصفوفات متعددة الأبعاد</a>
            </div>
        </div>

        <!-- Module 1 -->
        <div class="module">
            <span class="badge">الجزء الأول</span>
            <h3>🚀 YOLO: المهام والاستدلال</h3>
            <p>اكتشف قدرات YOLO في الاكتشاف، التجزئة، التصنيف، وتقدير الوضعية.</p>
            <div class="link-group">
                <a href="slides/Ultralytics_Foundations_1_Tasks_Inference.html" class="link-item link-slides">📂 عرض المحاضرة (Slides)</a>
                <a href="{repo_url}01_tasks_inference_ar.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل: مهام واستدلال YOLO</a>
            </div>
        </div>

        <!-- Module 2 -->
        <div class="module">
            <span class="badge">الجزء الثاني</span>
            <h3>🔍 تطبيقات وحلول العالم الحقيقي</h3>
            <p>ما وراء الصناديق: تحليل المناطق، التتبع الحركي، والخرائط الحرارية للفيديو.</p>
            <div class="link-group">
                <a href="slides/Ultralytics_Foundations_2_Real_World_Use_Cases.html" class="link-item link-slides">📂 عرض المحاضرة (Slides)</a>
                <a href="{repo_url}02_solutions_expanded.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل: حلول برمجية واقعية</a>
            </div>
        </div>

        <!-- Module 2B -->
        <div class="module">
            <span class="badge">الجزء 2ب (إضافي)</span>
            <h3>🎥 هندسة الفيديو والتدفق</h3>
            <p>التعامل مع الكاميرات المتعددة، التزامن، وتقليل اختناق المعالج (CPU Bottlenecks).</p>
            <div class="link-group">
                <a href="slides/Ultralytics_Foundations_2_Real_World_Use_Cases.html" class="link-item link-slides">📂 عرض المحاضرة (نفس الوحدة 2)</a>
                <a href="{repo_url}02b_video_engineering.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل: هندسة الفيديو والبث غير المتزامن</a>
            </div>
        </div>

        <!-- Module 3 -->
        <div class="module">
            <span class="badge">الجزء الثالث</span>
            <h3>🛠️ تدريب النماذج المخصصة</h3>
            <p>تجهيز البيانات الخاصة، ضبط المعاملات الفائقة، وبدء دورات التدريب.</p>
            <div class="link-group">
                <a href="slides/Ultralytics_Foundations_3_Custom_Data_Training.html" class="link-item link-slides">📂 عرض المحاضرة (Slides)</a>
                <a href="{repo_url}03_custom_training.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل: التدريب المخصص على COCO8</a>
            </div>
        </div>

        <!-- Module 4 -->
        <div class="module">
            <span class="badge">الجزء الرابع</span>
            <h3>📊 التقييم والنشر</h3>
            <p>فهم مصفوفة الارتباك، IoU، الدقة، الاستدعاء، وتصدير النماذج للإنتاج.</p>
            <div class="link-group">
                <a href="slides/Ultralytics_Foundations_4_Evaluation_Deployment.html" class="link-item link-slides">📂 عرض المحاضرة (Slides)</a>
                <a href="{repo_url}04a_roi_evaluation.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل 4أ: التقييم الموجه بالعائد المادي (ROI)</a>
                <a href="{repo_url}04b_evaluation_technical.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل 4ب: المقاييس التقنية والتشخيص</a>
            </div>
        </div>

        <!-- Module 5 -->
        <div class="module">
            <span class="badge">الجزء الخامس</span>
            <h3>🤗 نظام HuggingFace للرؤية</h3>
            <p>استخدام SAM 3 للتجزئة، والبحث بالصور، ونماذج لغة الرؤية المتعددة.</p>
            <div class="link-group">
                <a href="slides/HuggingFace_CV_Part5.html" class="link-item link-slides">📂 عرض المحاضرة (Slides)</a>
                <a href="{repo_url}05_huggingface_cv_ar.ipynb" class="link-item link-lab" target="_blank">🧪 المعمل: بايثون لـ HuggingFace CV</a>
            </div>
        </div>

    </div>

    <div class="footer">
        © 2026 جميع الحقوق محفوظة لـ سدايا (SDAIA) <br>
        منهج الرؤية الحاسوبية المطور.
    </div>
</body>
</html>
"""
    # Write to the root docs folder
    docs_dir = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/docs'
    if not os.path.exists(docs_dir): os.makedirs(docs_dir)
    
    with open(os.path.join(docs_dir, 'index.html'), 'w') as f:
        f.write(index_html)
    
    print("Created structured index.html in docs/")

if __name__ == "__main__":
    process_files()
    create_index()
