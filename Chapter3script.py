############ Chapter 3 ###############

# Exercise 1



hours = float(input('Enter hours : \n'))
rate = float(input('Enter rate : \n'))

if hours > 40:
	overtime_hours = hours - 40
	pay = 40*rate + 1.5*rate*overtime_hours
else:
	pay = hours*rate

print('Pay : ' + str(pay))


# Exercise 2


try:

	hours = float(input('Enter hours : \n'))
	rate = float(input('Enter rate : \n'))
	
	if hours > 40:
		overtime_hours = hours - 40
		pay = 40*rate + 1.5*rate*overtime_hours
	else:
		pay = hours*rate

	print('Pay : ' + str(pay))
except:
	print('Error, please enter numeric input')
	
	


# Exercise 3


try:
	score = float(input('Enter score between 0 and 1 inclusive : \n'))
	
	if score >= 0 and score <= 1:
		if score >= 0.9:
			grade = 'A'
		elif score >= 0.8:
			grade = 'B'
		elif score >= 0.7:
			grade = 'C'
		elif score >= 0.6:
			grade = 'D'
		elif score >= 0:
			grade = 'F'
	
	print(grade)

except:
	print('Bad score')

############# Going back to Chapter 4 Exercises ###########


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

