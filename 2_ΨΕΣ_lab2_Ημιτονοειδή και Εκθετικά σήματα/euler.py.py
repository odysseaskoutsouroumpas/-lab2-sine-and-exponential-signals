import matplotlib
matplotlib.use('agg')  # Χρήση του backend χωρίς GUI
import numpy as np
import matplotlib.pyplot as plt

# Δημιουργία του θ (από 1 έως 2π με 100 σημεία)
theta = np.linspace(1, 2 * np.pi, 100)

# Υπολογισμός του e^(jθ)
e_jtheta = np.exp(1j * theta)

# Υπολογισμός των τιμών για cos(θ), sin(θ), μέτρο και φάση
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
magnitude = np.abs(e_jtheta)
phase = np.angle(e_jtheta)

# Δημιουργία γραφημάτων
plt.figure(figsize=(10, 8))

# (i) cos(θ)
plt.subplot(2, 2, 1)
plt.plot(theta, cos_theta, label='cos(θ)', color='blue')
plt.title('cos(θ)')
plt.xlabel('θ')
plt.ylabel('cos(θ)')
plt.grid(True)
plt.legend()

# (ii) sin(θ)
plt.subplot(2, 2, 2)
plt.plot(theta, sin_theta, label='sin(θ)', color='green')
plt.title('sin(θ)')
plt.xlabel('θ')
plt.ylabel('sin(θ)')
plt.grid(True)
plt.legend()

# (iii) Φάση e^(jθ)
plt.subplot(2, 2, 3)
plt.plot(theta, magnitude, label='|e^(jθ)|', color='red')
plt.title('metro e^(jθ)')
plt.xlabel('θ')
plt.ylabel('|e^(jθ)|')
plt.grid(True)
plt.legend()

# (iv) Φάση e^(jθ)
plt.subplot(2, 2, 4)
plt.plot(theta, phase, label=' fasi e^(jθ)', color='purple')
plt.title('fasi e^(jθ)')
plt.xlabel('θ')
plt.ylabel('fasi')
plt.grid(True)
plt.legend()

# Αποθήκευση των γραφημάτων σε αρχείο εικόνας
plt.tight_layout()
plt.savefig("Erwtisi6_Eulerpng")
