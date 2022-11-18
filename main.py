import os
import shutil
import getpass
import sys
from API import API as api
from colors import bcolors
from prettytable import PrettyTable
import datetime as dt

class LibraryApp:
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
            print(f"{'Total Buku': <10}{'Total Pengguna': ^25}")
            print(f"{total_books: ^10}{total_users: ^25}")
            print("="*self.size_terminal)
            self.dashboard_menu(username)

    def dashboard_menu(self, username):
        menus = ["pengguna", "buku", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Menu Aplikasi")
        if choosen_menu == 1:
            return self.pengguna_menu(username)
        elif choosen_menu == 2:
            return self.buku_menu(username)
        elif choosen_menu == 3:
            return self.keluar_aplikasi() 

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
    
    def template_page(self, username):
        os.system("cls")
        self.header()
        self.cetak_pengguna(username)
        print("")
        return
    
    def konfirmasi_ulang(self):
        confirm = True
        while confirm:
            confirm_again = input("Apakah Anda ingin melakukan operasi ini lagi? (Y/n) ")
            if confirm_again not in ["y", "Y", "n", "N"]:
                print(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                continue
            if confirm_again == "y" or confirm_again == "Y":
                confirm = False
                again = True
                return again
            if confirm_again == "N" or confirm_again == "n":
                again = False         
                confirm = False
                return again

    def konfirmasi_operasi(self):
        again = True
        while again:
            submit = input("Apakah anda yakin? (Y/n) ")
            if submit not in ["Y", "y", "N", "n"]:
                print(f"{bcolors.FAIL}pilihan tidak tersedia{bcolors.ENDC}")
                continue
            if submit == "Y" or submit == "y":
                again = False
                return True
            if submit == "N" or submit == "n":
                again = False
                return False

    def keluar_aplikasi(self):
        print(f"{bcolors.OKCYAN}terimakasih{bcolors.ENDC}")
        quit()

# bagian pengguna
    def pengguna_menu(self, username):
        self.template_page(username)
        menus = ["daftar pengguna", "tambah pengguna", "ubah pengguna", "hapus pengguna", "kembali ke dashboard", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Pengguna Menu")
        if choosen_menu == 1:
            return self.menu_daftar_pengguna(username)
        elif choosen_menu == 2:
            return self.menu_tambah_pengguna(username)
        elif choosen_menu == 3:
            return self.menu_ubah_pengguna(username)
        elif choosen_menu == 4:
            return self.menu_hapus_pengguna(username)
        elif choosen_menu == 5:
            return self.dashboard_page(username)
        elif choosen_menu == 6:
            return self.keluar_aplikasi()

    def menu_daftar_pengguna(self,username):
        users = api.get_users()
        self.template_page(username)
        t = PrettyTable(["No", "NIK", "Nama", "Alamat"])
        for i in range(len(users)):
            t.add_row([i+1, users[i]["nik"], users[i]["nama"], users[i]["alamat"]])
        print(t)
        input(f"Tekan {bcolors.OKBLUE}enter{bcolors.ENDC} untuk kembali ke {bcolors.HEADER}Pengguna Menu{bcolors.ENDC}")
        return self.pengguna_menu(username)

    def menu_tambah_pengguna(self,username):
        again = True
        while again:
            data = {}
            self.template_page(username)
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
            except:
                print(f"{bcolors.FAIL}nik harus angka{bcolors.ENDC}")
            again = self.konfirmasi_ulang()
        return self.pengguna_menu(username)

    def menu_ubah_pengguna(self, username):
        again = True
        while again:
            data = {}
            self.template_page(username)
            result = {}
            try:
                nik = int(input("Masukkan NIK yang ingin diubah: "))
                user = api.get_user(nik)
                if len(user) > 0:
                    user = user[0]
                    print(f"NIK : {user['nik']}")
                    print(f"Nama : {user['nama']}")
                    print(f"Alamat : {user['alamat']}")
                    print("")
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
                        again = self.konfirmasi_ulang()
                        continue
                    data["nik"] = int(data["nik"])
                    result = api.change_user(data, nik)
                    if result["status"]:
                        print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                if len(user) == 0:
                    print(f"{bcolors.FAIL}user tidak ditemukan{bcolors.ENDC}")
            except:
                print(f"{bcolors.FAIL}nik harus angka{bcolors.ENDC}")
            again = self.konfirmasi_ulang()
        return self.pengguna_menu(username)
    
    def menu_hapus_pengguna(self, username):
        again = True
        while again:
            self.template_page(username)
            result = {}
            nik = 0
            try:
                nik = int(input("Masukkan NIK yang ingin dihapus: "))
            except:
                print(f"{bcolors.FAIL}nik harus angka{bcolors.ENDC}") 
                again = self.konfirmasi_ulang()
                continue
            submit = self.konfirmasi_operasi()
            if submit:
                result = api.delete_user(nik)
                if result["status"]:
                    print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                if not result["status"]:
                    print(f"{bcolors.FAIL}{result['detail']}{bcolors.ENDC}")
            again = self.konfirmasi_ulang()
            continue
        return self.pengguna_menu(username)

# bagian buku
    def buku_menu(self, username):
        self.template_page(username)
        menus = ["daftar buku", "tambah buku", "ubah buku", "hapus buku", "cari buku", "kembali ke dashboard", "keluar aplikasi"]
        choosen_menu = self.cetak_menu(menus, "Buku Menu")
        if choosen_menu == 1:
            return self.menu_daftar_buku(username)
        elif choosen_menu == 2:
            return self.menu_tambah_buku(username)
        elif choosen_menu == 3:
            return self.menu_ubah_buku(username)
        elif choosen_menu == 4:
            return self.menu_hapus_buku(username)
        elif choosen_menu == 5:
            return self.cari_buku(username)
        elif choosen_menu == 6:
            return self.dashboard_page(username)
        elif choosen_menu == 7:
            return self.keluar_aplikasi()

    def menu_daftar_buku(self,username):
        books = api.get_books()
        self.template_page(username)
        t = PrettyTable(["No", "ID", "Judul", "Penulis", "Tahun Terbit", "Penerbit", "Tgl di Perpustakaan", "Tgl di Update", "diinput oleh"])
        for i in range(len(books)):
            t.add_row([i+1, books[i]["book_id"], books[i]["book_title"], books[i]["book_author"], books[i]["year_of_publication"], books[i]["publisher"], dt.datetime.fromtimestamp(books[i]["created_at"] / 1000).strftime("%d-%m-%Y %H:%M:%S"), dt.datetime.fromtimestamp(books[i]["updated_at"] / 1000).strftime("%d-%m-%Y %H:%M:%S"), books[i]["created_by"]])
        print(t)
        input(f"Tekan {bcolors.OKBLUE}enter{bcolors.ENDC} untuk kembali ke {bcolors.HEADER}Pengguna Menu{bcolors.ENDC}")
        return self.buku_menu(username)

    def menu_tambah_buku(self,username):
        again = True
        while again:
            data = {}
            self.template_page(username)
            print(f"{bcolors.WARNING}pastikan cek terlebih dahulu sebelum (enter){bcolors.ENDC}")
            data["book_title"] = input("Masukkan judul buku: ")
            data["book_author"] = input("Masukkan nama penulis: ")
            data["year_of_publication"] = input("Masukkan tahun terbit: ")
            data["publisher"] = input("Masukkan penerbit: ")
            data["created_by"] = username
            submit = self.konfirmasi_operasi()
            if submit:
                result = api.post_book(data)
                if result["status"]:
                    print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                if not result["status"]:
                    print(f"{bcolors.FAIL}{result['detail']}{bcolors.ENDC}")
            again = self.konfirmasi_ulang()

        return self.buku_menu(username)

    def menu_ubah_buku(self, username):
        again = True
        while again:
            data = {}
            self.template_page(username)
            print(f"{bcolors.WARNING}pastikan cek terlebih dahulu sebelum (enter){bcolors.ENDC}")
            book_id = -1
            book_id = input("Masukkan id buku: ")
            book = api.get_book_by_id(book_id)
            if book["status"]:
                print(f"ID Buku: {book['data'][0]['book_id']}")
                print(f"Judul Buku: {book['data'][0]['book_title']}")
                print(f"Penulis: {book['data'][0]['book_author']}")
                print(f"Tahun terbit: {book['data'][0]['year_of_publication']}")
                print(f"Penerbit: {book['data'][0]['publisher']}")
                print("")
                print("data diubah menjadi:")
                data["book_id"] = str(book['data'][0]['book_id'])
                data["book_title"] = input("Masukkan judul baru: ")
                data["book_author"] = input("Masukkan penulis baru: ")
                data["year_of_publication"] = input("Masukkan tahun terbit baru: ")
                data["publisher"] = input("Masukkan penerbit baru: ")
                print(f"{bcolors.WARNING}apabila kosong maka dianggap tidak diubah{bcolors.ENDC}")
                submit = self.konfirmasi_operasi()
                if submit:
                    result = api.change_book(data)
                    if result["status"]:
                        print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                    if not result["status"]:
                        print(f"{bcolors.FAIL}{result['detail']}{bcolors.ENDC}")
            if not book["status"]:
                print(f"{bcolors.FAIL}{book['detail']}{bcolors.ENDC}")
            again = self.konfirmasi_ulang()
            
        return self.buku_menu(username)
    
    def menu_hapus_buku(self, username):
        again = True
        while again:
            self.template_page(username)
            book_id = input("Masukkan id buku: ")
            book = api.get_book_by_id(book_id)
            if book["status"]:
                print(f"ID Buku: \t{book['data'][0]['book_id']}")
                print(f"Judul Buku: \t{book['data'][0]['book_title']}")
                print(f"Penulis: \t{book['data'][0]['book_author']}")
                print(f"Tahun terbit: \t{book['data'][0]['year_of_publication']}")
                print(f"Penerbit: \t{book['data'][0]['publisher']}")
                print(f"{bcolors.WARNING}buku tersebut akan dihapus.{bcolors.ENDC}")
                submit = self.konfirmasi_operasi()
                if submit:
                    result = api.delete_book(book_id)
                    if result["status"]:
                        print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
                    if not result["status"]:
                        print(f"{bcolors.OKCYAN}{result['detail']}{bcolors.ENDC}")
            if not book["status"]:
                print(f"{bcolors.FAIL}{book['detail']}{bcolors.ENDC}")
            again = self.konfirmasi_ulang()

        return self.buku_menu(username)
    
    def cari_buku(self, username):
        again = True
        while again:
            self.template_page(username)
            book_name = input("Masukkan naama buku yang ingin dicari: ")
            result = api.get_book_by_name(book_name)
            if result["status"]:
                t = PrettyTable(["No", "ID", "Judul", "Penulis", "Tahun Terbit", "Penerbit", "Tgl di Perpustakaan", "Tgl di Update", "diinput oleh"])
                for i in range(len(result["data"])):
                    t.add_row([i+1, result["data"][i]["book_id"], result["data"][i]["book_title"], result["data"][i]["book_author"], result["data"][i]["year_of_publication"], result["data"][i]["publisher"], dt.datetime.fromtimestamp(result["data"][i]["created_at"] / 1000).strftime("%d-%m-%Y %H:%M:%S"), dt.datetime.fromtimestamp(result["data"][i]["updated_at"] / 1000).strftime("%d-%m-%Y %H:%M:%S"), result["data"][i]["created_by"]])
                print(t)
            if not result["status"]:
                print(f"{bcolors.FAIL}{result['detail']}{bcolors.ENDC}")
            again = self.konfirmasi_ulang()

        return self.buku_menu(username)

if __name__ == "__main__":
    app = LibraryApp()
