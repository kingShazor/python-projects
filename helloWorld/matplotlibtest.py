import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label="Sinuskurve")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinuskurve")
plt.legend()
plt.show()

