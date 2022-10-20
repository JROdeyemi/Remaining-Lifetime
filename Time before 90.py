#Create the prompt
Age = input('How old are you? \n ')

#Turn the received answer to an integer
Agenumber = int(Age)

#Calculate Number of days left using 365days/year
Days = (365 * 90) - (365 * Agenumber)

#Calculate Number of weeks left using 52weeks/year
Weeks = (52 * 90) - (52 * Agenumber)

#Calculate number of months left using 12months/year
Months = (12 * 90) - (12 * Agenumber)

#Print out remaining time left
print(f'You have {Days} days left, {Weeks} weeks, and {Months} months left.')





