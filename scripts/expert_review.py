import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# خريطة التحديثات الاحترافية (Expert Enrichments)
expert_updates = {
    "We can crop part of the image": """بإمكاننا قص أي جزء من الصورة كما نشاء عبر عملية تسمى "التقطيع" (Slicing). 
فكر فيها كأنك تحدد منطقة معينة في جدول بيانات لتنسخها.""",

    "try to understand what this line does": """# هنا نستخدم سحر بايثون لدمج العناوين مع الأرقام في قاموس (Dictionary) ليسهل قراءتها!""",

    "نحتاج للقسمة أولاً لتحويل نوع البيانات": """لاحظ أننا نقسم على 3 لنأخذ "المتوسط الحسابي" للألوان. 
> [!TIP]
> **لماذا نحول النوع لـ float؟** لأن جمع ثلاثة أرقام قد يتجاوز الرقم 255، مما يسبب "فيضان" (Overflow) في الذاكرة وتظهر الألوان بشكل خاطئ!""",

    "يُنصح باستخدام أوزان مختلفة": """## 👁️ خدعة العين البشرية!
هل تعلم أن عينك ترى اللون الأخضر بوضوح أكثر من الأزرق؟ لذلك، في رؤية الكمبيوتر، نعطي "وزناً" أكبر للون الأخضر (58%) عند التحويل للأبيض والأسود لتبدو الصورة طبيعية أكثر لعينك.""",

    "البكسلات ذات الإضاءة العالية هي التي تنتمي للحصان": "لنقم بتجربة مثيرة: سنعزل الحصان عن الخلفية باستخدام 'شرط منطقي'. أي بكسل إضاءته أعلى من درجة معينة سنعتبره هو هدفنا."
}

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_text = "".join(cell.get('source', []))
        for key, enrichment in expert_updates.items():
            if key in source_text:
                cell['source'] = [enrichment]
                break
    elif cell['cell_type'] == 'code':
        # تحديث التعليقات داخل الكود لتكون عربية ومفيدة
        source_lines = cell.get('source', [])
        new_source = []
        for line in source_lines:
            if "try to understand what this line does" in line:
                new_source.append(line.replace("# try to understand what this line does", expert_updates["try to understand what this line does"]))
            else:
                new_source.append(line)
        cell['source'] = new_source

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تمت المراجعة الفنية والتربوية الشاملة بنجاح!")
