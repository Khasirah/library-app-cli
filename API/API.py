import json
import os
import time

PATH_BOOKS = "databases\\Book.json"
PATH_USER = "databases\\User.json"

# user json
def get_user(username):
    with open(PATH_USER, "r") as json_file:
        users = json.load(json_file)
        return filter(lambda user: user["username"] == username, users)

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
def get_total_book():
    with open(PATH_BOOKS, "r") as json_file:
        books = json.load(json_file)
        return len(books) 

def get_all_books():
    with open(PATH_BOOKS, "r") as json_file:
        books = json.load(json_file)
        return books

def post_book(book_title, book_author, year_of_publication, publisher, created_by):
    books = get_all_books()
    book_id = len(books) + 1
    book = {
            "book_id": book_id,
            "book_title": book_title,
            "book_author": book_author,
            "year_of_publication":year_of_publication,
            "publisher": publisher,
            "created_at": int(round(time.time() * 1000))
            }    
