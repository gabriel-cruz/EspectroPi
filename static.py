import matplotlib.pyplot as plt
import numpy as np
from constants import STANDARD_FILE

x, y = np.loadtxt(STANDARD_FILE, delimiter = '/', unpack=True)
plt.xlim(200, 850)
plt.ylim(0, 40000)

plt.plot(x, y)
plt.show()
