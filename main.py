import tools.port_scan
import tools.HTTP_header_inspector
import tools.password_strength_check

import os

def clear_screen():
    # if Windows
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux
        os.system('clear')




def show_disclaimer():
	disclaimer_text = f"""
	⚠️  IMPORTANT NOTICE  ⚠️

	This program is designed for educational purposes and security testing 
	on your own network or with explicit permission from the system owner.

	It is ILLEGAL to use this program for attacks or unauthorized access 
	to systems. The user is fully responsible for their actions.

	Use this tool only on your own network or with proper authorization.

	By continuing to use this program, you confirm that you understand and accept these terms.
	-----------------------------------------------------------------
	To proceed, you must confirm your intent to use this program responsibly. Type the following statement exactly as shown:

	I solemnly swear that I am up to ONLY good
	"""
	print(disclaimer_text)
	phrase = "I solemnly swear that I am up to ONLY good"

	tries_left = 3

	while tries_left != 0:
		answer = input()
		if answer == phrase:
			clear_screen()
			return True
		else:
			tries_left -= 1
			if tries_left == 0:
				print("Failed to accept terms, exiting program...")
				exit(0)
			print(f"Please accept the terms by typing in the phrase! You have {tries_left} tries left")


if __name__ == "__main__":
	if show_disclaimer():
		while 1:
			clear_screen()
			print(" ________________________________ ")
			print("|         WELCOME TO BSEC        |")
			print("|     Enter number to use tool   |")
			print("|________________________________|")
			print("|          1. Port scan          |")
			print("|   2. Password strength check   |")
			print("|    3. HTTP header inspector    |")
			print("|--------------------------------|")
			menu_answer = input("\n-> ")
			match menu_answer:
				case '1':
					tools.port_scan.run()
				case '2':
					tools.password_strength_check.run()
				case '3':
					tools.HTTP_header_inspector.run()
				case _:
					print("Invalid input!")
