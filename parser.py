with open('log.txt', 'r') as inf:
	for line in inf:
		print("Всего запросов: " + str(len(inf.readlines())))
	inf.seek(0)		
	d = []; ipcount = 0
	for line in inf:
		if line[:15] not in d:
			d.append(line[:15])
			ipcount += 1
	print("Уникальных IP адресов: " + str(ipcount))
	inf.seek(0)
	a = []; countfirefox = 0; countsafari = 0; countedge = 0; countchrome = 0; countopera = 0
	for line in inf:
		if line[-25:] not in a:
			a.append(line[-25:])
	for i in a:
		if i.count("Firefox"): countfirefox += 1
		elif i.count("Safari"): countsafari += 1
		elif i.count("Edge"): countedge += 1
		elif i.count("Chrome"): countchrome += 1
		elif i.count("Opera"): countopera += 1
	print("Firefox: " + str(countfirefox))
	print("Safari: " + str(countsafari))
	print("Edge: " + str(countedge))
	print("Chrome: " + str(countchrome))
	print("Opera: " + str(countopera))
