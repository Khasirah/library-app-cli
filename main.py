import os
import json
import shutil
import getpass
import sys

class LibraryApp:
    def __init__(self) -> None:
        os.system("cls")
        self.size_terminal = shutil.get_terminal_size().columns
        self.db_path = "databases"
        self.check_user_db()
        self.header()
        self.login_menu()
    
    def check_user_db(self):
        is_user_json_exist = os.path.exists(f"{self.db_path}\\User.json")
        if is_user_json_exist == False:
            os.mkdir("databases")
            admin = {"username": "admin", "password": "admin"}
            json_string = json.dumps(admin)
            with open("databases\\User.json", "w") as user:
                user.write(json_string)
                user.close()
            print("berhasil membuat user admin dengan password admin, silahkan ganti password di menu ubah pengguna")
            input("Tekan (Enter) untuk menuju halaman login")
        return

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
        print("")
        return

    def login_validation(self, username, password):
        with open(f"{self.db_path}\\User.json", "r") as json_file:
            user = json.load(json_file)

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
        
        while ((not is_password_correct) and (count_incorrect <= 2)):
            username = input("Username: ")
            password = getpass.getpass("Password: ")

            result = self.login_validation(username, password)
            print(result["detail"])
            is_password_correct = result["status"]
            count_incorrect += 1

        if is_password_correct: 
            return self.dashboard_menu()

        return sys.exit()


    def dashboard_menu(self):
        os.system("cls")
        self.header()
        print("dashboard")




if __name__ == "__main__":
    app = LibraryApp()
