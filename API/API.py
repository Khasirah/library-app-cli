from collections import UserString
import json
import os
import time

PATH_BOOKS = "databases\\Book.json"
PATH_USER = "databases\\User.json"

# write data to db
def write_data_to_db(data, db):
    json_string = json.dumps(data)
    with open(db, "w") as db_file:
        db_file.write(json_string)
        db_file.close()

# user json
def open_db_users():
    with open(PATH_USER, "r") as json_file:
        users = json.load(json_file)
        return users

# GET
def get_user(username):
    with open(PATH_USER, "r") as json_file:
        users = json.load(json_file)
        return list(filter(lambda user: user["username"] == username, users))
    
def get_total_user():
    with open(PATH_USER, "r") as json_file:
        users = json.load(json_file)
        return len(users)

def get_users():
    with open(PATH_USER, "r") as json_file:
        users = json.load(json_file)
        users = filter(lambda user: user.pop('password'), users)
        return list(users)

def get_user_by_nik(nik):
    users = open_db_users()
    return list(filter(lambda user: user["nik"] == nik, users))

# POST
def add_user(data):
    user_exist = len(get_user_by_nik(data["nik"]))
    if user_exist > 0:
        return {"status": False, "detail": "pengguna telah terdaftar"}

    users = open_db_users()
    users.append(data)

    try:
        write_data_to_db(users, PATH_USER)
        return {"status": True, "detail": "pengguna berhasil didaftarkan"}
    except Exception as e:
        return {"status": False, "detail": e}


# create DB
def create_db(db_name: str, data: list):
    path = "databases"
    is_folder_db_exist = os.path.exists("databases")
    if not is_folder_db_exist:
        os.mkdir("databases")
    is_db_exist = os.path.exists(f"{path}\\{db_name}")
    if not is_db_exist:
        json_string = json.dumps(data)
        with open(f"{path}\\{db_name}", "w") as db:
            db.write(json_string)
            db.close()
        print(f"berhasil membuat {db_name}")
    if is_db_exist:
        print(f"berhasil terhubung ke databases {db_name}")

# book json
# ======================================
# GET
def get_total_book():
    with open(PATH_BOOKS, "r") as json_file:
        books = json.load(json_file)
        return len(books) 

def get_all_books():
    with open(PATH_BOOKS, "r") as json_file:
        books = json.load(json_file)
        return books

# --------------------------------------
# POST
def post_book(book_title, book_author, year_of_publication, publisher, created_by):
    books = get_all_books()
    book_id = len(books) + 1
    time_now = int(round(time.time() * 1000))
    book = {
            "book_id": book_id,
            "book_title": book_title,
            "book_author": book_author,
            "year_of_publication":year_of_publication,
            "publisher": publisher,
            "created_at": time_now,
            "updated_at": time_now 
            }    
