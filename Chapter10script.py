##### Chapter 10 #####

print( (1,4,5) < (1,4,5) )

print((1,),(1,2),(1,2,3),(1,2,3,4))

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname, domain)


d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)


### Exercise 1 / Exercise 2

print('\n Exercise 1 / Exercise 2 \n')

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	emailcount = dict()
	
	hourcount = dict()

	for line in file_handle:
		
		# For lines that contain contact information, track address
		# and increment our count of emails from this person.
		
		if line[:5] == 'From ':
			
			words = line.split()
			
			# For reference, words will have this format in every case :
			#['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
			
			address = words[1]
			
			emailcount[address] = emailcount.get(address,0) + 1
			
			time = words[5]
			
			hour = time[0:2]
			
			hourcount[hour] = hourcount.get(hour,0) + 1
			
	lst1 = list()
	
	for key,value in list(emailcount.items()):
	
		lst1.append((value, key))
		
	lst1.sort(reverse = True)
	
	# The first element of lst is a tuple (number, email address)
	# for the highest frequency email contact, we want the address
	# to print from the dictionary so that our formatting matches
	# the books.
	
	high_freq_key = lst1[0][1]
	
	print(high_freq_key, emailcount[high_freq_key])
	
	lst2 = list()
	
	for key,value in list(hourcount.items()):
	
		lst2.append((key,value))
	
	lst2.sort()
	
	for elmnt in lst2:
	
		print(elmnt[0], elmnt[1])



except:

	print('File cannot be opened : ' + file_name)
	
	
### Exercise 3

print('\n Exercise 3 \n')

import string

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	lettercount = dict()
	
	total = 0
	
	for line in file_handle:
	
		#line = line.translate(str.maketrans('', '', string.punctuation))
		#line = line.translate(str.maketrans('', '', '0123456789'))
		#line = line.translate(str.maketrans('', '', '»¿ï'))
		line = line.lower()
		words = line.split()

		for word in words:
		
			for letter in word:
				
				if letter in 'abcdefghijklmnopqrstuvwxyz':
				
					total = total + 1
					lettercount[letter] = lettercount.get(letter,0) + 1	

	lst = list()
	
	for key,value in list(lettercount.items()):
	
		frequency = value / total
		lst.append((key,frequency))
	
	lst.sort()
	
	for elmnt in lst:
	
		print(elmnt[0], elmnt[1])
		
except:
	
	print('File cannot be opened : ' + file_name)

