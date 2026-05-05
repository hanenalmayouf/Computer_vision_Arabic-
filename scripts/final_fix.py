import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

# مصفوفة التحديث القوية بناءً على محتوى الخلية أو موقعها
with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# الشروحات الممتعة
enrichment_content = {
    "intro_title": "# 🖼️ كيف يرى الكمبيوتر صورنا؟ (المصفوفات الرقمية)",
    "intro_text": "تخيل أن الكمبيوتر لا يملك عينين مثلك! بالنسبة له، كل صورة هي مجرد **جدول كبير من الأرقام**. في هذه الرحلة، سنتحكم في هذه الأرقام لنغير ملامح الصور.",
    "section_1": "## 1. قراءة وعرض الصور 📥\nأول خطوة هي إدخال الصورة إلى لغة البرمجة. فكر فيها كأننا نأخذ صورة فوتوغرافية ونضعها داخل \"ماسح ضوئي\" برمجياً ليفهمها الكمبيوتر.",
    "section_2": "## 2. الحقيقة الرقمية: الصور هي مصفوفات! 🔢\nهنا تبدأ المتعة! عندما نقول \"مصفوفة\"، فنحن نقصد \"جدول أرقام\". \n\n> [!TIP]\n> **فكر فيها كذا:** الصورة الملونة هي عبارة عن 3 جداول فوق بعضها (أحمر، أخضر، أزرق). كل مربع في الجدول يسمى **بكسل (Pixel)**.",
    "section_3": "## 3. صيد البكسلات: الوصول لأي نقطة وتغييرها 🎯\nكل بكسل في الصورة له \"عنوان\" مثل إحداثيات الخريطة (رقم الصف، رقم العمود). إذا عرفت العنوان، يمكنك تغيير لون هذه النقطة!",
    "section_4": "## 4. فن القص واللصق ✂️\nتماماً كما تفعل في برامج تعديل الصور، يمكنك قص \"شريحة\" من أرقام المصفوفة ولصقها في مكان آخر.",
    "section_7": "## 7. تفكيك الصورة: قنوات الألوان (RGB) 🌈\nأي صورة ملونة هي في الأصل مزيج من 3 ألوان أساسية. سنقوم هنا بـ \"تشريح\" الصورة لنرى الطبقات الملونة.",
    "section_9": "## 9. التمييز الذكي (Thresholding) 🔍\nهذه الخطوة هي بداية \"الذكاء\". نحن نخبر الكمبيوتر: \"أي رقم أكبر من 150 اعتبره (حصان) وأي رقم أصغر اعتبره (خلفية)\"."
}

clean_cells = []
# الهيدر الموحد
colab_header = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# 🎓 معمل رؤية الكمبيوتر: التعامل مع الصور\n\n",
        "> [!IMPORTANT]\n",
        "> **ملاحظة للطلاب:** اضغط على **File** ثم **Save a copy in Drive** للبدء.\n\n",
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hanenalmayouf/Computer_vision_Arabic-/blob/main/labs/00_images.ipynb)"
    ]
}
clean_cells.append(colab_header)

# استبدال الخلايا بشكل جراحي
for cell in nb['cells']:
    source_text = "".join(cell['source'])
    if "معمل رؤية الكمبيوتر" in source_text or "Google Colab" in source_text:
        continue
    
    if cell['cell_type'] == 'markdown':
        # استبدال العناوين والفقرات بناءً على الكلمات المفتاحية القديمة أو العربية
        if "التعامل مع الصور كمصفوفات" in source_text or "Images as N-Dimensional" in source_text:
            cell['source'] = [enrichment_content["intro_title"]]
        elif "سنتعلم كيفية التعامل" in source_text or "in this notebook, we will" in source_text:
            cell['source'] = [enrichment_content["intro_text"]]
        elif "1. قراءة وعرض الصور" in source_text or "Read and Show" in source_text:
            cell['source'] = [enrichment_content["section_1"]]
        elif "2. الصور هي مصفوفات" in source_text or "Images are Arrays" in source_text:
            cell['source'] = [enrichment_content["section_2"]]
        elif "3. الوصول للبكسل" in source_text or "Pixel Access" in source_text:
            cell['source'] = [enrichment_content["section_3"]]
        elif "4. القص واللصق" in source_text or "Crop and Paste" in source_text:
            cell['source'] = [enrichment_content["section_4"]]
        elif "7. قنوات الألوان" in source_text or "Color Channels" in source_text:
            cell['source'] = [enrichment_content["section_7"]]
        elif "9. فصل العناصر" in source_text or "Thresholding" in source_text:
            cell['source'] = [enrichment_content["section_9"]]

    clean_cells.append(cell)

nb['cells'] = clean_cells

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تم التحديث النهائي والشامل للمعمل!")
