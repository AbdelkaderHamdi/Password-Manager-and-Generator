from  cryptography.fernet import Fernet

def write_key(): 
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
def load_key():
    file= open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter your master password? ")
key = load_key()
Fer= Fernet(key)

def view():
    with open('passwords.txt' , 'r') as f: 
        for line in f.readlines(): 
            data=line.rstrip()
            user, passw=data.split(" | ")
            print(f"User: {user} and its Password: {Fer.decrypt(passw.encode().decode())}")

def add():
    name= input("Account Name: ")
    pwd = input("Account password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + Fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode = input("Would you like to add a new password or view existing ones (add , view)? press q to quit:  ").strip().lower()

    if mode == 'q': 
        break
    elif mode == 'add': 
        add() 
    elif mode == 'view': 
        view()
    else : 
        print("Invalid mode! ")
        continue