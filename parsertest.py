"""
парсер по списку "log = inf.read()" работает быстрее 
находит все упоминания "Chrome", "Safari", "Firefox", "Edge", "Opera"? скорее всего неправильно
имеет ограничение по памяти
"""
import re #регулярные выражения - https://habr.com/ru/post/349860/
reg = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #шаблон для поиска ip
browsers = ["Chrome", "Safari", "Firefox", "Edge", "Opera"]
with open("log.txt", "r") as inf:
	log = inf.read()
	ip_list = re.findall(reg, log) #все ip
	print("Всего запросов: " + str(len(ip_list)))
	print("Уникальных IP адресов: " + str(len(set(ip_list))))
	for browsers in browsers:
		print(browsers + ": " + str(len(re.findall(browsers, log))))