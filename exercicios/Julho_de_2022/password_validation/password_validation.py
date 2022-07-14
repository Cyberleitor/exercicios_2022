def creating_password():
	validation = False
	while validation == False:
		password = input('What will be your password? ')
		if len(password) >= 10:
			print("Okay, your password is valid. Don't forget him")
			validation = True
		else:
			print('Please, enter a password with 10 characters or more.')
			validation = False

creating_password()
