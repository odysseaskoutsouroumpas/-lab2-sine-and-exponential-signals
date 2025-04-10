import matplotlib
matplotlib.use('agg')  # Χρήση του backend χωρίς GUI
import numpy as np
import matplotlib.pyplot as plt

# Χρονικός άξονας
t = np.linspace(0, 1, 1000)

# (i) x1(t) = 3 sin(5t + π/4)
x1 = 3 * np.sin(5 * t + np.pi / 4)

# (ii) x2(t) = 3 sin(5t + π/2)
x2 = 3 * np.sin(5 * t + np.pi / 2)

# (iii) x3(t) = 3 sin(9t + π/2)
x3 = 3 * np.sin(9 * t + np.pi / 2)

# (iv) x4(t) = 3 cos(5t)
x4 = 3 * np.cos(5 * t)

# Δημιουργία γραφημάτων
plt.figure(figsize=(10, 8))

# (i) x1(t)
plt.subplot(4, 1, 1)
plt.plot(t, x1, label='x1(t) = 3*sin(5t + π/4)', color='blue')
plt.title('x1(t) = 3*sin(5t + π/4)')
plt.grid()
plt.legend()

# (ii) x2(t)
plt.subplot(4, 1, 2)
plt.plot(t, x2, label='x2(t) = 3*sin(5t + π/2)', color='green')
plt.title('x2(t) = 3*sin(5t + π/2)')
plt.grid()
plt.legend()

# (iii) x3(t)
plt.subplot(4, 1, 3)
plt.plot(t, x3, label='x3(t) = 3*sin(9t + π/2)', color='red')
plt.title('x3(t) = 3*sin(9t + π/2)')
plt.grid()
plt.legend()

# (iv) x4(t)
plt.subplot(4, 1, 4)
plt.plot(t, x4, label='x4(t) = 3*cos(5t)', color='purple')
plt.title('x4(t) = 3*cos(5t)')
plt.grid()
plt.legend()

# Αποθήκευση γραφημάτων σε εικόνα
plt.tight_layout()
plt.savefig("Erwtisi2_Synartiseis.png")  # Αποθήκευση εικόνας
