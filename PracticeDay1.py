user_name = input("What is your name? ")
birth_year = int(input("Age? ")) 

print(f"Hi {user_name}, in 10 years you will be {birth_year + 10} years old.")

first_numer = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(f"The sum of {first_numer} and {second_number} is {first_numer + second_number}.")
print(f"The difference of {first_numer} and {second_number} is {first_numer - second_number}.")
print(f"The product of {first_numer} and {second_number} is {first_numer * second_number}.")
print(f"The quotient of {first_numer} and {second_number} is {first_numer / second_number}.")
print(f"The floor division of {first_numer} and {second_number} is {first_numer // second_number}.")
print(f"The remainder of {first_numer} and {second_number} is {first_numer % second_number}.")


temperature_celsius = float(input("Enter temperature in Celsius: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is {temperature_fahrenheit}.")

number = int(input("Enter a number to check if it is even or odd: "))
if number % 2 == 0:
    print(f"{number} is even.") 
else:
    print(f"{number} is odd.")