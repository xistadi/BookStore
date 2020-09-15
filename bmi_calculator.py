weight = int(input("Ваш вес в килограммах ? : ")) 
height = float(input("Ваш рост в метрах ?: "))
bmi = weight / (height ** 2) 
print("Ваш индекс массы тела: ", bmi) 
temp = round(((bmi - 20) / 30) * 10) # 30 шагов = 100%
if bmi > 50: # исключение 1
	print("20" + "="* 10 + "|50")
elif bmi < 20: # исключение 2
	print("20|" + "="* 10 + "50")
else: 
	print("20" + "="* temp + "|" + "="* (10 - temp) + "50")