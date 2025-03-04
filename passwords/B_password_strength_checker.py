import re

global password_known = False
global password_too_short = False
global password_not_complex = False

points = 0
FILE_NAME = "rock_you.txt"

def check_password_length(password):

	global password_too_short

	p_length = len(password)

	if p_length < 8: # if password is shorter than 8 chars
		return -1
		password_too_short == True
	elif p_length > 8 and p_length < 16: # if password is longer than 8 but shorter than 16 chars
		return 1
	else: # if password is longer than 16 chars
		return 2

def check_password_complexity(password):

	global password_not_complex
	# assign standard value
	has_digit = False
	has_special_sign = False
	has_capital_letter = False
	has_lowercase_letter = False

	temp_arr = [has_digit, has_special_sign, has_capital_letter, has_lowercase_letter] # array to store all checks for later use

	for letter in password:
		if has_digit and has_special_sign and has_capital_letter and has_lowercase_letter: # break if all are True. No need to continue loop
			break
		if re.match(r'[a-z]', letter): # if password contains a lowercase letter
			has_lowercase_letter = True
		if re.match(r'[A-Z]', letter): # if password contains a capital letter
			has_capital_letter = True
		if re.match(r'/d', letter): # if password contains a digit
			has_digit = True
		if re.match(r'[^\w\s]', letter): # if password contains a special sign
			has_special_sign = True
	counter = 0 # counter var to keep count of 'has_'-variables True-states
	for i in temp_arr:
		if i == True: # add 1 to counter var if 'has_' == True
			counter += 1

	if counter == 4: # if all 'has_' == True
		return 2
	elif counter == 3: # if all but one 'has_' == True
		return 1
	else # if one or two 'has_' == True
		return -1
		password_not_complex = True



def check_password_if_common(password, COMMON_PASSWORDS):
	try:
		with open(COMMON_PASSWORDS, "r", encoding="latin-1") as file: # change encoding if you are using file that is not using "latin-1"
		for line in line:
			if password == line.strip(): # password is in list of common passwords
				return -1
				password_known = True
			else: # if password NOT in list of common passwords
				return 1

	except FileNotFoundError as e:
		print("File not found: {e}")
		return 0

def password_strength(points):

	if password_known:
		print("Password is in list of common passwords!")
	if password_too_short:
		print("Password is too short!")
	if password_not_complex:
		print("Password is not complex enough. Did you use atleast one of each: example(#9bA)")

	if points > 3:
		print("Your password is very good")
	elif points == 3 or points == 2:
		print("Your password is good")
	elif points == 1 or points == 0:
		print("Your password is weak")
	else:
		print("Your password is very weak")

def main(points, FILE_NAME)

	while 1:
		input_password = input("B-PasswordStrength$ ")
		check_password_length(input_password)
		check_password_complexity(input_password)
		check_password_if_common(input_password, FILE_NAME)
		password_strength(points)
