import json
import os

# user json
def get_user():
    with open("databases\\User.json", "r") as json_file:
        user = json.load(json_file)
        return user 

def create_user():
    is_user_json_exist = os.path.exists("databases\\User.json") 
    if not is_user_json_exist:
        os.mkdir("databases")
        admin = {"username": "admin", "password": "admin"}
        json_string = json.dumps(admin)
        with open("databases\\User.json", "w") as user:
            user.write(json_string)
            user.close()
        print("berhasil membuat databases user")
        input("tekan Enter untuk melanjutkan ke halaman login")
    
    if is_user_json_exist:
        print("berhasil terhubung ke databases user")
