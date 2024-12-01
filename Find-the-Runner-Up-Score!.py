# Find the Runner-Up Score!

'''Given the participants' score sheet for your University Sports Day,'''
'''you are required to find the runner-up score. You are given  scores.'''
'''Store them in a list and find the score of the runner-up.'''

n = int(input()) # number of scores
s = input() # scores input as string (2 4 6 6 3)
s = s.split() # it turns the string input into an iterable object
l = []
n -= 1 # n will be used as element's position
while n >= 0: # adds elements one-by-one to the list
    l.append(int(s[n]))
    n -=1
l.sort() # organizes list by element's value
L = list(set(l)) # creates a new list, excluding the repeated values
print(L[-2]) # prints the runner-up score
