import random
letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Litle kami password generator")
nr_letters = int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input("how many symbols would you like in your password?\n"))
nr_numbers = int(input("how many numbers would you like in your password?\n"))

password = []

for lett in range(1, nr_letters + 1):
    password += random.choice(letters)

for symb in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    
for numb in range(1, nr_numbers + 1):
    password += random.choice(numbers)
  
#print(password)
random.shuffle(password)
#print(password)
passwor = ""
for char in password:
    passwor += char
print(f"Your password is {passwor}")