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
        api.create_db("User.json", [{"username": "admin", "password": "admin", "nik": "1111111111111111", "nama": "admin"}])
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
        user = list(api.get_user(username))
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
            self.dashboard_menu()
            input()

    def dashboard_menu(self):
        menus = ["pengguna", "buku", "peminjaman buku", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Menu Aplikasi")
        if choosen_menu == 1:
            self.pengguna_menu()
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
    def pengguna_menu(self):
        os.system("cls")
        self.header()
        menus = ["daftar pengguna", "tambah pengguna", "ubah pengguna", "hapus pengguna", "kembali ke dashboard", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Pengguna Menu")
        if choosen_menu == 1:
            self.menu_daftar_pengguna()
        elif choosen_menu == 2:
            print(2)
        elif choosen_menu == 3:
            print(3)
        elif choosen_menu == 4:
            print(4)
        elif choosen_menu == 5:
            print(5)
        elif choosen_menu == 6:
            self.keluar_aplikasi() 

    def menu_daftar_pengguna(self):
        users = api.get_users()
        os.system("cls")
        self.header()
        t = PrettyTable(["No", "NIK", "Nama", "Alamat"])
        for i in range(len(users)):
            t.add_row([i+1, users[i]["username"], "bla", "bla bal"])
        print(t)
        input(f"Tekan {bcolors.OKBLUE}enter{bcolors.ENDC} untuk kembali ke {bcolors.HEADER}Pengguna Menu{bcolors.ENDC}")
        self.pengguna_menu()

if __name__ == "__main__":
    app = LibraryApp()
