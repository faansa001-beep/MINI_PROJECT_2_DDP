# NAMA: NURUL SHAFA AZIZAH #
# NIM: 2509116112 #
# PRODI: SISTEM INFORMASI #

users = {
    "admin": {"password": "123", "role": "Manager"},
    "Andi": {"password": "456", "role": "Karyawan"}
}

# Data Travel Log (id: {tujuan, tanggal, catatan})
dokumen_log = {
    "647201234567890009872":{
        "nama": "Andi Setiabudi",
        "jenis": "KTP",
        "berlaku_hingga": "2026-12-20"
    },
    "910987654321":{
        "nama": "Rina Astuti",
        "jenis": "SIM A",
        "berlaku_hingga": "2030-2-21"
    },
    "6472098765432121002":{
        "nama": "Indra Subekti",
        "jenis": "KTP",
        "berlaku_hingga": "2033-5-15"
    }
}

# ==== Fungsi CRUD ====
def read_log():
    if not dokumen_log:
        print("Belum ada dokumen.")
    else:
        print("\n=== dokumen Log ===")
        for id_log, data in dokumen_log.items():
            print(f"{id_log} nama: {data['nama']}, "
                  f"{data['nama']}, berlaku_hingga: {data['berlaku_hingga']}")

def create_log():
    try:
        id_log = max(dokumen_log.keys(), default=0) + 1
        nama = input("Masukkan nama dokumen: ")
        tanggal = input("Masukkan tanggal berlaku (YYYY-MM-DD): ")
        berlaku_hingga = input("Masukkan tanggal: ")
        dokumen_log[id_log] = {"nama": nama, "tanggal": tanggal, "berlaku_hingga": berlaku_hingga}
        print("Catatan perjalanan berhasil ditambahkan!")
    except Exception as e:
        print("Terjadi kesalahan:", e)

def update_log():
    try:
        read_log()
        id_log = int(input("Masukkan yang ingin diupdate: "))
        if id_log in dokumen_log:
            nama = input("Masukkan nama baru: ")
            tanggal = input("Masukkan tanggal baru (YYYY-MM-DD): ")
            berlaku_hingga = input("Masukkan berlaku_hingga baru: ")
            dokumen_log[id_log] = {"nama": nama, "tanggal": tanggal, "berlaku_hingga": berlaku_hingga}
            print("Catatan dokumen berhasil diupdate!")
        else:
            print("data tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")

def delete_log():
    try:
        read_log()
        id_log = int(input("Masukkan dokumen yg mau dihapus: "))
        if id_log in dokumen_log:
            del dokumen_log[id_log]
            print("dokumen berhasil dihapus!")
        else:
            print(" dokumen tidak ditemukan!")
    except ValueError:
        print("Input harus berupa angka!")

# ==== Fungsi Menu ====
def menu_manager():
    while True:
        print("\n=== MENU MANAGER (Dokumen Log) ===")
        print("1. Lihat dokumen Log")
        print("2. Tambah dokumen Log")
        print("3. Update dokumen Log")
        print("4. Hapus dokumen Log")
        print("5. keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_log()
        elif pilihan == "2":
            create_log()
        elif pilihan == "3":
            update_log()
        elif pilihan == "4":
            delete_log()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")

def menu_karyawan():
    while True:
        print("\n=== MENU KARYAWAN (dokumen log) ===")
        print("1. Lihat dokumen Log")
        print("2. keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_log()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")

# ==== Fungsi Login ====
def login():
    print("=== LOGIN SISTEM DOKUMEN LOG ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil! Selamat datang, {username} ({users[username]['role']})")
        return users[username]["role"]
    else:
        print("Username atau password salah!")
        return None

# ==== Main Program ====
while True:
    role = login()
    if role == "Manager":
        menu_manager()
    elif role == "Karyawan":
        menu_karyawan()
