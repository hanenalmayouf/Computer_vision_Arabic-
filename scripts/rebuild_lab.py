import json

# القالب الكامل للمعمل مع الشروحات الممتعة
nb_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🎓 معمل رؤية الكمبيوتر: التعامل مع الصور\n\n",
    "> [!IMPORTANT]\n",
    "> **ملاحظة للطلاب:** اضغط على **File** ثم **Save a copy in Drive** للبدء.\n\n",
    "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hanenalmayouf/Computer_vision_Arabic-/blob/main/labs/00_images.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "GtQxh2HqP1za"
   },
   "source": [
    "# 🖼️ كيف يرى الكمبيوتر صورنا؟ (المصفوفات الرقمية)\n\nتخيل أنك تنظر إلى صورة \"حصان\" جميلة.. أنت ترى شعراً، عيوناً، وحوافر. لكن هل تعلم ماذا يرى الكمبيوتر؟ 🤖\n\nبالنسبة للكمبيوتر، الصورة هي عبارة عن **فسيفساء عملاقة** مكونة من مربعات صغيرة جداً تسمى **بكسلات (Pixels)**. كل بكسل من هذه المربعات ليس له لون في نظر الكمبيوتر، بل له **رقم**!\n\n### 🔢 كيف تتحول الألوان إلى أرقام؟\nالكمبيوتر يحفظ شدة الضوء في كل بكسل برقم يتراوح بين **0** و **255**:\n*   **الرقم 0:** يعني \"ظلام تام\" (لون أسود).\n*   **الرقم 255:** يعني \"نور ساطع\" (لون أبيض).\n*   **الأرقام بينهما:** هي درجات الرمادي المختلفة.\n\n### 📐 المصفوفة (The Array)\nعندما نضع هذه الأرقام في صفوف وأعمدة، نحصل على ما يسمى **المصفوفة (Array)**. فكر فيها كأنها جدول بيانات في Excel، حيث يمثل كل بكسل خلية في هذا الجدول.\n\n**مثال بسيط:** إذا كانت لدينا صورة صغيرة جداً (3×3 بكسل) لشكل بسيط، قد يراها الكمبيوتر هكذا:\n\n| 255 | 0 | 255 |\n| :---: | :---: | :---: |\n| 0 | 255 | 0 |\n| 255 | 0 | 255 |\n\nهذا الجدول هو \"المصفوفة الرقمية\" التي سنقوم باللعب بها وتعديلها في هذا المعمل!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {
    "id": "HT-izJ_SP1zd"
   },
   "outputs": [],
   "source": [
    "import sys\n",
    "if 'google.colab' in sys.modules:\n",
    "    %pip install numpy Pillow\n",
    "else:\n",
    "    !pip install numpy Pillow\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {
    "id": "aHRQGOBKP1zf"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from PIL import Image\n",
    "import os\n",
    "import requests\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ksdfH9goP1zg"
   },
   "source": [
    "## 1. قراءة وعرض الصور 📥\nأول خطوة هي إدخال الصورة إلى لغة البرمجة. فكر فيها كأننا نأخذ صورة فوتوغرافية ونضعها داخل \"ماسح ضوئي\" برمجياً ليفهمها الكمبيوتر."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

file_path = '/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/labs/00_images.ipynb'
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb_content, f, ensure_ascii=False, indent=1)

print("تمت إعادة بناء المعمل بالكامل بنجاح!")
