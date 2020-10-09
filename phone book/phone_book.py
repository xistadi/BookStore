from Packages.sql_cr import Users, Phone_numbers, Base
from Packages.delete_from_db import *
from Packages.fetch_sqlite import *
from Packages.insert_phonenumber import *
from Packages.insert_sql import *
from Packages.update_db import *

print("kekw")

while True:
	value = input(f"1.Ввести нового пользователя\n2.Удалить пользователя по id\n3.Обновить данные пользователя\n4.Вывести полный список\nДля выхода введите 'выход'\n")
	if value == "1":
		insert_sql()
	elif value == "2":
		delete_from_db()
	elif value == "3":
		update_db()
	elif value == "4":
		fetch_sqlite()
	elif value == "выход":
		break
	else: 
		print("Введите правильно!")