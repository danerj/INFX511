##### Chapter 8 #####

t1 = ['a', 'b', 'c']

t2 = ['d', 'e']

t3 = t1 + t2

t1.extend(t2)

print(t3)

print(t1)

print(t2)

t4 = []

for i in range(len(t1)):
	
	t4.append(t1.pop())
	
print(t4)

### Exercise 1

print('\n Exercise 1 \n')

def chop(t):

	del t[0]
	
	del t[len(t)-1]
	

chop(t4)

print(t4)

jaques = 'Jaques Babaganoosh'

jaques = jaques.split()

jaques = jaques[0] + jaques[1]

jaques = list(jaques)

print(jaques)


### Exercise 2

print('\n Exercise 2 \n')

# The first line is not guarded. Also the for loop. Rewritten with try/except:

fname = 'mbox-short.txt'

try:

    fhand = open(fname)
	
except:

    print("File not found:", fname)
	
    quit()
	
try:

    for line in fhand:
	
        words = line.split()
		
        if len(words) == 0 : continue
		
        if words[0] != 'From' : continue
		
        print(words[2])
		
except:

    print("File:", fname," could not be found")
	
    quit()
	

### Exercise 3

print('\n Exercise 3 \n')

fname = 'mbox-short.txt'

try:

    fhand = open(fname)
	
except:

    print("File not found:", fname)
	
    quit()
	
try:

    for line in fhand:
	
        words = line.split()
		
        if len(words) != 0 and words[0] == 'From':
		
            print(words[2])

except:

    print("File:", fname," is empty")
	
    quit()

### Exercise 4

print('\n Exercise 4 \n')

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	word_list = []
	
	for line in file_handle:
	
		line = line.split()
		
		for word in line:
		
			if not word in word_list:
			
				word_list.append(word)
			
	
	word_list.sort()
	
	print(word_list)
	

except:

	print('File cannot be opened : ' + file_name)
	


### Exercise 5

print('\n Exercise 5 \n')

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	count = 0
	
	for line in file_handle:
	
		if line[:5] == 'From ':
		
			words = line.split()
			
			print(words[1])
		
			count = count + 1
	
	print('There were ' + str(count) + ' lines in the file with From as the first word')
	

except:

	print('File cannot be opened : ' + file_name)

	


### Exercise 6

print('\n Exercise 6 \n')

number_list = []

while True:

	try:
	
		user_input = input('Enter a number or enter \'done\' to quit: \n')
		
		if user_input == 'done':
		
			break
			
		number_list.append(float(user_input))
			
	
	except:
	
		print('bad input')


if len(number_list) > 0:
	print('minimum = ', str(min(number_list)),'maximum = ', str(max(number_list)))

