import matplotlib
matplotlib.use('agg')  # Χρήση του backend χωρίς GUI
import numpy as np
import matplotlib.pyplot as plt

# Χρονικός άξονας
t = np.linspace(0, 1, 1000)

# Ορισμός του σήματος x(t) = 2 * (4 * cos(88t) + cos(8t))
x_t = 2 * (4 * np.cos(88 * t) + np.cos(8 * t))

# Δημιουργία γραφήματος
plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label=r'$x(t) = 2 \cdot (4 \cos(88t) + \cos(8t))$', color='blue')
plt.title(r'$x(t) = 2 \cdot (4 \cos(88t) + \cos(8t))$')
plt.xlabel('xronos (t)')
plt.ylabel('timi simatos x(t)')
plt.grid()
plt.legend()

# Αποθήκευση γραφήματος σε εικόνα
plt.tight_layout()
plt.savefig("Erwtisi3_Tetragoniko_Sigma.png")  # Αποθήκευση εικόνας
