import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('lampada.txt', delimiter = '/', unpack=True)
plt.xlim(200, 850)
plt.ylim(0, 40000)

plt.plot(x, y)
plt.show()
