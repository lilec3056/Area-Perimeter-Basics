# ask user for their name

name = input("What is your name? ")

# ask user for their favourite integer

fav_num = int(input("What is your favourite number? "))

# Double, Halve and Square the users favourite number

double = fav_num * 2
half = fav_num / 2
square = fav_num ** 2

# greet the user

print(f"Hi {name}, your favourite number is {fav_num}!")

# output the results of doubling, halving and squaring the users fav number
print()
print(f"Half of your favourite number {fav_num} is {half}")
print(f"Double of your favourite number {fav_num} is {double}")
print(f"Your favourite number {fav_num} squared is {square}")
print()

print(f"Have an awesome day {name}!")
print()
