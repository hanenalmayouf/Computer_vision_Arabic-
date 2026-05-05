import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# نستخدم نصاً قصيراً جداً للبحث لضمان المطابقة
target_fragment = "لقراءة صورة"
new_content = """⭐⭐⭐ للتعامل مع الصور برمجياً، نمر بخطوتين بسيطتين:
1. 📥 **التحميل:** نستخدم `Image.open()` لفتح ملف الصورة.
2. 🔢 **التحويل:** نستخدم `np.asarray()` لتحويل تلك الصورة إلى أرقام (مصفوفة) لكي يتمكن الكمبيوتر من معالجتها."""

changed = False
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source_text = "".join(cell.get('source', []))
        if target_fragment in source_text:
            cell['source'] = [new_content]
            print(f"تم تغيير الخلية رقم {i}")
            changed = True

if not changed:
    print("تحذير: لم يتم العثور على الفقرة المستهدفة! سأحاول البحث عن جزء آخر من النص.")
    # محاولة ثانية بنص مختلف قليلاً
    target_fragment = "Image.open"
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            source_text = "".join(cell.get('source', []))
            if target_fragment in source_text and "np.asarray" in source_text:
                cell['source'] = [new_content]
                print(f"تم تغيير الخلية رقم {i} (محاولة ثانية)")
                changed = True

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("انتهى السكربت من العمل.")
