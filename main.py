import os
import shutil
import getpass
import sys
from API import API as api
from colors import bcolors
from prettytable import PrettyTable

class LibraryApp:
    """LibraryApp administration"""
    def __init__(self) -> None:
        os.system("cls")
        self.is_login = False
        self.size_terminal = shutil.get_terminal_size().columns
        api.create_db("User.json", [{"username": "admin", "password": "admin", "nik": "1111111111111111", "nama": "admin", "alamat": "admin"}])
        api.create_db("Book.json", [])
        input(f"Tekan {bcolors.OKBLUE}enter{bcolors.ENDC} untuk melanjutkan login")
        self.header()
        self.login_menu()

    def header(self):
        """header every page must have"""
        os.system("cls")
        print(".--.           .---.        .-.".center(self.size_terminal))
        print("   .---|--|   .-.     | A |  .---. |~|    .--.".center(self.size_terminal))
        print("    .--|===|Ch|---|_|--.__| S |--|:::| |~|-==-|==|---.".center(self.size_terminal))
        print("      |%%|NT2|oc|===| |~~|%%| C |--|   |_|~|CATS|  |___|-.".center(self.size_terminal))
        print("      |  |   |ah|===| |==|  | I |  |:::|=| |    |GB|---|=|".center(self.size_terminal))
        print("      |  |   |ol|   |_|__|  | I |__|   | | |    |  |___| |".center(self.size_terminal))
        print("      |~~|===|--|===|~|~~|%%|~~~|--|:::|=|~|----|==|---|=|".center(self.size_terminal))
        print("      ^--^---'--^---^-^--^--^---'--^---^-^-^-==-^--^---^-'".center(self.size_terminal))
        print("")
        print(" Selamat datang di perpustakaan ".center(self.size_terminal, "*"))
        print("*"*self.size_terminal)

    def login_validation(self, username, password):
        user = api.get_user(username)
        result = {}
      
        if len(user) == 0:
            result["status"] = False
            result["detail"] = "username tidak ditemukan"
            return result

        user = user[0]

        if password != user["password"]:
            result["status"] = False
            result["detail"] = "password tidak sesuai"
            return result

        result["status"] = True
        result["detail"] = "berhasil login"

        return result

    def login_menu(self):
        is_password_correct = False
        count_incorrect = 0
        username = ""
     
        while ((not is_password_correct) and (count_incorrect <= 2)):
            username = input("Username: ")
            password = getpass.getpass("Password: ")

            result = self.login_validation(username, password)
            print(result["detail"])
            is_password_correct = result["status"]
            count_incorrect += 1

        if is_password_correct:
            self.is_login = True
            return self.dashboard_page(username)

        return sys.exit()

    def cetak_pengguna(self, username):
        user = list(api.get_user(username))
        user = user[0]
        print(f"selamat datang, {user['username']}".rjust(self.size_terminal))

    def dashboard_page(self, username):
        os.system("cls")
        total_books = api.get_total_book()
        total_users = api.get_total_user()
        if self.is_login:
            self.header()
            user = list(api.get_user(username))
            user = user[0]
            print(f"selamat datang, {user['username']}".rjust(self.size_terminal))
            print(f"{bcolors.HEADER}INFORMASI{bcolors.ENDC}")
            print("-"*self.size_terminal)
            print(f"{'Total Buku': <10}{'Total Pengguna': ^25}{'Total Buku Dipinjam': ^25}{'Total Buku Mendakati Jatuh Tempo (H-3)': ^40}{'Total Buku Melewati Batas Pengembalian': >40}")
            print(f"{total_books: ^10}{total_users: ^25}")
            print("="*self.size_terminal)
            self.dashboard_menu(username)
            input()

    def dashboard_menu(self, username):
        menus = ["pengguna", "buku", "peminjaman buku", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Menu Aplikasi")
        if choosen_menu == 1:
            self.pengguna_menu(username)
        elif choosen_menu == 2:
            print(2)
        elif choosen_menu == 3:
            print(3)
        elif choosen_menu == 4:
            self.keluar_aplikasi() 

    def cetak_menu(self, menus: list, judul: str):
        print("")
        print(f"{bcolors.HEADER}{judul}{bcolors.ENDC}")
        print("+"*30)
        for i in range(len(menus)):
            print(f"{i+1}) {menus[i]}")
        choosen_menu = -1
        while choosen_menu < 1 or choosen_menu > len(menus):
            try:
                choosen_menu = int(input("masukkan pilihan anda: "))
                if choosen_menu < 1 or choosen_menu > len(menus):
                    raise Exception(f"{bcolors.FAIL}menu tidak tersedia{bcolors.ENDC}")
            except:
                print(f"{bcolors.FAIL}menu tidak tersedia{bcolors.ENDC}")
        return choosen_menu

    def keluar_aplikasi(self):
        print(f"{bcolors.OKCYAN}terimakasih{bcolors.ENDC}")
        quit()

# bagian pengguna
    def pengguna_menu(self, username):
        os.system("cls")
        self.header()
        self.cetak_pengguna(username)
        menus = ["daftar pengguna", "tambah pengguna", "ubah pengguna", "hapus pengguna", "kembali ke dashboard", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Pengguna Menu")
        if choosen_menu == 1:
            self.menu_daftar_pengguna(username)
        elif choosen_menu == 2:
            self.menu_tambah_pengguna(username)
        elif choosen_menu == 3:
            self.menu_ubah_pengguna(username)
        elif choosen_menu == 4:
            print(4)
        elif choosen_menu == 5:
            print(5)
        elif choosen_menu == 6:
            self.keluar_aplikasi() 

    def menu_daftar_pengguna(self,username):
        users = api.get_users()
        os.system("cls")
        self.header()
        self.cetak_pengguna(username)
        t = PrettyTable(["No", "NIK", "Nama", "Alamat"])
        for i in range(len(users)):
            t.add_row([i+1, users[i]["nik"], users[i]["nama"], users[i]["alamat"]])
        print(t)
        input(f"Tekan {bcolors.OKBLUE}enter{bcolors.ENDC} untuk kembali ke {bcolors.HEADER}Pengguna Menu{bcolors.ENDC}")
        self.pengguna_menu(username)

    def menu_tambah_pengguna(self,username):
        again = True
        while again:
            data = {}
            os.system("cls")
            self.header()
            self.cetak_pengguna(username)
            print("")
            result = {}
            try:
                data["nik"] = int(input("Masukkan NIK : "))
                data["username"] = data["nik"]
                data["password"] = data["nik"]
                data["nama"] = input("Masukkan Nama : ")
                data["alamat"] = input("Masukkan Alamat : ")
                result = api.add_user(data)
                if result["status"]:
                    print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                if not result["status"]:
                    print(f"{bcolors.FAIL}{result['detail']}{bcolors.ENDC}")
                confirm_again = input("Apakah Anda ingin menambah anggota lagi? (Y/n)")
                if confirm_again not in ["y", "Y", "n", "N"]:
                    raise Exception(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                if confirm_again == "N" or confirm_again == "n":
                    again = False
            except:
                print(f"{bcolors.FAIL}nik harus angka{bcolors.ENDC}")
                confirm = True
                while confirm:
                    confirm_again = input("Apakah Anda ingin menambah anggota lagi? (Y/n)")
                    if confirm_again not in ["y", "Y", "n", "N"]:
                        print(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                    if confirm_again == "N" or confirm_again == "n":
                        again = False
                        confirm = False
                    if confirm_again == "Y" or confirm_again == "y":
                        confirm = False
        self.pengguna_menu(username)

    def menu_ubah_pengguna(self, username):
        again = True
        while again:
            data = {}
            os.system("cls")
            self.header()
            self.cetak_pengguna(username)
            print("")
            result = {}
            try:
                nik = int(input("Masukkan NIK yang ingin diubah: "))
                user = api.get_user(nik)
                if len(user) > 0:
                    user = user[0]
                    print(f"NIK : {user['nik']}")
                    print(f"Nama : {user['nama']}")
                    print(f"Alamat : {user['alamat']}")
                    print("data diubah menjadi:")
                    data["nik"] = input("Masukkan NIK baru: ")
                    if len(data["nik"]) == 0:
                        data["nik"] = user["nik"]
                    data["username"] = data["nik"]
                    data["password"] = data["nik"]
                    data["nama"] = input("Masukkan nama baru: ")
                    if len(data["nama"]) == 0:
                        data["nama"] = user["nama"]
                    data["alamat"] = input("Masukkan alamat baru: ")
                    if len(data["alamat"]) == 0:
                        data["alamat"] = user["alamat"]
                    if user == data:
                        print(f"{bcolors.OKBLUE}data tidak ada yang berubah{bcolors.ENDC}")
                        confirm_again = input("Apakah Anda ingin mengubah anggota lagi? (Y/n)")
                        if confirm_again not in ["y", "Y", "n", "N"]:
                            raise Exception(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                        if confirm_again == "N" or confirm_again == "n":
                            again = False
                        continue
                    result = api.change_user(data)
                    if result["status"]:
                        print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                if len(user) == 0:
                    print(f"{bcolors.FAIL}user tidak ditemukan{bcolors.ENDC}")
                confirm_again = input("Apakah Anda ingin mengubah anggota lagi? (Y/n)")
                if confirm_again not in ["y", "Y", "n", "N"]:
                    raise Exception(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                if confirm_again == "N" or confirm_again == "n":
                    again = False
            except:
                print(f"{bcolors.FAIL}nik harus angka{bcolors.ENDC}")
                confirm = True            
                while confirm:
                    confirm_again = input("Apakah Anda ingin mengubah anggota lagi? (Y/n)")
                    if confirm_again not in ["y", "Y", "n", "N"]:
                        print(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                    if confirm_again == "N" or confirm_again == "n":
                        again = False
                        confirm = False
                    if confirm_again == "Y" or confirm_again == "y":
                        confirm = False
        self.pengguna_menu(username)
    
    def menu_hapus_pengguna(self, username):
        again = True
        while again:
            data = {}
            os.system("cls")
            self.header()
            self.cetak_pengguna(username)
            print("")
            result = {}

if __name__ == "__main__":
    app = LibraryApp()
