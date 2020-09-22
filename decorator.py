creds = {'name1': 'pass1', 'name2': 'pass2'}


def auth_required(func):
	def wrapper_decorator(*args, **kwargs):
		login = input("Enter login: ")
		password = input("Enter password: ")
		if login in creds and password == creds[login]:
			value = func(*args, **kwargs)
			return value
		return "Unknown user"
	return wrapper_decorator




@auth_required
def some_func(a, b):
	return(a + b)



print(some_func(2, 2))