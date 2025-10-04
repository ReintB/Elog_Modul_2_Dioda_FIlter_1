import matplotlib.pyplot as plt

RL = [1500, 1000, 500, 200, 100]

Vout_pengukuran_RL = [6.26, 6.236, 6.192, 6.114, 6.009]
Vout_perhitungan_RL = [8.825, 8.783, 8.677, 8.463, 8.150]

Vripple_pengukuran_RL = [24.398, 48.159, 75.327, 196.483, 413.361]
Vripple_perhitungan_RL = [0.014, 0.021, 0.042, 0.102, 0.196]

C = [1000, 47, 10, 5]

Vout_pengukuran_C = [6.009, 4.0, 3.535, 3.435]
Vout_perhitungan_C = [8.158, 3.265, 0.967, 0.52]

Vripple_pengukuran_C = [394.585, 3.97, 5.935, 6.201]
Vripple_perhitungan_C = [0.196, 1.671, 2.326, 2.501]

# Plot 1: RL vs Voutput
plt.figure(figsize=(8,5))
plt.plot(RL, Vout_pengukuran_RL, marker='o', label="Vout DC Pengukuran")
plt.plot(RL, Vout_perhitungan_RL, marker='s', label="Vout DC Perhitungan")
plt.xlabel("RL (Ohm)")
plt.ylabel("V Output (DC)")
plt.title("RL vs V Output DC")
plt.legend()
plt.grid(True)
plt.savefig("grafik1_RL_vs_Voutput.png", dpi=300)
plt.close()

# Plot 2: RL vs Vripple
plt.figure(figsize=(8,5))
plt.plot(RL, Vripple_pengukuran_RL, marker='o', label="Vripple Pengukuran")
plt.plot(RL, Vripple_perhitungan_RL, marker='s', label="Vripple Perhitungan")
plt.xlabel("RL (Ohm)")
plt.ylabel("V Ripple")
plt.title("RL vs Vripple")
plt.legend()
plt.grid(True)
plt.savefig("grafik2_RL_vs_Vripple.png", dpi=300)
plt.close()

# Plot 3: C vs Voutput
plt.figure(figsize=(8,5))
plt.plot(C, Vout_pengukuran_C, marker='o', label="Vout DC Pengukuran")
plt.plot(C, Vout_perhitungan_C, marker='s', label="Vout DC Perhitungan")
plt.xlabel("C (uF)")
plt.ylabel("V Output (DC)")
plt.title("C vs V Output DC")
plt.legend()
plt.grid(True)
plt.savefig("grafik3_C_vs_Voutput.png", dpi=300)
plt.close()

# Plot 4: C vs Vripple
plt.figure(figsize=(8,5))
plt.plot(C, Vripple_pengukuran_C, marker='o', label="Vripple Pengukuran")
plt.plot(C, Vripple_perhitungan_C, marker='s', label="Vripple Perhitungan")
plt.xlabel("C (uF)")
plt.ylabel("V Ripple")
plt.title("C vs Vripple")
plt.legend()
plt.grid(True)
plt.savefig("grafik4_C_vs_Vripple.png", dpi=300)
plt.close()

print("Semua grafik berhasil disimpan sebagai PNG")