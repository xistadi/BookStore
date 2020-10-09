from Packages.sql_cr import Users, Phone_numbers, Base
from Packages.delete_from_db import delete_from_db
from Packages.fetch_sqlite import fetch_sqlite
from Packages.insert_phonenumber import insert_phonenumber
from Packages.insert_sql import insert_sql
from Packages.update_db import update_db

while True:
	value = input(f"1.Ввести нового пользователя\n2.Удалить пользователя по id\n3.Обновить данные пользователя\n4.Добавить номер телефона по id\n5.Вывести весь список\nДля выхода введите 'выход'\n")
	if value == "1":
		insert_sql()
	elif value == "2":
		delete_from_db()
	elif value == "3":
		update_db()
	elif value == "4":
		insert_phonenumber()
	elif value == "5":
		fetch_sqlite()
	elif value == "выход":
		break
	else: 
		print("Введите правильно!")