import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# النص الجديد المنسق
new_intro_text = """⭐⭐⭐ للتعامل مع الصور برمجياً، نمر بخطوتين بسيطتين:
1. 📥 **التحميل:** نستخدم `Image.open()` لفتح ملف الصورة.
2. 🔢 **التحويل:** نستخدم `np.asarray()` لتحويل تلك الصورة إلى أرقام (مصفوفة) لكي يتمكن الكمبيوتر من معالجتها."""

# استهداف الخلية رقم 5 تحديداً لأنها هي المقصودة في المقدمة
if len(nb['cells']) > 5:
    nb['cells'][5]['source'] = [new_intro_text]
    print("تم تحديث مقدمة التحميل في الخلية رقم 5 بنجاح!")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تم الإصلاح الدقيق.")
