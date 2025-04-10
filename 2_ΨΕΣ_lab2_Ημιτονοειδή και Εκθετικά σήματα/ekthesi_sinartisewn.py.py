import matplotlib
matplotlib.use('agg')  # Χρήση του backend χωρίς GUI
import numpy as np
import matplotlib.pyplot as plt

# Χρονικός άξονας
t = np.linspace(-3, 3, 1000)

# Ορισμός των εκθετικών συναρτήσεων
f1 = 0.5**(2 * t)
f2 = 2**(2 * t)
f3 = 0.5**(-2 * t)
f4 = 2**(-2 * t)

# Δημιουργία γραφημάτων σε 2x2 πλέγμα (subplot 2x2)
plt.figure(figsize=(10, 10))

# Επάνω αριστερά (f1)
plt.subplot(2, 2, 1)
plt.plot(t, f1, label='f(t) = 0.5^(2t)', color='blue')
plt.title('f(t) = 0.5^(2t)')
plt.xlabel('xronos (t)')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()

# Επάνω δεξιά (f2)
plt.subplot(2, 2, 2)
plt.plot(t, f2, label='f(t) = 2^(2t)', color='green')
plt.title('f(t) = 2^(2t)')
plt.xlabel('xronos (t)')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()

# Κάτω αριστερά (f3)
plt.subplot(2, 2, 3)
plt.plot(t, f3, label='f(t) = 0.5^(-2t)', color='red')
plt.title('f(t) = 0.5^(-2t)')
plt.xlabel('xronos (t)')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()

# Κάτω δεξιά (f4)
plt.subplot(2, 2, 4)
plt.plot(t, f4, label='f(t) = 2^(-2t)', color='purple')
plt.title('f(t) = 2^(-2t)')
plt.xlabel('xronos (t)')
plt.ylabel('f(t)')
plt.grid(True)
plt.legend()

# Αποθήκευση των γραφημάτων
plt.tight_layout()
plt.savefig("Erwtisi5_Ekthesi_sinartisewn.png")  # Αποθήκευση εικόνας
