
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

text = "إيجابيات صحيحة"
reshaped = arabic_reshaper.reshape(text)
final = get_display(reshaped)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title(reshaped)
plt.xlabel("Reshaped Only")

plt.subplot(1, 2, 2)
plt.title(final)
plt.xlabel("Reshaped + Bidi")

plt.savefig('test_ar_versions.png')
print("Generated test_ar_versions.png")
