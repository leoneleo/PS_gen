"""
Create random passwords using different types of characteres
"""

import random
import string


size=int(input("Enter the size of the password: ")) # get the size of the password
print(f"Your password has {size} characteres \n")

n_ps = int(input("Enter the number of possible password: ")) # get the number of different passwords




all_char = string.ascii_letters + string.digits # all characters without special ones
all_char_sp = string.ascii_letters + string.digits +string.punctuation # all char and punctiations

def req():
    """
    Check for password requirements like numbers, lower/upper case and special characters 
    """
    print('WHAT ARE THE REQUIREMENTS FOR YOUR PASSWORD? \n')
    print('',
        '1 - There must be no special characters \n',
        '2 - lower/upper case letters, numbers and special characters \n')
    
    answ = int(input("Type the correspondent number (1 or 2): "))
    
    if answ not in {1,2}:
        print('You must type either 1 or 2')
        answ = req()
    
    return answ
    
req_ans = req()

for j in range(n_ps):
    password = '' #empty password
    match req_ans:
        
        case 1:
            for i in range(size):
                password+=(all_char[random.randint(0,len(all_char)-1)])
            

        case 2:
            password+=(string.punctuation[random.randint(0,len(string.punctuation))])
            for i in range(size-1):
                password+=(all_char_sp[random.randint(0,len(all_char_sp)-1)])
    print(password)


