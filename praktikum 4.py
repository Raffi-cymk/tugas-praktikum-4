# Program untuk menambahkan data ke dalam sebuah list dengan perhitungan nilai akhir

data_list = []

while True:
    # Meminta data dari pengguna
    nama = input("Masukkan nama: ")
    
    # Input dan validasi nilai Tugas
    try:
        tugas = float(input("Masukkan nilai Tugas (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka.")
        continue
    
    # Input dan validasi nilai UTS
    try:
        uts = float(input("Masukkan nilai UTS (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka.")
        continue
    
    # Input dan validasi nilai UAS
    try:
        uas = float(input("Masukkan nilai UAS (0-100): "))
    except ValueError:
        print("Nilai harus berupa angka.")
        continue
    
    # Menghitung nilai akhir
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    
    # Menambahkan data ke dalam list
    data_list.append({
        'Nama': nama,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    tambah_data = input("Tambah data lagi? (y/t): ").lower()
    if tambah_data == 't':
        break
    elif tambah_data != 'y':
        print("Input tidak valid, anggap 'y' untuk melanjutkan.")

# Menampilkan daftar data
print("\nDaftar Data:")
print("==========================================")
print("No | Nama        | Tugas | UTS | UAS | Nilai Akhir")
print("==========================================")
for i, data in enumerate(data_list, start=1):
    print(f"{i:2} | {data['Nama']:10} | {data['Tugas']:5} | {data['UTS']:4} | {data['UAS']:4} | {data['Nilai Akhir']:11.2f}")
print("==========================================")
