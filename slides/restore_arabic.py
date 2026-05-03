
import os

def restore_arabic_labels(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    translations = {
        'Hyper-Sensitive Model Results': 'نتائج النموذج مفرط الحساسية',
        'True Positives\\n(Cars Detected)': 'إيجابيات صحيحة\\n(تم صيد السيارات)',
        'False Positives\\n(Empty -> "Car")': 'إيجابيات خاطئة\\n(فارغ ← "سيارة")',
        'False Negatives\\n(Cars Missed)': 'سلبيات خاطئة\\n(سيارات ضاعت)',
        'True Negatives\\n(Correct Rejections)': 'سلبيات صحيحة\\n(رفض صحيح)',
        'Precision': 'الضبط',
        'Recall': 'الاستدعاء',
        'F1 Score': 'مقياس F1',
        'Balanced Accuracy': 'الدقة المتوازنة',
        'Score (%)': 'الدرجة (%)',
        'Confidence Threshold': 'عتبة الثقة',
        'Best F1 at conf=': 'أفضل F1 عند conf=',
        'Total Financial Loss ($)': 'إجمالي الخسارة المالية ($)',
        'Decision Threshold': 'عتبة القرار',
        'Min loss at': 'أقل خسارة عند',
        'Ground Truth (GT)': 'الحقيقة (GT)',
        'Prediction': 'التوقع',
        'Before: Imbalanced': 'قبل: غير متوازن',
        'After: Balanced Samples': 'بعد: عينات موزونة',
        'Training Loss': 'خسارة التدريب',
        'Validation Loss': 'خسارة التحقق',
        'Overfitting: Losses Diverging': 'الإفراط: تباعد الخسائر',
        'Epochs': 'العصور (Epochs)',
        'Loss': 'الخسارة',
        'Underfitting: High Plateau': 'عدم الكفاية: هضبة مرتفعة',
        'Healthy: Losses Converging': 'صحي: تقارب الخسائر',
        'Too High: Divergence / Jumps': 'مرتفع جداً: تباعد / قفزات',
        'Too Low: Very Slow Progress': 'منخفض جداً: تقدم بطيء للغاية',
        'Just Right: Fast & Healthy': 'مناسب تماماً: سريع وصحي',
        'Val (No WD) - Overfitting': 'التحقق (بدون WD) — إفراط',
        'Val (With WD) - Stable': 'التحقق (مع WD) — مستقر',
        'Best Checkpoint': 'أفضل نقطة (Checkpoint)',
        'Patience Window': 'نافذة الصبر (Patience)',
        'Early Stopping': 'إيقاف التدريب',
        'Pred 1 (TP, conf=0.91)': 'توقع 1 (TP, ثقة=0.91)',
        'Pred 2\\n(FP, conf=0.74)': 'توقع 2\\n(FP, ثقة=0.74)',
        'What do you need?': 'ماذا تحتاج؟',
        'Segment / Cut / Isolate': 'قص / عزل / تحديد',
        'Search / Rank\\nImages': 'البحث / ترتيب\\nالصور',
        'VLM / VQA /\\nReasoning': 'فهم / قراءة /\\nإجابة أسئلة',
        'Text Query': 'استعلام نصي',
        'Visual Query': 'استعلام بصري',
        'Arabic + Multi-lingual': 'عربي + لغات',
        'Fast': 'سريع',
        'Score': 'الدرجة',
        'Best F1': 'أفضل F1',
        'Profit Zone': 'منطقة الربح',
        'Loss Zone': 'منطقة الخسارة'
    }

    for en, ar in translations.items():
        content = content.replace(f"'{en}'", f"'{ar}'")
        content = content.replace(f'"{en}"', f'"{ar}"')

    with open(filepath, 'w') as f:
        f.write(content)

restore_arabic_labels('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/Ultralytics_Foundations_4_Evaluation_Deployment.qmd')
restore_arabic_labels('/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/slides/HuggingFace_CV_Part5.qmd')
