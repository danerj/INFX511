#### Chapter 7 ####

# Exercise 1

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
except:

	print('File cannot be opened : ' + file_name)

for line in file_handle:

	print(line.upper())
	

	
# Exercise 2 / Exercise 3

file_name = input('Enter the file name: ')

try:

	file_handle = open(file_name)
	
	count = 0
	
	total = 0

	for line in file_handle:
		
		if line.find('X-DSPAM-Confidence:') == -1:
		
			continue
			
		else:
		
			count = count + 1
			
			number = float(line[line.find(':')+1:])
			
			total = total + number
		
	average = total/count
	
	print('Average Spam Confidence = ' + str(average))
	
except:
	
	if file_name == 'na na boo boo':
	
		print('NA NA BOO BOO TO YOU - You have been punk\'d!')
		
	else:
	
		print('File cannot be opened : ' + file_name)
	
