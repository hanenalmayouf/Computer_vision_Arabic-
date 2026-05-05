import json

target_file = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# إضافة خلية اختبار في القمة تماماً
test_cell = {
 "cell_type": "markdown",
 "metadata": {},
 "source": [
  "# [اختبار] إذا كنت ترى هذا النص فالتحديث يعمل بنجاح! ✅\n",
  "\n",
  "## [شرح ممتع] الحقيقة الرقمية للمصفوفات 🔢\n",
  "هذا هو الشرح الذي نتحدث عنه."
 ]
}

nb['cells'] = [test_cell] + nb['cells']

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("تمت إضافة خلية الاختبار في القمة!")
