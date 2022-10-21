import json
import os

# user json
def get_user():
    with open("databases\\User.json", "r") as json_file:
        user = json.load(json_file)
        return user 

def create_user(db_path):
    is_user_json_exist = os.path.exists(f"{db_path}\\User.json") 
    if is_user_json_exist == False:
        os.mkdir("databases")
        admin = {"username": "admin", "password": "admin"}
        json_string = json.dumps(admin)
        with open("databases\\User.json", "w") as user:
            user.write(json_string)
            user.close()
