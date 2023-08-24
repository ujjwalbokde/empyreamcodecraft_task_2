import random
print("Welcome to python random password generator ! \n")
user_words = input("Enter words for password: ").split()
lst = []
splch = ['!', '@', '#', '$', '%', '*', '^', '&']
digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for word in user_words:
    lst.append(word)

num_digits = int(input("Enter the number of digits: "))
num_special_chars = int(input("Enter the number of special characters: "))

random.shuffle(lst)

password = []

for word in lst:
    password += word

    for i in range(1,num_digits+1):
        if num_digits > 0:
            char2 = random.choice(digit)
            password += char2
            num_digits -= 1

    for j in range(1,num_special_chars+1):
        if num_special_chars > 0:
            char3 = random.choice(splch)
            password += char3
            num_special_chars -= 1

random.shuffle(password)

password_m=""
for l in password:
    password_m+=l
print("Password =",password_m)