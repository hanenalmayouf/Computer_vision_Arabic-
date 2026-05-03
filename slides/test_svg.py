
import matplotlib.pyplot as plt

plt.rcParams['svg.fonttype'] = 'none'
plt.figure(figsize=(5, 3))
plt.title("نتائج النموذج")
plt.xlabel("المحور الأفقي")
plt.savefig('test_svg_ar.svg')
print("Generated test_svg_ar.svg")
