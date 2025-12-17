start = 50
count_zero = 0

commands = []
print("Paste perintah (contoh: L68, R1000), ketik 'END' untuk selesai:")

while True:
    line = input()
    if line == "END":
        break
    if line.strip():
        commands.append(line.strip())

print("\n--- Memulai Pemrosesan ---")

for cmd in commands:
    arah = cmd[0].upper()     
    langkah = int(cmd[1:])     
    
    tambahan_nol = 0 

    if arah == 'R':
        tambahan_nol = (start + langkah) // 100
        
        start = (start + langkah) % 100

    elif arah == 'L':
        jarak_ke_nol = start if start != 0 else 100
        
        if langkah >= jarak_ke_nol:
            sisa_langkah = langkah - jarak_ke_nol
            tambahan_nol = 1 + (sisa_langkah // 100)
        else:
            tambahan_nol = 0
            
        start = (start - langkah) % 100

    count_zero += tambahan_nol
    print(f"→ {cmd} : Posisi jadi {start}, Nemu nol {tambahan_nol} kali.")

print("--------------------------")
print("Posisi Akhir Dial:", start)
print("Password (Total 0):", count_zero)