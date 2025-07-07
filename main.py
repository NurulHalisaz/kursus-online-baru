from data import kursus_list, admin_akun, user_list

def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username == admin_akun["username"] and password == admin_akun["password"]:
        print("Login sebagai Admin")
        menu_admin()
    else:
        for user in user_list:
            if user["username"] == username and user["password"] == password:
                print(f"Login sebagai Pengguna {username}")
                menu_user(username)
                return
        print("Login gagal. Username atau password salah.")

def daftar_user():
    print("\n=== PENDAFTARAN USER ===")
    username = input("Buat username: ")
    password = input("Buat password: ")
    user_list.append({"username": username, "password": password})
    print("Pendaftaran berhasil. Silakan login.")

def tampilkan_semua_kursus():
    print("\n== Semua Kursus ==")
    for i, k in enumerate(kursus_list, 1):
        print(f"{i}. {k['nama']} - {k['tingkat']} - {k['deskripsi']} - Rp{k['harga']}")

def tambah_kursus():
    print("\n== Tambah Kursus Baru ==")
    nama = input("Nama kursus: ")
    tingkat = input("Tingkat (Beginner / Intermediate / Advanced): ")
    deskripsi = input("Deskripsi: ")
    try:
        harga = int(input("Harga (Rp): "))
        kursus_list.append({"nama": nama, "tingkat": tingkat, "deskripsi": deskripsi, "harga": harga})
        print("Kursus berhasil ditambahkan.")
    except ValueError:
        print("Harga harus berupa angka.")

def hapus_kursus():
    tampilkan_semua_kursus()
    try:
        idx = int(input("Masukkan nomor kursus yang ingin dihapus: "))
        if 1 <= idx <= len(kursus_list):
            hapus = kursus_list.pop(idx - 1)
            print(f"Kursus '{hapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def daftar_ke_kursus(username):
    tampilkan_semua_kursus()
    try:
        pilihan = int(input("Pilih nomor kursus untuk mendaftar: "))
        if 1 <= pilihan <= len(kursus_list):
            kursus = kursus_list[pilihan - 1]
            print(f"{username} berhasil mendaftar ke '{kursus['nama']}' dengan biaya Rp{kursus['harga']}")
        else:
            print("Nomor tidak tersedia.")
    except ValueError:
        print("Input tidak valid.")

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat semua kursus")
        print("2. Tambah kursus")
        print("3. Hapus kursus")
        print("4. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_semua_kursus()
        elif pilihan == "2":
            tambah_kursus()
        elif pilihan == "3":
            hapus_kursus()
        elif pilihan == "4":
            print("Logout dari Admin.")
            break
        else:
            print("Pilihan tidak valid.")

def menu_user(username):
    while True:
        print(f"\n=== MENU USER ({username}) ===")
        print("1. Lihat semua kursus")
        print("2. Daftar ke kursus")
        print("3. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_semua_kursus()
        elif pilihan == "2":
            daftar_ke_kursus(username)
        elif pilihan == "3":
            print("Logout dari Pengguna.")
            break
        else:
            print("Pilihan tidak valid.")

def menu_utama():
    while True:
        print("\n=== SISTEM KURSUS ONLINE ===")
        print("1. Login")
        print("2. Daftar sebagai user")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            login()
        elif pilihan == "2":
            daftar_user()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu_utama()
