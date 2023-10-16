#NOT A RELIABLE MANAGER
#JUST FOR FUN
#pip install cryptography

import os
from cryptography.fernet import Fernet

# Create a txt file as a sister file to the py program
current_directory = os.path.dirname(os.path.abspath(__file__))
pwdName = "passwords.txt"
pwdFilepath = os.path.join(current_directory, pwdName)

# Create a cryptography file as a sister file to the py program
crptName = "key.key"
crptFilepath = os.path.join(current_directory, crptName)

#retrieve key from key.key file
def loadKey():
    file = open(crptFilepath, "rb")
    key = file.read()
    file.close()
    return key

key = loadKey()
fer = Fernet(key)

#get username/password from file
def view():
    with open(pwdFilepath, "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"Username: {user}, Password: " ,fer.decrypt(pwd.encode()).decode())

#add username/pwd from file 
def add():
    name = input("Account Name: \n")
    pwd = input("Password: \n")

    with open(pwdFilepath, "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n")

#selection mode
while True:
    mode = int(input("1 - New Password\n2 - Existing Password\n3 - Quit\n"))
    if mode == 1:
        add()
    elif mode == 2:
        view()
    elif mode == 3:
        break
    else:
        print("Invalid Option")