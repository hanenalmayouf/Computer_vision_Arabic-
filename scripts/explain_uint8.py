import json

import os

# الحصول على المسار النسبي للملف
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'labs', '00_images.ipynb')

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_uint8_explanation = """### 🧐 ماذا يعني `uint8`؟ (سر الأرقام في عالم الصور)

عندما يتعامل الكمبيوتر مع الصور، فإنه يحتاج لذكاء في توفير المساحة. لهذا نستخدم نوع بيانات يسمى **`uint8`**. دعونا نفكك هذا الاسم العجيب:

1. **حرف الـ `u` (اختصار لـ Unsigned):**
   * تعني "بدون إشارة" (+ أو -).
   * **الفرق بينها وبين الأرقام العادية:** الأرقام "العادية" (Signed) يمكن أن تكون سالبة (مثل -5). أما **Unsigned** فهي تبدأ دائماً من **الصفر وصعوداً**. 
   * (فكر فيها: هل سبق ورأيت لوناً قيمته "سالب 10"؟ بالطبع لا! لذلك لا نحتاج للإشارة السالبة في الصور).

2. **رقم `8` (تعني 8-bit):**
   * هذا هو "حجم الصندوق". في عالم الكمبيوتر، الصندوق الذي حجمه 8-بت يتسع لـ **256** احتمال فقط.
   * لذلك، تبدأ الأرقام من **0** (أسود تماماً) وتنتهي عند **255** (أبيض ساطع).

**بالمختصر:** الـ `uint8` هو نوع بيانات "اقتصادي" ومثالي للصور؛ لأنه يعطينا 256 درجة من اللون دون أن يستهلك مساحة تخزين ضخمة في الذاكرة."""

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_text = "".join(cell.get('source', []))
        if "كما نلاحظ، نوع البيانات هو `uint8`" in source_text or "unsigned 8-bit integer" in source_text:
            cell['source'] = [new_uint8_explanation]
            break

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
