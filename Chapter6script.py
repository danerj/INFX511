##### Chapter 6 #####

# In chapter examples and other things I want to try out.

fruit = 'banana'

letter = fruit[1]

print(letter)

grandma = fruit[2:]

print(grandma)

for char in fruit:
	print(char)
	

# Exercise 1
print('\nExercise 1 \n')


index = len(fruit)

while index >= 1:
	print(fruit[index-1])
	index = index - 1

# Exercise 2

# Given that fruit is a string, fruit[:] means the entire
# string stored in the variable fruit - i.e. start at the
# beginning and go to the end. Let's see :

print('\nExercise 2 \n\n' + fruit[:] + '\n')

# It checks out.

def count(word, target_letter):

	try:
		count = 0
		
		for letter in word:
		
			if letter == target_letter:
			
				count = count + 1
		
		print('The word ' + word + ' has the letter \'' + 
					target_letter + '\': ' + str(count) + ' times')
	except:
		print('Invalid input')


count(fruit,'a')
count('asdfasdfasdf','d')
count('yyyywer', 't')
count('Xian Noodles', 'o')

print('I' in 'Team')

help(str.encode)

line = 'Next stop Mercer Street'

print(line.lower().startswith('n'))

print(line.count('e'))

# Exercise 4

# Count how many times the letter 'a' occurs in the word banana,
# which is still stored as a string in the variable fruit.


print('\nExercise 4\n')
print(fruit.count('a'))



data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# Exercise 5

print('\nExercise 5\n')

str = 'X-DSPAM-Confidence:0.8475'

print(str)

number = float(str[str.find(':')+1:])

print(number)

print(type(number))


# Exercise 6

print('\nExercise 6\n')

print('   spacious   '.strip())
print('www.example.com'.strip('cmowz.'))
print('.....sdfasdf...sadfas..sadfas....sdfasdfasd')


# str.replace(old, new[, count])
# Return a copy of the string with all occurrences of substring old replaced by new.
# If the optional argument count is given, only the first count occurrences are replaced.


print(str.replace('-','!!!!!!!'))
print(str)