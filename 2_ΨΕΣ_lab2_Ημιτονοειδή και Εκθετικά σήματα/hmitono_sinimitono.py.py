import matplotlib
matplotlib.use('agg')  # Χρήση του backend χωρίς GUI
import numpy as np
import matplotlib.pyplot as plt

# Χρονικός άξονας
t = np.linspace(0, 1, 1000)

# (i) Ημίτονο
A1, f1, phi1 = 2, 2, 0
y1 = A1 * np.sin(2 * np.pi * f1 * t + np.deg2rad(phi1))

# (ii) Συνημίτονο
A2, f2, phi2 = np.sqrt(3), 5, 45
y2 = A2 * np.cos(2 * np.pi * f2 * t + np.deg2rad(phi2))

# (iii) Συνημίτονο από ΑΜ
A3, f3, phi3 = 3, 1, np.pi / 7
y3 = A3 * np.cos(2 * np.pi * f3 * t + phi3)

# Δημιουργία και αποθήκευση διαγραμμάτων
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, y1, label='Ημίτονο (i)', color='blue')
plt.title('Ημίτονο (A=2, f=2Hz, φ=0°)')
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, y2, label='Συνημίτονο (ii)', color='green')
plt.title('Συνημίτονο (A=√3, f=5Hz, φ=45°)')
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, y3, label='Συνημίτονο (iii)', color='red')
plt.title('Συνημίτονο από ΑΜ (A=3, f=1Hz, φ=π/7)')
plt.grid()
plt.legend()

plt.tight_layout()
plt.savefig("Erwtisi1_HmitonoSimmisono_backend_agg.png")  # Αποθήκευση διαγράμματος
