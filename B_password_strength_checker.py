#Funktion: KontrolleraLösenordStyrka(password)
#    Initialisera poäng = 0

#    // Steg 2: Kontrollera lösenordets längd
#    Om lösenordets längd är mindre än 8
#        Subtrahera 1 från poäng (låg poäng om för kort)
#    Annars
#        Lägg till 1 till poäng (bra längd)

#    // Steg 3: Kontrollera komplexiteten
#    Om lösenordet innehåller:
#        - Minst en liten bokstav
#        - Minst en stor bokstav
#        - Minst en siffra
#        - Minst ett specialtecken
#        Lägg till 2 till poäng (hög komplexitet)
#    Annars
#        Lägg till 1 till poäng (låg komplexitet)

#    // Steg 4: Kontrollera om lösenordet är ett vanligt lösenord
#   Om lösenordet finns i en lista med vanliga lösenord
#        Subtrahera 2 från poäng (vanligt lösenord)

#    // Steg 5: Bedöm lösenordets styrka
#    Om poäng <= 1
#        Returnera "Mycket svagt"
#    Annars om poäng = 2
#        Returnera "Svagt"
#    Annars om poäng = 3
#        Returnera "Måttligt"
#    Annars om poäng = 4
#        Returnera "Starkt"
#    Annars
#        Returnera "Mycket starkt"

import re


points = 0

def check_password_length(password):
	p_length = len(password)

	if p_length < 8: # if password is shorter than 8 chars
		return -1
	elif p_length > 8 and p_length < 16: # if password is longer than 8 but shorter than 16 chars
		return 1
	else: # if password is longer than 16 chars
		return 2

def check_password_complexity(password):

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



def check_password_if_common(password):
	pass

def password_strength(points):
	

