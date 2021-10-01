name =input("Whats your name ?: ")
surname =input("Whats your surname ?: ")
gr =input("Whats the number of your group ?: " )
print("Hi!, " + surname + " "+ name + " in group " + gr )
email = input("Please, enter your email: ")
Otv = surname[:5] + name[:5]*2 + email[:5]*3
print("Your password: " + Otv.lower() )  # Вывод ответа