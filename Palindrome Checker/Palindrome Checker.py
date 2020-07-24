#Palindrome Checker
###Kunal Saboo
###7/23/2020

#Collect Input
inpX = input('Enter your word: ') #Ask for input from cmd
inp = inpX.lower() #Make the input lowercase
isPalin = True #Initialize true variable for palindrome
i = 0 #Counter variable
while i< len(inp)/2: #While loop iterating through half or one less than half if its odd
    if inp[i] == inp[-1*(i+1)]: #Checks if the current index is equal to the same spot coming backwards using negative indexing
        pass #If it meets the palindrome condition do nothing
    else: #If it violates the palindrome condition
        isPalin = False #Make it false
    i=i+1 #iterate through the counter
#Print result
if isPalin:
    print(inpX + " is a palindrome.")
else:
    print(inpX + " is not a palindrome.")