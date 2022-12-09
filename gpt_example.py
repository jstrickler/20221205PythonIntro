#open the file
file = open('DATA/presidents.txt', 'r')

#create a dictionary to store the states
states = {}

#loop through each line in the file
for line in file:
	#split the line
	words = line.split()
	#get the state
	state = words[-1]
	#check if the state is in the dictionary
	if state in states:
		#if it is, increment the count
		states[state] += 1
	else:
		#if it isn't, add it to the dictionary
		states[state] = 1

#print the results
for state in states:
	print(state + ": " + str(states[state]))

#close the file
file.close()
