from Packages.delete_from_db import delete_from_db
from Packages.fetch_sqlite import fetch_sqlite
from Packages.insert_phonenumber import insert_phonenumber
from Packages.insert_sql import insert_sql
from Packages.update_db import update_db
from Packages.clear_screen import clear_screen

def print_menu():
    # вывод основного меню
    line = "=" * 80
    while True:
        clear_screen()
        value = input(f"{line}\n1.Ввести нового пользователя\n2.Удалить пользователя по id\n3.Обновить данные пользователя\n4.Добавить номер телефона по id\n5.Вывести весь список\nДля выхода введите 'exit'\n{line}\n")
        if value == "1":
            clear_screen()
            insert_sql()
        elif value == "2":
            clear_screen()
            delete_from_db()
        elif value == "3":
            clear_screen()
            update_db()
        elif value == "4":
            clear_screen()
            insert_phonenumber()
        elif value == "5":
            clear_screen()
            fetch_sqlite()
        elif value == "exit":
            clear_screen()
            print("Всего доброго!")
            break
        else: 
            clear_screen()
            print("Вы ввели не правильно! Попробуйте снова!")
            input("Чтобы подолжить нажмите Enter")

if __name__ == "__main__":
    print_menu()