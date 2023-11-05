print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
print("------------------------------------------------------")

def hitung_tahun(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def hitung_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return False
    if bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            jumlah_hari = 29
        else:
            jumlah_hari = 28
    elif bulan in [4, 6, 9, 11]:
        jumlah_hari = 30
    else:
        jumlah_hari = 31
    
    return jumlah_hari

bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun (misalnya 2023): "))

jumlah_hari = hitung_bulan(tahun, bulan)

if jumlah_hari:
    print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari")
else:
    print("Input bulan atau tahun tidak valid.")
