users = ['A','B','admin','d','e']
for user in users:
	if user=='admin':
		print('hello ' +user+', would you like to see a status report?')

	else:
		print('hello '+user+', thank you for logging in again.')