##### Chapter 9 #####


### Exercise 1

print('\n Exercise 1 \n')

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	word_list = dict()
		
	for line in file_handle:

		words = line.split()
			
		for word in words:
			
			word_list[word] = 1
		
	print(word_list)


except:

	print('File : ' + file_name + ' does not work')


###

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

lst = list(counts.keys())

print(lst)

lst.sort()

for key in lst:
	print(key, counts[key])
	
import string

print(string.punctuation)

### 

### Exercise 2 / Exercise 3 / Exercise 4 / Exercise 5

print('\n Exercise 2 / Exercise 3 / Exercise 4 / Exercise 5 \n')

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	daycount = dict()
	
	emailcount = dict()
	
	domaincount = dict()

	for line in file_handle:
		
		if line[:5] == 'From ':
			
			words = line.split()
			
			day = words[2]
			
			daycount[day] = daycount.get(day,0) + 1
			
			address = words[1]
			
			emailcount[address] = emailcount.get(address,0) + 1
			
			atpos = address.find('@')
			
			domain = address[atpos+1:]
			
			domaincount[domain] = domaincount.get(domain,0) + 1
	
	
	maximum = 0
	
	for key in emailcount:
	
		# Note that this does not handle the case of tied values
		
		if emailcount[key] > maximum:
		
			highest_frequency_key = key
			
			maximum = emailcount[highest_frequency_key]
	

	print(daycount)
	
	print(emailcount)
	
	print(highest_frequency_key, str(emailcount[highest_frequency_key]))
	
	print(domaincount)
	
	
except:

	print('File cannot be opened : ' + file_name)
	



