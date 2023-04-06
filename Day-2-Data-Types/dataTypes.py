'Strings'
# We can pull each character from a string using square brackets

print('Hello'[0]) #first character 
print('Hello'[-1]) #last character

print('1234' + '567') #concatinates the two numbers

#Interger

print(123 + 456)
#to put commas in numbers in python we use underscores
# the underscores are interpreted as computers as commmas
# this is to make them human readable
112_223_345_987

# Flaot -Decimal point
3.12334

#Boolen
True
False

num_chars = len(input('What is your name? '))
print(f'Your name has {num_chars} characetrs')
print(type(num_chars))

a = float(123)
print(type(a))
print(70 + float('100.5'))

####Day 2.1 data types challange

# Write a program that adds the digits in a 2 digit number. e.g. 
# if the input was 35, then the output should be 3 + 5 = 8

user_input =input('Enter a two digit number? ')

first_index = int(user_input[0])
second_index = int(user_input[1])

result = first_index + second_index
print(f'{first_index} + {second_index} = {result}')

# Mathematical operators in python
print(2+3)
print(4-1)
print(2*3)
print(6/3)
print(3**3)

#for operations with  many operators with high precedence are prioritized
# .The operators with same precedence ,the left most is considered first
print(3 * 3 + 3 / 3 - 3)
#change above code to get 3 instead of 7
print((3*3) / (3-3+3))

######Day 2.2 BMI CALCULATOR challenge
height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kgs: '))

#USING THE EXPONENT  OPERATOR AND PEMDASLR
bmi = int(weight / (height**2))
print(bmi)


# //f-string
score = 0
height = 1.8
isWinning = True

print(f'Your scoore is{score}, height is {height} and you are winning is {isWinning} ')

#day 2.3 Your life in weeks challenge
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
user_input = int(input('How old are you? '))

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

total_days =  90 * 365
total_weeks = 90 * 52
total_months = 90 * 12


message= (f'You have {total_days - (user_input * 365)} days, {total_weeks - (user_input * 52)} weeks and {total_months - (user_input* 12)} months left')
print(message)

#####TIP CALCULATOR - FINAL PROJECT

print('Welcome to the tip calculator!')
bill = float(input('What was your total bill? $'))
percentage_tip = int(input('What percentage tip would you like to give? 10, 12 or 15?'))
people = int(input('How many people to split the bill? '))

tip = (percentage_tip / 100) * bill + bill
each_person_total = round((tip / people),2)
print(f'Each person should pay {each_person_total}')
