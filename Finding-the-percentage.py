# finding the percentage
'''The provided code stub will read in a dictionary containing key/value 
pairs of name:[marks] for a list of students. Print the average of the 
marks array for the student name provided, showing 2 places after the decimal.'''

n = int(input()) # number of students
marks = {} # creates dictionary
for _ in range(n): # asks for data of each student
    name_and_grades = input().split() # splits data and stores it in a list
    name = name_and_grades[0] # sets first element of the list as name
    grades = list(map(float, name_and_grades[1:])) # sets other elements of the list as grades
    marks[name] = grades # stores data into dictionary, relating keys name and grades
query_name = input() # student to see average
if query_name in marks:
    average = sum(marks[query_name]) / 3 # sets variable with sum of grades of specific student, divided by 3
    print(f'{average:.2f}') #prints average with .2 decimal
