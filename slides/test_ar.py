
import matplotlib.pyplot as plt
import matplotlib.axes
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np

def fix_ar(text):
    if not isinstance(text, str): return text
    if any("\u0600" <= c <= "\u06FF" for c in text):
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)
    return text

# Set font
plt.rcParams['font.family'] = 'Arial'

# Test
text = "إيجابيات صحيحة"
fixed = fix_ar(text)
print(f"Original: {text}")
print(f"Fixed: {fixed}")

fig, ax = plt.subplots()
ax.set_title(text) # Should be broken if not patched
plt.savefig('test_plot.png')
print("Saved test_plot.png")
