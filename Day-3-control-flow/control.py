
# Free for mid life crisis that is between 45 and 55
# print('Welcme to the Rollercoaster')
# height = int(input('What is your height in cm ? '))
# bill = 0

# if height >= 120:
#     print('You can the rollercoaster')
#     age = int(input('What is your age ? '))
#     if age < 12:
#         bill = 5
#         print('Child ticket pay $ 5.')
#     elif age <= 18:
#         bill = 7
#         print('Youth ticket pay $ 7.')
#     elif age >= 45 and age <= 55:
#         print('Everything is gonna be okay, have a free ride on us')
#     else:
#         bill = 12
#         print('Adult ticket pay $12 ')

#     wants_photo = input('Do you want a photo taken? Type Y or N.')
#     if wants_photo == 'Y':
#        bill += 3
#     print(f'Your final bill is {bill}')
# else:
#     print('Sorry, you have to grow taller before you can ride.')


# # A program that checks whether the number entered is /odd or Even
# number = int(input('Which number do you want to check ? '))

# if number % 2 == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')


# height = float(input('Enter your height in meters: '))
# weight = float(input('Enter your weight in kgs: '))

# bmi = round(weight / (height**2), 1)

# if bmi < 18.5:
#     print(f'Your bmi is : {bmi}, you are underweight.')
# elif bmi < 25:
#     print(f'Your bmi is {bmi}, you have normal weight.')
# elif bmi < 30:
#     print(f'Your bmi is {bmi}, you are overweight.')
# elif bmi < 35:
#     print(f'Your bmi is {bmi}, you are obese.')
# else:
#     print(f'Your bmi is {bmi}, your are clinically obese')


# # Write a program that works out whether if a given year is a leap year.
# #  A normal year has 365 days, leap years have 366, with an extra day in February.

# year = int(input('Which year do you want to check ? '))

# if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#        print(f'{year} is a leap year.')
#       else:
#         print(f'{year}  is not a leap year')
#     else:
#      print(f'{year} is a leap year.')
# else:
#     print(f'{year}  is not a leap year')


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# # Based on a user's order, work out their final bill.

# # Small Pizza: $15

# # Medium Pizza: $20

# # Large Pizza: $25

# # Pepperoni for Small Pizza: +$2

# # Pepperoni for Medium or Large Pizza: +$3

# # Extra cheese for any size pizza: + $1
# bill = 0
# if size == "S":
#         bill += 15
# elif size == "M": 
#         bill += 20
# else:
#         bill += 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2  
# else:
#     bill += 3 
# if extra_cheese  == "Y":
#     bill += 1
# print(f"Your final bill is: ${bill}.")

# # LOVE CALCULATOR
'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
'''
print('Welcome to the love Calculator. ')
name1 = input('What is your name ?\n')
name2 = input('What is their name ?\n')

string_combined = name1 + name2
lower_case_string = string_combined.lower()
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u +e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')


love = l + o + v + e

love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}, you go together like coke and mentos.')
    
elif (love_score >= 40) and (love_score <= 50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
user_input1 = input('You\'re at a cross road.Where do you want to go ? Type "left" or "right"\n').lower()


if user_input1 == 'left':
    user_input2 = input('You have come to a lake.There is an Island in the middle of the lake. Type "wait" to wait for a boat. Or "swim to swim across."\n').lower()
    if user_input2 == 'wait':
        user_input3 = input('You have arrived at the island unharmed.There is a house with there doors.One red, One yellow and One blue.Which colour do you  choose?\n ').lower()
        if user_input3 == 'blue':
            print('You entered a room full of beasts.Game over')
        elif user_input3 == 'red':
            print('You entered a room full of fire.Game over')
        elif user_input3 == 'yellow':
            print('You found the treasure. You win!')
        else:
            print('You chose the door that does\'nt exist.Game over')
    else:
        print('You got attached by a crocoGame over')
else:
    print('You fell into a ditch. Game Over')


















