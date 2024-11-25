import random 
import string
import math

letters_upper= string.ascii_uppercase
letters_lower= string.ascii_lowercase
numbers= string.digits
symbols_specified= ['!', '#', '$', '%', '&', '*', '+', '?', '@', '^']

print(" we make a password containe 35%\ lowercase 35%\ uppercase 20%\ digits 10%\ symbols:")
password_lenght= int(input("Enter the lenght of password: "))

nb_lower= math.ceil(password_lenght*0.35)
nb_upper= math.ceil(password_lenght*0.35)
nb_digits= math.ceil(password_lenght*0.2)
nb_symbols= math.ceil(password_lenght*0.1)

if (nb_symbols+nb_digits+nb_lower+nb_upper)<=password_lenght:
    nb_lower+=password_lenght-(nb_symbols+nb_digits+nb_lower+nb_upper)
else : 
    nb_lower-= (nb_symbols+nb_digits+nb_lower+nb_upper)- password_lenght

print(nb_lower)
print(nb_upper)
print(nb_digits)
print(nb_symbols)

password= random.sample(letters_lower,nb_lower )+random.sample(letters_upper,nb_upper )+random.sample(numbers,nb_digits )+random.sample(symbols_specified,nb_symbols )

random.shuffle(password)

password= ''.join(password)


print("Generated password:", password)



