import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 12*x**2 + 36*x + 10

def f_prime(x):
    return 3*x**2 - 24*x + 36

def f_double_prime(x):
    return 6*x - 24

x = np.linspace(-2, 14, 500)
y = f(x)

titik_kritis = np.roots([3, -24, 36]) 
nilai_kritis = f(titik_kritis)

titik_infleksi = np.roots([6, -24]) 
nilai_infleksi = f(titik_infleksi)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="f(x) = x^3 - 12x^2 + 36x + 10", color="blue")

plt.scatter(titik_kritis, nilai_kritis, color="red", label="Titik Kritis")
for x_k, y_k in zip(titik_kritis, nilai_kritis):
    plt.text(x_k, y_k + 5, f"({x_k:.2f}, {y_k:.2f})", color="red")

plt.scatter(titik_infleksi, nilai_infleksi, color="green", label="Titik Infleksi")
for x_i, y_i in zip(titik_infleksi, nilai_infleksi):
    plt.text(x_i, y_i - 30, f"({x_i:.2f}, {y_i:.2f})", color="green")

plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Grafik dari f(x) = x^3 - 12x^2 + 36x + 10", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
