# input() = mengambil inputan dari keyboard
# int() = fungsi untuk mengkonversi nilai ke integer

alpha = 0.8

# Langkah Pertama
s1 = int(input('Masukkan data aktual di hari ke 1 : '))
s2 = int(input('Masukkan data aktual di hari ke 2 : '))
rumus_s2 = alpha * s2 + (1 - alpha) * s1

s3 = int(input('Masukkan data aktual di hari ke 3 : '))
rumus_s3 = alpha * s3 + (1 - alpha) * rumus_s2

s4 = int(input('Masukkan data aktual di hari ke 4 : '))
rumus_s4 = alpha * s4 + (1 - alpha) * rumus_s3

s5 = int(input('Masukkan data aktual di hari ke 5 : '))
rumus_s5 = alpha * s5 + (1 - alpha) * rumus_s4

s6 = int(input('Masukkan data aktual di hari ke 6 : '))
rumus_s6 = alpha * s6 + (1 - alpha) * rumus_s5

# Langkah Kedua
ss1 = s1

ss2 = alpha * rumus_s2 + (1 - alpha) * ss1
ss3 = alpha * rumus_s3 + (1 - alpha) * ss2

ss4 = alpha * rumus_s4 + (1 - alpha) * ss3
ss5 = alpha * rumus_s5 + (1 - alpha) * ss4
ss6 = alpha * rumus_s6 + (1 - alpha) * ss5

# Langkah Ketiga
a1 = 2 * s1 - ss1
a2 = 2 * rumus_s2 - ss2
a3 = 2 * rumus_s3 - ss3
a4 = 2 * rumus_s4 - ss4
a5 = 2 * rumus_s5 - ss5
a6 = 2 * rumus_s6 - ss6

# Langkah Ke empat
b1 = alpha / (1 - alpha) * (s1 - ss1)
b2 = alpha / (1 - alpha) * (rumus_s2 - ss2)
b3 = alpha / (1 - alpha) * (rumus_s3 - ss3)
b4 = alpha / (1 - alpha) * (rumus_s4 - ss4)
b5 = alpha / (1 - alpha) * (rumus_s5 - ss5)
b6 = alpha / (1 - alpha) * (rumus_s6 - ss6)

# langkah ke lima
st = a6 + b6

print("Nilai Ramalan Hari ke-7 : " + str(st))