import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

detailed_intro = """# 🖼️ كيف يرى الكمبيوتر صورنا؟ (المصفوفات الرقمية)

تخيل أنك تنظر إلى صورة "حصان" جميلة.. أنت ترى شعراً، عيوناً، وحوافر. لكن هل تعلم ماذا يرى الكمبيوتر؟ 🤖

بالنسبة للكمبيوتر، الصورة هي عبارة عن **فسيفساء عملاقة** مكونة من مربعات صغيرة جداً تسمى **بكسلات (Pixels)**. كل بكسل من هذه المربعات ليس له لون في نظر الكمبيوتر، بل له **رقم**!

### 🔢 كيف تتحول الألوان إلى أرقام؟
الكمبيوتر يحفظ شدة الضوء في كل بكسل برقم يتراوح بين **0** و **255**:
*   **الرقم 0:** يعني "ظلام تام" (لون أسود).
*   **الرقم 255:** يعني "نور ساطع" (لون أبيض).
*   **الأرقام بينهما:** هي درجات الرمادي المختلفة.

### 📐 المصفوفة (The Array)
عندما نضع هذه الأرقام في صفوف وأعمدة، نحصل على ما يسمى **المصفوفة (Array)**. فكر فيها كأنها جدول بيانات في Excel، حيث يمثل كل بكسل خلية في هذا الجدول.

**مثال بسيط:** إذا كانت لدينا صورة صغيرة جداً (3×3 بكسل) لشكل بسيط، قد يراها الكمبيوتر هكذا:

| 255 | 0 | 255 |
| :---: | :---: | :---: |
| 0 | 255 | 0 |
| 255 | 0 | 255 |

هذا الجدول هو "المصفوفة الرقمية" التي سنقوم باللعب بها وتعديلها في هذا المعمل!"""

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_cells = []
seen_intro = False

for cell in nb['cells']:
    source_text = "".join(cell['source'])
    
    # استبدال سكشن المقدمة بالشرح التفصيلي الجديد
    if ("كيف يرى الكمبيوتر" in source_text or "Images as N-Dimensional" in source_text) and not seen_intro:
        cell['source'] = [detailed_intro]
        seen_intro = True
        new_cells.append(cell)
        continue
    
    # تخطي أي تكرار للمقدمة قد يكون موجوداً
    if "كيف يرى الكمبيوتر" in source_text and seen_intro:
        continue

    new_cells.append(cell)

nb['cells'] = new_cells

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تمت إضافة الشرح التفصيلي للمقدمة بنجاح!")
