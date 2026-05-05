import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# الشرح الكامل والمنسق
explanation_text = """# 🖼️ كيف يرى الكمبيوتر صورنا؟ (المصفوفات الرقمية)

تخيل أنك تنظر إلى صورة حصان جميلة.. أنت ترى شعراً وعيوناً، لكن الكمبيوتر يرى **فسيفساء عملاقة** من المربعات الصغيرة تسمى **بكسلات (Pixels)**. 

كل بكسل له **رقم** يمثل شدة الضوء:
*   **0** يعني أسود (مطفأ).
*   **255** يعني أبيض (سوبر مشرق).

المصفوفة (Array) هي مجرد جدول لهذه الأرقام، تماماً مثل جداول Excel.

**مثال لجدول 3×3 بكسل:**

| 255 | 0 | 255 |
| :---: | :---: | :---: |
| 0 | 255 | 0 |
| 255 | 0 | 255 |"""

new_cells = []
inserted = False

for cell in nb['cells']:
    source_text = "".join(cell.get('source', []))
    
    # حذف أي نسخة قديمة غير مكتملة من الشرح
    if 'كيف يرى الكمبيوتر' in source_text:
        continue
        
    # إدخال الشرح الجديد قبل أول خلية كود
    if cell['cell_type'] == 'code' and not inserted:
        new_cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [explanation_text]
        })
        inserted = True
    
    new_cells.append(cell)

nb['cells'] = new_cells

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تم إصلاح الشرح بنجاح!")
