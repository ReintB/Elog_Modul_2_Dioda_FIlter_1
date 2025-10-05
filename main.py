import matplotlib.pyplot as plt

# ===============================
# Data dari tabel (RL variabel)
# ===============================
RL = [1500, 1000, 500, 200, 100]

Vout_pengukuran_RL = [6.26, 6.236, 6.192, 6.114, 6.009]
Vout_perhitungan_RL = [7.778, 7.767, 7.735, 7.640, 7.488]

Vripple_pengukuran_RL = [0.024398, 0.048159, 0.075327, 0.196483, 0.413361]
Vripple_perhitungan_RL = [0.012, 0.018, 0.037, 0.092, 0.180]

# ===============================
# Data dari tabel (C variabel)
# ===============================
C = [1000, 47, 10, 5]

Vout_pengukuran_C = [6.009, 4.356, 3.535, 3.435]
Vout_perhitungan_C = [7.488, 3.435, 1.509, 0.836]

Vripple_pengukuran_C = [0.394585, 3.97, 5.935, 6.201]
Vripple_perhitungan_C = [0.180, 2.116, 3.630, 4.022]

# ===============================
# Plot 1: RL vs Voutput
# ===============================
plt.figure(figsize=(8,5))
plt.plot(RL, Vout_pengukuran_RL, marker='o', label="Vout DC Pengukuran")
plt.plot(RL, Vout_perhitungan_RL, marker='s', label="Vout DC Perhitungan")
plt.xlabel("RL (Ohm)")
plt.ylabel("V Output (DC) [V]")
plt.title("RL vs V Output (DC)")
plt.legend()
plt.grid(True)
plt.savefig("rev_grafik1_RL_vs_Voutput.png", dpi=300)
plt.close()

# ===============================
# Plot 2: RL vs Vripple
# ===============================
plt.figure(figsize=(8,5))
plt.plot(RL, Vripple_pengukuran_RL, marker='o', label="Vripple Pengukuran")
plt.plot(RL, Vripple_perhitungan_RL, marker='s', label="Vripple Perhitungan")
plt.xlabel("RL (Ohm)")
plt.ylabel("V Ripple (rms) [V]")
plt.title("RL vs Vripple (rms)")
plt.legend()
plt.grid(True)
plt.savefig("rev_grafik2_RL_vs_Vripple.png", dpi=300)
plt.close()

# ===============================
# Plot 3: C vs Voutput
# ===============================
plt.figure(figsize=(8,5))
plt.plot(C, Vout_pengukuran_C, marker='o', label="Vout DC Pengukuran")
plt.plot(C, Vout_perhitungan_C, marker='s', label="Vout DC Perhitungan")
plt.xlabel("C (uF)")
plt.ylabel("V Output (DC) [V]")
plt.title("C vs V Output (DC)")
plt.legend()
plt.grid(True)
plt.xscale("log")  # gunakan skala log untuk C
plt.savefig("rev_grafik3_C_vs_Voutput.png", dpi=300)
plt.close()

# ===============================
# Plot 4: C vs Vripple
# ===============================
plt.figure(figsize=(8,5))
plt.plot(C, Vripple_pengukuran_C, marker='o', label="Vripple Pengukuran")
plt.plot(C, Vripple_perhitungan_C, marker='s', label="Vripple Perhitungan")
plt.xlabel("C (uF)")
plt.ylabel("V Ripple (rms) [V]")
plt.title("C vs Vripple (rms)")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.savefig("rev_grafik4_C_vs_Vripple.png", dpi=300)
plt.close()

print("Semua grafik revisi berhasil disimpan sebagai PNG:")
print("- rev_grafik1_RL_vs_Voutput.png")
print("- rev_grafik2_RL_vs_Vripple.png")
print("- rev_grafik3_C_vs_Voutput.png")
print("- rev_grafik4_C_vs_Vripple.png")