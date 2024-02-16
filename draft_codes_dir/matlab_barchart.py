import matplotlib.pyplot as plt
import numpy as np

lx = np.array(["A", "B", "C", "D"])
ly = np.array([2, 56, 23, 12])
plt.subplot(1, 2, 1)
plt.title("Letter plot")
plt.bar(lx, ly)

fx = np.array(["Apple", "Banana"])
fy = np.array([400, 500])
plt.subplot(1, 2, 2)
plt.title("Fruites")
plt.barh(fx, fy,color='hotpink',height=0.65)

plt.show()
