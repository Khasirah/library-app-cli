import os
import shutil
import getpass
import sys
from API import API as api
from colors import bcolors

class LibraryApp:
    """LibraryApp administration"""
    def __init__(self) -> None:
        os.system("cls")
        self.is_login = False
        self.size_terminal = shutil.get_terminal_size().columns
        api.create_db("User.json", [{"username": "admin", "password": "admin"}])
        api.create_db("Book.json", [])
        input("Tekan enter untuk melanjutkan login")
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
        user = user[0]
        result = {}

        if username != user["username"]:
            result["status"] = False
            result["detail"] = "username tidak sesuai"
            return result

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
        if self.is_login:
            self.header()
            user = list(api.get_user(username))
            user = user[0]
            print(f"selamat datang, {user['username']}".rjust(self.size_terminal))
            print(f"{bcolors.HEADER}INFORMASI{bcolors.ENDC}")
            print("-"*self.size_terminal)
            print(f"{'Total Buku': <10}{'Total Buku Dipinjam': ^25}{'Total Buku Mendakati Jatuh Tempo (H-3)': ^40}{'Total Buku Melewati Batas Pengembalian': >40}")
            print(f"{total_books: ^10}")
            print("="*self.size_terminal)
            self.dashboard_menu()
            input()

    def dashboard_menu(self):
        print("")
        print(f"{bcolors.HEADER}Menu Aplikasi Perpustakaan{bcolors.ENDC}")
        print("+"*30)
        print("1. tambah buku")
        print("2. update buku")
        print("3. hapus buku")
        print("5. lihat daftar buku")
        print("6. peminjaman buku")
        print("7. pengembalian buku")
        print("8. lihat daftar buku dipinjam")
        print("9. keluar aplikasi")
        menu = -1
        while menu == -1:
            try:
                menu = int(input("masukkan pilihan anda: "))
            except:
                print(f"{bcolors.FAIL}menu tidak tersedia{bcolors.ENDC}")
        return menu

if __name__ == "__main__":
    app = LibraryApp()
