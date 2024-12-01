# Nested Lists
'''Given the names and grades for each student in a class of n students,
store them in a nested list and print the name(s) of any student(s) having
the second lowest grade. Note: If there are multiple students with the second
lowest grade, order their names alphabetically and print each name on a new line.'''

n = int(input()) # number of students
l = []
while n>0: # asks for name and grade of each student and stores them in a list
    student = input()
    grade = float(input())
    sl = [student,grade]
    l.append(sl)
    n -= 1

increasing_grade_list = sorted(l, key = lambda x: x[1]) # create new list ordered by grade
grades = sorted(set(x[1] for x in increasing_grade_list)) # excludes duplicates
second_lowest = grades[1] # store the second lowest grade at a variable
names = [] #creates list of names
for e in l: # stores first elements (names) of the original list if second lowest grade appears with them
    if second_lowest in e:
        names.append(e[0])

names.sort() # order list of names alphabetically 
for name in names: # prints name by name
    print(name)
