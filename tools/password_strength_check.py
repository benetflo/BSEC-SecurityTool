import re


def password_length(password):

    p_len = len(password)
    if p_len < 8:
        return 0, True
    else:
        return 1, False

def password_complexity(password):
    
    temp_score = 0
    has_special = False
    has_digit = False
    has_capital = False
    has_lowercase = False
    
    for letter in password:

        if not has_special and re.match(r'[^a-zA-Z0-9]', letter):
            temp_score += 1
            has_special = True
        if not has_digit and re.match(r'[0-9]', letter):
            temp_score += 1
            has_digit = True
        if not has_capital and re.match(r'[A-Z]', letter):
            temp_score += 1
            has_capital = True
        if not has_lowercase and re.match(r'[a-z]', letter):
            temp_score += 1
            has_lowercase = True
        
        if has_special and has_digit and has_capital and has_lowercase:
            return temp_score, has_special, has_digit, has_capital, has_lowercase
    
    return temp_score, has_special, has_digit, has_capital, has_lowercase

def password_in_common_list(password, file_path):

    try:
        with open(file_path, "r") as f:
            for line in f:
                if password == line.strip():
                    return 0, False
    except FileNotFoundError:
        print("Could not read from list of common passwords, your password might be in list of common passwords!")
        return 0, False
    
    return 1, True




def info_to_user(points, p_too_short, has_special, has_lowercase, has_capital, has_digit, p_not_in_list):
    
    if points < 5:
        pass
    
    print()
    if p_too_short:
        print("You password is too short! You should consider making it longer than 8 characters!")
    if not has_special:
        print("Your password did not contain any special characters! (#%&?!)")
    if not has_lowercase:
        print("Your password did not contain any lowercase letters! (a-z)")
    if not has_capital:
        print("Your password did not contain any capital letters! (A-Z)")
    if not has_digit:
        print("Your password did not contain any numbers! (0-9)")
    if not p_not_in_list:
        print("You password is in list of commmon passwords! Consider using another password!")
    print()





def main():

    file_path = "tools/textfiles/10k-most-common.txt"
    points = 0
    temp_score = 0
    password_too_short = False
    password_has_special = False
    password_has_lowercase = False
    password_has_capital = False
    password_has_digit = False
    password_not_in_list = False

    while 1:
        print("\n/help for info")
        input_password = input("BSEC-PASSWORD-STRENGTH-CHECK$ ")
        if input_password == "exit":
            break
        elif input_password == "/help":
            pass
        else:
            temp_score, password_too_short = password_length(input_password)
            points += temp_score
            temp_score, password_has_special, password_has_digit, password_has_capital, password_has_lowercase = password_complexity(input_password)
            temp_score, password_not_in_list = password_in_common_list(input_password, file_path)
            info_to_user(points, password_too_short, password_has_special, password_has_lowercase, password_has_capital, password_has_digit, password_not_in_list)

def run():
    main()
