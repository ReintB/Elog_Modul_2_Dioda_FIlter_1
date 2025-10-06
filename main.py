import matplotlib.pyplot as plt

# ===============================
# Data dari tabel (RL variabel)
# ===============================
RL = [1500, 1000, 500, 200, 100]

Vout_pengukuran_RL = [6.250, 6.221, 6.217, 6.014, 5.819]
Vout_perhitungan_RL = [7.67867036, 7.668049793, 7.636363636, 7.542857143, 7.392]

Vripple_pengukuran_RL = [0.277980, 0.41498, 0.85731, 0.207758, 0.393508]
Vripple_perhitungan_RL = [0.01231467333, 0.01844646088, 0.03674047168, 0.09072647087, 0.1778238829]

# ===============================
# Data dari tabel (C variabel)
# ===============================
C = [1000, 47, 10, 5]  # mikro Farad

Vout_pengukuran_C = [5.824, 2.224, 0.323442, 0.05659]
Vout_perhitungan_C = [7.699999679, 7.699993174, 7.699967917, 7.699935834]

Vripple_pengukuran_C = [0.385832, 4.02, 3.929, 6.185]
Vripple_perhitungan_C = [0.000001852332036, 0.00000511835345, 0.000002405626122, 0.00004811225243]

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
plt.savefig("new_grafik1_RL_vs_Voutput.png", dpi=300)
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
plt.savefig("new_grafik2_RL_vs_Vripple.png", dpi=300)
plt.close()

# ===============================
# Plot 3: C vs Voutput
# ===============================
plt.figure(figsize=(8,5))
plt.plot(C, Vout_pengukuran_C, marker='o', label="Vout DC Pengukuran")
plt.plot(C, Vout_perhitungan_C, marker='s', label="Vout DC Perhitungan")
plt.xlabel("C (µF)")
plt.ylabel("V Output (DC) [V]")
plt.title("C vs V Output (DC)")
plt.legend()
plt.grid(True)
plt.xscale("log")  # gunakan skala log untuk C
plt.savefig("new_grafik3_C_vs_Voutput.png", dpi=300)
plt.close()

# ===============================
# Plot 4: C vs Vripple
# ===============================
plt.figure(figsize=(8,5))
plt.plot(C, Vripple_pengukuran_C, marker='o', label="Vripple Pengukuran")
plt.plot(C, Vripple_perhitungan_C, marker='s', label="Vripple Perhitungan")
plt.xlabel("C (µF)")
plt.ylabel("V Ripple (rms) [V]")
plt.title("C vs Vripple (rms)")
plt.legend()
plt.grid(True)
plt.xscale("log")
plt.savefig("new_grafik4_C_vs_Vripple.png", dpi=300)
plt.close()

print("Semua grafik baru berhasil disimpan sebagai PNG:")
print("- new_grafik1_RL_vs_Voutput.png")
print("- new_grafik2_RL_vs_Vripple.png")
print("- new_grafik3_C_vs_Voutput.png")
print("- new_grafik4_C_vs_Vripple.png")