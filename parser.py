#построчный парсер работает только по срезам из строк

browsers = {"Chrome": 0, "Safari": 0, "Firefox": 0, "Edge": 0, "Opera": 0}
with open("log.txt", "r") as inf:
	for line in inf: print("Всего запросов: " + str(len(inf.readlines())))
	inf.seek(0) 
	d = []
	for line in inf:
		if line[:15] not in d: #срез первых 15-ти символов с ip 
			d.append(line[:15])
	print("Уникальных IP адресов: " + str(len(d)))
	inf.seek(0)
	for line in inf:
		for key in browsers:
			if line[-35:-6].find(key) > 0: #если в срезанной строке есть браузер "key"
				browsers[key] += 1 #добавляем в счетчик по ключу 
	for key in browsers:
		print(key + ": " + str(browsers[key]))