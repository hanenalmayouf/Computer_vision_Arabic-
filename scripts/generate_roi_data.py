import numpy as np

def generate_roi_stats():
    np.random.seed(42)  # For consistency
    total_defects = 500
    total_good = 9500
    
    # Generate fake confidence scores
    # Good boards are very tightly clustered at the low end
    # Defects are more spread out, making the choice of threshold critical
    scores_defects = np.random.normal(0.55, 0.20, total_defects)
    scores_good = np.random.normal(0.10, 0.03, total_good)
    
    # Clip to [0, 1]
    scores_defects = np.clip(scores_defects, 0.01, 0.99)
    scores_good = np.clip(scores_good, 0.01, 0.99)
    
    thresholds = np.linspace(0.01, 0.99, 100)
    
    results = []
    for t in thresholds:
        tp = np.sum(scores_defects >= t)
        fn = total_defects - tp
        fp = np.sum(scores_good >= t)
        tn = total_good - fp
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / total_defects
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        loss = (fn * 500) + (fp * 25)
        results.append((t, tp, fn, fp, tn, f1, loss))
    
    # Find Option A: Max F1
    results_sorted_f1 = sorted(results, key=lambda x: x[5], reverse=True)
    best_f1_item = results_sorted_f1[0]
    
    # Find Option B: Min Loss (Max ROI)
    results_sorted_loss = sorted(results, key=lambda x: x[6])
    best_roi_item = results_sorted_loss[0]
    
    print("--- Option A (Max F1) ---")
    t, tp, fn, fp, tn, f1, loss = best_f1_item
    print(f"Threshold: {t:.2f}, FN: {fn}, FP: {fp}, F1: {f1:.3f}, Loss: ${loss:,.0f}")
    
    print("\n--- Option B (Best ROI) ---")
    t, tp, fn, fp, tn, f1, loss = best_roi_item
    print(f"Threshold: {t:.2f}, FN: {fn}, FP: {fp}, F1: {f1:.3f}, Loss: ${loss:,.0f}")

generate_roi_stats()
