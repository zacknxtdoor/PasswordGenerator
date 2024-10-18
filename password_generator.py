import random

def make_password(password_length):
    if password_length < 4:
        return "Error: password length must be greater than or equal to 4"
    
    
    symbols = '!@#$%^&*()?'
    digits = '0123456789'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    lst = []
    
    # Making sure that one character from each category is included
    lst.append(random.choice(symbols))
    lst.append(random.choice(digits))
    lst.append(random.choice(lowercase))
    lst.append(random.choice(uppercase))
    

    all_possibilities = symbols + digits + lowercase + uppercase
    for i in range(password_length - 4):
        lst.append(random.choice(all_possibilities))
    
    random.shuffle(lst)
    
    return "".join(lst)