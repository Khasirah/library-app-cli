import json
import os
import time
import re
from utilities import utilities as u

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

# PUT
def change_user(data, nik_ubah):
    users = open_db_users()
    users = list(filter(lambda user: user["nik"] != nik_ubah, users))
    users.append(data)
    json_string = json.dumps(users)
    with open(PATH_USER, "w") as db:
        db.write(json_string)
        db.close()
    return {"status": True, "detail": "berhasil mengubah data"}

# DELETE
def delete_user(username):
    users = open_db_users()
    user = list(filter(lambda user: user["nik"] == username, users))
    if len(user) == 0:
        return {"status": False, "detail": "pengguna tidak terdaftar"}
    users = list(filter(lambda user: user["nik"] != username, users))
    json_string = json.dumps(users)
    with open(PATH_USER, "w") as db:
        db.write(json_string)
        db.close()
    return {"status": True, "detail": "berhasil menghapus data"}

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

def get_books():
    with open(PATH_BOOKS, "r") as json_file:
        books = json.load(json_file)
        return books

def get_book_by_id(book_id):
    books = get_books()
    pattern_number_only = '^\d+$'
    is_number = re.match(pattern_number_only, book_id)
    if is_number:
        book_id = int(book_id)
        if book_id < 0:
            return {"status": False, "detail": "angka tidak boleh lebih kecil dari 0"} 
        book = list(filter(lambda book: book["book_id"] == book_id, books))
        if len(book) == 0:
            return {"status": False, "detail": "buku tidak terdaftar"}
        return {"status": True, "data": book}
    else:
        return {"status": False, "detail": "harap masukkan angka"}

def get_book_by_name(book_name: str) -> dict:
    # check book_name
    if book_name.isspace() or len(book_name) == 0:
        return {"status": False, "detail": "nama buku tidak boleh kosong"}
    
    books = get_books()
    book_name = u.delete_first_char_space(book_name).lower()
    books = list(filter(lambda book: book_name in book["book_title"].lower(), books))
    
    if len(books) == 0:
        return {"status": False, "detail": "buku tidak ditemukan"}

    return {"status": True, "data": books}

# --------------------------------------
# POST
def post_book(data):
    books = get_books()
    book_id = get_total_book()
    time_now = int(round(time.time() * 1000))
    pattern = '(?:(?:18|19|20|21)[0-9]{2})'
    result = re.match(pattern, data["year_of_publication"])
    try:
        if result:
            data["year_of_publication"] = int(data["year_of_publication"])
        else:
            return {"status": False, "detail": "tahun terbit tidak sesuai format contoh: 1998"} 
    except:
        return {"status": False, "detail": "tahun terbit harus angka"}
    book = {
            "book_id": book_id,
            "book_title": data["book_title"],
            "book_author": data["book_author"],
            "year_of_publication": data["year_of_publication"],
            "publisher": data["publisher"],
            "created_at": time_now,
            "updated_at": time_now,
            "created_by": data["created_by"]
            }
    try:
        books.append(book)
        write_data_to_db(books, PATH_BOOKS)
    except:
        return {"status": False, "detail": "gagal input ke database"}  

    return {"status": True, "detail": "berhasil menambahkan buku"}  

# ------------------------------------------
# PUT
def change_book(data):
    time_now = int(round(time.time() * 1000))
    books = get_books()
    current_book_index = u.search_index(books, int(data["book_id"]), "book_id")
    current_book = get_book_by_id(data["book_id"])
    current_book = current_book["data"][0]
    data["book_id"] = int(data["book_id"])
    books = list(filter(lambda book: book["book_id"] != int(data["book_id"]), books))
    
    # check book_title
    if data["book_title"].isspace() or len(data["book_title"]) == 0:
        data["book_title"] = current_book["book_title"]
    
    data["book_title"] = u.delete_first_char_space(data["book_title"])
    
    # check book_author
    if data["book_author"].isspace() or len(data["book_author"]) == 0:
        data["book_author"] = current_book["book_author"]

    data["book_author"] = u.delete_first_char_space(data["book_author"])

    # check year_of_publication
    pattern = '(?:(?:18|19|20|21)[0-9]{2})'
    if data["year_of_publication"].isspace() or len(data["year_of_publication"]) == 0:
        data["year_of_publication"] = str(current_book["year_of_publication"])
    
    result_pattern_year = re.match(pattern, data["year_of_publication"])
    if result_pattern_year:
        data["year_of_publication"] = int(data["year_of_publication"])
    else:
        return {"status": False, "detail": "tahun terbit tidak sesuai format contoh: 1998"}

    # check publisher
    if data["publisher"].isspace() or len(data["publisher"]) == 0:
        data["publisher"] = current_book["publisher"]
    
    data["publisher"] = u.delete_first_char_space(data["publisher"])

    book = {
            "book_id": data["book_id"],
            "book_title": data["book_title"],
            "book_author": data["book_author"],
            "year_of_publication": data["year_of_publication"],
            "publisher": data["publisher"],
            "created_at": current_book["created_at"],
            "updated_at": time_now,
            "created_by": current_book["created_by"]
        }

    try:
        books.insert(current_book_index, book)
        write_data_to_db(books, PATH_BOOKS)
        return {"status": True, "detail": "berhasil memasukkan ke database"}
    except:
        return {"status": False, "detail": "gagal memasukkan ke database"}
    
# --------------------------------------------------
# DELETE
def delete_book(book_id):
    books = get_books()
    pattern_number_only = '^\d+$'
    is_number = re.match(pattern_number_only, book_id)
    if is_number:
        book_id = int(book_id)
        if book_id < 0:
            return {"status": False, "detail": "angka tidak boleh lebih kecil dari 0"}
        books = list(filter(lambda book: book["book_id"] != book_id, books))
        try:
            write_data_to_db(books, PATH_BOOKS)
            return {"status": True, "detail": "berhasil menghapus data"}
        except:
            return {"status": False, "detail": "gagal menghapus data"}
    else:
        return {"status": False, "detail": "harap masukkan angka"}