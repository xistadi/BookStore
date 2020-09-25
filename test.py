import re #регулярные выражения - https://habr.com/ru/post/349860/
reg = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
reg2 = r"" #пробовал шаблон для браузеров, работает медленнее.
with open("log.txt", "r") as inf:
	log = inf.read()
	ip_list = re.findall(reg, log)
	print("Всего запросов: " + str(len(ip_list)))
	print("Уникальных IP адресов: " + str(len(set(ip_list))))
	print("Chrome: " + str(len(re.findall("Chrome", log))))
	print("Safari: " + str(len(re.findall("Safari", log))))
	print("Firefox: " + str(len(re.findall("Firefox", log))))
	print("Microsoft Edge: " + str(len(re.findall("Edge", log))))
	print("Opera: " + str(len(re.findall("Opera", log))))