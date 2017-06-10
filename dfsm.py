"""
The is a DFSM with language set of a, b, c
where w contains the substring 'bbc' but not as
a prefix. Minimum examples are 'abbc', 'bbbc', 'cbbc'
This program reads in a list of 2 files and process'
each string in the file and outputs if the string is 
part of the language with 'accept' or not with 'reject'
"""
#w contains bbc but not as a prefix: ex: abbc, bbbc, cbbc
#defining the language set
L = ['a', 'b', 'c']

rej = 0		#to count the rejected strings
acc = 0		#to count the accepted strings

#defining the state machine using dictionaires
FSM = 	{
		"S"  : { 'a' : "Q1", 'b' : "Q4", 'c' : "Q1", '\n' : "S"  }, 
		"Q1" : { 'a' : "Q1", 'b' : "Q2", 'c' : "Q1", '\n' : "Q1" },
		"Q2" : { 'a' : "Q1", 'b' : "Q3", 'c' : "Q1", '\n' : "Q2" },
		"Q3" : { 'a' : "Q1", 'b' : "Q3", 'c' : "F",  '\n' : "Q3" },
		"Q4" : { 'a' : "Q1", 'b' : "Q5", 'c' : "Q1", '\n' : "Q4" },
		"Q5" : { 'a' : "Q1", 'b' : "Q3", 'c' : "T",  '\n' : "Q5" },
		"T"  : { 'a' : "T",  'b' : "T",  'c' : "T",  '\n' : "T"  },
		"F"  : { 'a' : "F",  'b' : "F",  'c' : "F",  '\n' : "F"  }
	}

print "Jose C. Ramirez\n"

#array of files to process
files = ["mydata.txt", "F13.txt"]

#process for each file in the files array
for infile in files:

	#if the file is Halversons Data
	if (infile == "F13.txt"):
		print "\nHalverson\'s Data\n"

	#opening a file
	f = open(infile)

	#setting the Start state for every string
	state = "S"

	#process when reading a line
	for line in f:

		#process for each character in the line
		#for every character in the line
		for char in line:
			#first check if the character is valid
			if (char not in L and char != '\n' and char != ' '):
				#if the character is not in the language reject the string
				print "%-20s %15s" % (line[:-1], "Rejected")

				#increment the number of strings rejected
				rej += 1
				#terminate loop for the current string
				break

			#if the character is in the set
			else:
				#if it is not the last character
				if (char != '\n'):
					#consume the character to the next state
					state = FSM[state][char]

				#if it is the last character
				else:
					#check if it is in the Final state
					if (state == "F"):
						#accept the string if in the final state
						print "%-20s %15s" % (line[:-1], "Accepted")

						#increment number of accepted strings
						acc += 1

					#otherwise reject if it is in a rejecting state
					else:
						#if the line is empty, reject
						if (line == '\n'):
							print "%-20s %15s" % ("EMPTY STRING", "Rejected")
							print

						#if the line is not empty print
						else:
							#print the string and reject
							print "%-20s %15s" % (line[:-1], "Rejected")

							#increment the number of rejected stings
							rej += 1

		#reset the start state for the next line in the file
		state = "S"

	print "-"*40
	print "Number of Accepted strings: ", acc
	print "Number of Rejected strings: ", rej
	print "-"*40
	acc = 0
	rej = 0
	#closing the file
	f.close()
