print('Hello World!')
 ##Day 1.1 challange
 # # Write a program  that prints the same notes from the previous lesson using what you have learnt about the Python print function.

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

print('Day 1 - Python Print Function')
print('The Function is Declared like this:')
print("print('what to print')")

#new line
print('Hello world\nHello World\nHello world')
#concatination
print('Hello' + ' '+ 'Veronica')

##Day 1.2 challange
# The output in your program should match the example output shown below exactly, character for character, 
# even spaces and symbols should be identical, otherwise the tests won't pass.
# Day 1 - String Manipulation
# String Concatenation is done with the "+" sign.
# e.g. print("Hello " + "world")
# New lines can be created with a backslash and n.

print('Day 1 - String Manipulation\nString Concatination is done with the "+" sign.\ne.g. print("Hello " + "world")')
print('New lines are created with a backslash and n.')

#input function

#the input() will get user input in console
#Then print will print the word "Hello"  and the user input
print('Hello' + ' ' + input('What is your name? '))


##Day 1.3 challange
#  Write a program that prints the number of characters in a user's name. 
# You might need to Google for a function that calculates the length of a string.

##Option1
name =print(len(input('What is your name??')))
####option2 
# name = len(input('What is your name??'))
# print(name)

name = input('What is your name? ')
length = len(name)
print(length)

# Day 1.4 Challange
# Write a program that switches the values stored in the variables a and b.
a = input('a: ')
b = input('b: ')

#create a new variable and set to value of a
value = a
a = b
b = value

print("a: " + a)
print("b: " + b)

#### FINAL PROJECT - BAND NAME GENERATOR
## welcome the the user to the generator

print('Welcome to the band name generator.')

#Ask the user for the city they grew up in
city = input('What is the name of the city that you grew up in?\n')

#Ask for pet name
pet = input('What is the name of your pet?\n')

#combine city name and the pet name to show the user their band name
brand_name = city + pet
print(f'Your brand name is {brand_name}')
