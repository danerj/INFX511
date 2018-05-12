###### Chapter 4 ######

import math

print(math.pi)

print(math.sin(math.pi / 4))

print((math.sin(math.pi / 3))**2 + (math.cos(math.pi / 3))**2)

import random

for i in range(10):
	print(random.random())

t = range(6)

for i in range(6):
	print(t[i])

print('\n \n')

for i in range(8):
	print(random.choice(t))

def print_lyrics():
	print("To the town of Agua Fria rode a stranger one fine day")
	print("Hardly spoke to folks around him, didn't have too much to say,")
	print("No one dared to ask his business, no one dared to make a slip")
	print("The stranger there among them had a big iron on his hip,")
	print("Big iron on his hip")

print_lyrics()

print(type(None))

###### Exercises ######

# Exercise 1

# I will run the program 3 times instead of 2 times

for iteration in range(3):
	for i in range(10):
		print(random.random())
	
	print('\n')


# Exercise 2

# This is the program and the error message you receive
# I have used a multline comment to embed the results in the script.
'''
repeat_lyrics()

def print_lyrics(): 
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

def repeat_lyrics():
	print_lyrics()
	print_lyrics()


Traceback (most recent call last):
  File "Chapter4script.py", line 63, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
'''

# Exercise 3

# I think it is important to note that the order in which the
# two functions are defined does not change the output from
# the original organization given in the textbook.

# From the textbook : "Function deﬁnitions do not alter the 
# ﬂow of execution of the program, but remember that statements
# inside the function are not executed until the function is called.
# A function call is like a detour in the ﬂow of execution. Instead
# of going to the next statement, the ﬂow jumps to the body of the 
# function, executes all the statements there, and then comes back
# to pick up where it left oﬀ".

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics(): 
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')


repeat_lyrics()

# Exercise 4

# Answer : d

# Exercise 5

# Answer : d

# Exercise 6

def computepay(hours,rate):
    if hours > 40:
        pay = hours * rate + (hours - 40) * rate * 0.5
    else:
        pay = hours * rate
    return pay

answer = computepay(45,10)
print(str(answer))

# Exercise 7

def computegrade(score):
    if score >= 0.9:
        print("A") 
    elif score >= 0.8:
        print("B") 
    elif score >= 0.7:
        print("C") 
    elif score >= 0.6:
        print("D") 
    else:
        print("F") 	

try:
    entry = float(input('Enter Score: '))
    if entry >= 0.0 and entry <= 1.0:
        computegrade(entry)
    else:
        print("Bad score")
except:
    print("Bad score") 
    quit()

