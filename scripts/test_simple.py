import json

# إنشاء ملف جديد تماماً وبسيط جداً للتجربة
test_nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🎓 تجربة الشرح الممتع 🔢\n",
    "إذا كنت ترى هذا السطر والإيموجي، فهذا يعني أن التحديث يعمل!\n",
    "\n",
    "### 🖼️ الحقيقة الرقمية:\n",
    "هنا نضع الشرح الممتع الذي نتحدث عنه."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

file_path = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/Final_Fun_Lab.ipynb'
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(test_nb, f, ensure_ascii=False, indent=1)

print("تم إنشاء ملف التجربة!")
