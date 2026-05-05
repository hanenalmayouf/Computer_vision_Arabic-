import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

target_fragment = "لقراءة صورة، نحتاج لاستخدام الدالة"
new_content = """للتعامل مع الصور برمجياً، نمر بخطوتين بسيطتين:
1. 📥 **التحميل:** نستخدم `Image.open()` لفتح ملف الصورة.
2. 🔢 **التحويل:** نستخدم `np.asarray()` لتحويل تلك الصورة إلى أرقام (مصفوفة) لكي يتمكن الكمبيوتر من معالجتها."""

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_text = "".join(cell.get('source', []))
        if target_fragment in source_text:
            cell['source'] = [new_content]
            break

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تم تحسين صياغة فقرة التحميل بنجاح!")
