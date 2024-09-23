import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig2, ax2 = plt.subplots()
ax2.plot(x, y)
plt.show()
x = np.linspace(0, 3 * np.pi, 300)
y = np.sin(x)

fig2, ax2 = plt.subplots()
ax2.plot(x, y)
plt.show()

