#построчный парсер работает по срезам из строк
import re #регулярные выражения - https://habr.com/ru/post/349860/
reg = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #шаблон для поиска ip
browsers = {"Chrome": 0, "Safari": 0, "Firefox": 0, "Edge": 0, "Opera": 0}
with open("log.txt", "r") as inf:
	log = inf.read()
	ip_list = re.findall(reg, log) #все ip
	print("Всего запросов: " + str(len(ip_list)))
	print("Уникальных IP адресов: " + str(len(set(ip_list))))
	inf.seek(0)
	for line in inf:
		for key in browsers:
			if line[-35:-6].find(key) > 0: #если в срезанной строке есть браузер "key"
				browsers[key] += 1 #добавляем в счетчик по ключу 
	for key in browsers:
		print(key + ": " + str(browsers[key]))