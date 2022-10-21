import os
import json
import shutil
import getpass
import sys
from API import API as api

class LibraryApp:
    """LibraryApp administration"""
    def __init__(self) -> None:
        os.system("cls")
        self.is_login = False
        self.size_terminal = shutil.get_terminal_size().columns
        api.create_user()
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
        print("")

    def login_validation(self, username, password):
        user = api.get_user()
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
            self.is_login = True
            return self.dashboard_menu()

        return sys.exit()

    def dashboard_menu(self):
        os.system("cls")
        self.header()
        print("dashboard")




if __name__ == "__main__":
    app = LibraryApp()
