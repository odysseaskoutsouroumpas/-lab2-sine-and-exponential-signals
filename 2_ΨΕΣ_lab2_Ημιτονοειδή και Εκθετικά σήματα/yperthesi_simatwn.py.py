import matplotlib
matplotlib.use('agg')  # Χρήση του backend χωρίς GUI
import numpy as np
import matplotlib.pyplot as plt

# Χρονικός άξονας
t = np.linspace(0, 1, 1000)

# Ορισμός των ημιτονοειδών σημάτων
x1 = np.sin(18 * t)
x2 = np.sin(20 * t)
x3 = np.sin(2 * t)

# Υπερθέσεις
X12 = x1 + x2
X23 = x2 + x3
X4 = 4 * x3 * x2

# Δημιουργία γραφημάτων
plt.figure(figsize=(10, 12))

# (i) X12 = x1 + x2
plt.subplot(4, 1, 1)
plt.plot(t, X12, label='X12 = x1 + x2', color='blue')
plt.title('X12 = sin(18t) + sin(20t)')
plt.grid()
plt.legend()

# (ii) X23 = x2 + x3
plt.subplot(4, 1, 2)
plt.plot(t, X23, label='X23 = x2 + x3', color='green')
plt.title('X23 = sin(20t) + sin(2t)')
plt.grid()
plt.legend()

# (iii) X4 = 4 * x3 * x2
plt.subplot(4, 1, 3)
plt.plot(t, X4, label='X4 = 4 * x3 * x2', color='red')
plt.title('X4 = 4 * sin(2t) * sin(20t)')
plt.grid()
plt.legend()

# Υπολογισμός περιόδων για κάθε σήμα
T_x1 = 2 * np.pi / 18  # Περίοδος για x1(t)
T_x2 = 2 * np.pi / 20  # Περίοδος για x2(t)
T_x3 = 2 * np.pi / 2   # Περίοδος για x3(t)

# Αποθήκευση γραφημάτων σε εικόνα
plt.tight_layout()
plt.savefig("Erwtisi4_Yperthesi_Sigmaton.png")  # Αποθήκευση εικόνας
