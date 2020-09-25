def my_generator():
	for i in range(1, 100):
		if i % 3: yield i
		else: yield "Василий"


g = my_generator()
while True:
	a = input("Вызов генератора? y/n: ")
	if a == "y":
		print(next(g))
	elif a == "n": break