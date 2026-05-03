
import os

def translate_plots_to_english(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    translations = {
        'نتائج النموذج مفرط الحساسية': 'Hyper-Sensitive Model Results',
        'إيجابيات صحيحة\\n(تم صيد السيارات)': 'True Positives\\n(Cars Detected)',
        'إيجابيات خاطئة\\n(فارغ ← "سيارة")': 'False Positives\\n(Empty -> "Car")',
        'سلبيات خاطئة\\n(سيارات ضاعت)': 'False Negatives\\n(Cars Missed)',
        'سلبيات صحيحة\\n(رفض صحيح)': 'True Negatives\\n(Correct Rejections)',
        'الضبط (Precision)': 'Precision',
        'الاستدعاء (Recall)': 'Recall',
        'مقياس F1': 'F1 Score',
        'الدقة المتوازنة': 'Balanced Accuracy',
        'الدرجة (%)': 'Score (%)',
        'عتبة الثقة (Confidence Threshold)': 'Confidence Threshold',
        'أفضل F1 عند conf=': 'Best F1 at conf=',
        'إجمالي الخسارة المالية ($)': 'Total Financial Loss ($)',
        'عتبة القرار (Decision Threshold)': 'Decision Threshold',
        'أقل خسارة عند': 'Min loss at',
        'الحقيقة (GT)': 'Ground Truth (GT)',
        'التوقع': 'Prediction',
        'قبل: غير متوازن': 'Before: Imbalanced',
        'بعد: عينات موزونة': 'After: Balanced Samples',
        'خسارة التدريب': 'Training Loss',
        'خسارة التحقق': 'Validation Loss',
        'الإفراط: تباعد الخسائر': 'Overfitting: Losses Diverging',
        'العصور (Epochs)': 'Epochs',
        'الخسارة (Loss)': 'Loss',
        'عدم الكفاية: هضبة مرتفعة': 'Underfitting: High Plateau',
        'صحي: تقارب الخسائر': 'Healthy: Losses Converging',
        'مرتفع جداً: تباعد / قفزات': 'Too High: Divergence / Jumps',
        'منخفض جداً: تقدم بطيء للغاية': 'Too Low: Very Slow Progress',
        'مناسب تماماً: سريع وصحي': 'Just Right: Fast & Healthy',
        'التحقق (بدون WD) — إفراط': 'Val (No WD) - Overfitting',
        'التحقق (مع WD) — مستقر': 'Val (With WD) - Stable',
        'أفضل نقطة (Checkpoint)': 'Best Checkpoint',
        'نافذة الصبر (Patience)': 'Patience Window',
        'إيجابيات صحيحة': 'True Positives',
        'إيجابيات خاطئة': 'False Positives',
        'سلبيات خاطئة': 'False Negatives',
        'سلبيات صحيحة': 'True Negatives',
        'الضبط': 'Precision',
        'الاستدعاء': 'Recall',
        'إيقاف التدريب': 'Early Stopping',
        'توقع 1 (TP, ثقة=0.91)': 'Pred 1 (TP, conf=0.91)',
        'توقع 2\\n(FP, ثقة=0.74)': 'Pred 2\\n(FP, conf=0.74)',
        'ماذا تحتاج؟': 'What do you need?',
        'قص / عزل / تحديد': 'Segment / Cut / Isolate',
        'البحث / ترتيب\\nالصور': 'Search / Rank\\nImages',
        'فهم / قراءة /\\nإجابة أسئلة': 'VLM / VQA /\\nReasoning',
        'استعلام نصي': 'Text Query',
        'استعلام بصري': 'Visual Query',
        'عربي + لغات': 'Arabic + Multi-lingual',
        'سريع': 'Fast',
        'توقع': 'Prediction',
        'الدرجة': 'Score',
        'أفضل F1': 'Best F1',
        'منطقة الربح': 'Profit Zone',
        'منطقة الخسارة': 'Loss Zone'
    }

    for ar, en in translations.items():
        content = content.replace(f"'{ar}'", f"'{en}'")
        content = content.replace(f'"{ar}"', f'"{en}"')

    with open(filepath, 'w') as f:
        f.write(content)

translate_plots_to_english('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
translate_plots_to_english('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
