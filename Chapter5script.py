############# Chapter 5 ################
'''
while True:

	line = input('> ')
	
	if line == 'done':
	
		break 
		
	print(line) 

print('Done!')

# Exercise 1

total = 0
count = 0

while True:

	try:
	
		user_input = input('Enter a number or enter \'done\' to quit: \n')
		
		if user_input == 'done':
			
			break
		
		user_input = float(user_input)
		
		total = total + user_input
		
		count = count + 1
		
	except:
		
		print('bad data')
	


average = total / count

print(total, count, average)
'''
# Exercise 2

max = None
min = None

while True:

	try:
	
		user_input = input('Enter a number or enter \'done\' to quit: \n')
		
		if user_input == 'done':
		
			break
			
		user_input = float(user_input)
		
		if max == None:
		
			max = user_input
			min = user_input
		
		elif user_input > max:
		
			max = user_input
		
		elif user_input < min:
		
			min = user_input
			
	
	except:
	
		print('bad input')

print('min = ', min,'max = ', max)
