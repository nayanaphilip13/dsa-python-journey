# Variable - Is a box that having a name and holds a value
name = "Nayana"
age = 25
city = "Kerala"
# print() is used to output something
print(name)
print(age)
print(city)

# Lists - List is a collection of items, kept in an order and in a single variable
# ex: marks = [88, 34, 56]
# And index starts from 0 not 1.
marks = [88, 45, 92, 67, 100]
print(marks[0])   # prints 88
print(marks[2])   # prints 92
print(marks[4])   # prints 100

# For calculating length of a list ->len(marks)
# For loop for i in range(len(marks)):
    #print(marks[i])
marks = [88, 45, 92, 67, 100]
print("Total Marks:", len(marks))
for i in range(len(marks)):
    print("Mark at position", i ,"is", marks[i])

#if/else Loops
age = 20

if age >= 18 :
    print("Can cast Vote")
else :
    print("Cant Vote")

marks = [88,45,92,67,100]
for i in range(len(marks)):
    if marks[i] >= 50:
        print(marks[i],"→ Pass ✅")
    else :
        print(marks[i], "→ Fail ❌")

marks = [33, 78, 55, 20, 90, 48]
# And add one more condition using elif (which means "else if"):

# If marks >= 75 → print "Distinction 🏆"
# elif marks >= 50 → print "Pass ✅"
# else → print "Fail ❌"

for i in range(len(marks)):
    if marks[i] >= 75 :
        print("Distinction 🏆")
    elif marks[i] >= 50 :
        print ("Pass ✅")
    else :
        print("Fail ❌")

#Functions 
def greet(name):
    print("Welcome", name)

greet("Nayana")
greet("Nish")

# def → means "I am creating a function"
# greet → the name of the function (you choose this)
# (name) → the input you give it (called a parameter)
# Everything indented inside is what the function does

# Function to calculate and return an answer
def add(a,b):
    result = a+b
    return result

answers = add(10, 30)
print(answers)
# return means "send this answer back"
# answer stores whatever the function returns

def check_result(marks):
    for i in range(len(marks)):
        if marks[i] >= 75 :
            print("Distinction 🏆")
        elif marks[i] >= 50 :
            print ("Pass ✅")
        else :
            print("Fail ❌")

my_marks = [33, 78, 55, 20, 90, 48]
check_result(my_marks)

# Write a function called find_max that:

# Takes a list of numbers as input
# Loops through the list
# Finds and prints the biggest number

def find_max(numbers):
    biggest = 0
    for i in range(len(numbers)):
        if numbers[i] > biggest:
            biggest = numbers[i]  # update biggest
    print("Highest Number is:", biggest)  # print AFTER loop ends

numbers_list = [20, 10, 5, 60, 56]
find_max(numbers_list)

#Dictionary -> stores in key value pair
student = {
    "name" : "Nayana",
    "age" : 32,
    "city" : "Bangalore"
}
#Access in dictionary
student["name"] = "Nayana"
print(student["age"]) 
#loop in dictionary
for key in student:
    print(key, "->", student[key])

#List of dictionaries
students = [
    {"name": "Nayana", "marks": 92},
    {"name": "Priya",  "marks": 45},
    {"name": "Anjali", "marks": 78}
]
for i in range(len(students)):
    print(students[i]["name"], "got", students[i]["marks"])

#Challenge
# Create a list of 3 students with name and marks. Loop through and print:

# If marks >= 75 → "Distinction 🏆"
# If marks >= 50 → "Pass ✅"
# Else → "Fail ❌"

# Like this output:

# Nayana → Distinction 🏆
# Priya → Fail ❌
# Anjali → Pass ✅


students = [
    {"name": "Nayana", "marks": 92},
    {"name": "Priya",  "marks": 45},
    {"name": "Anjali", "marks": 68}
]

for i in range(len(students)):
    if(students[i]["marks"] >= 75):
        print(students[i]["name"], "→ Distinction 🏆")
    elif(students[i]["marks"] >= 50):
        print(students[i]["name"], "→ Pass ✅")
    else:
        print(students[i]["name"], "→ Fail ❌")

#String Operations
# 1. Join two strings together (called concatenation)
# name = "Nayana"
# city = "Kerala"
# print(name + " is from " + city)
# prints: Nayana is from Kerala

# 2. Find the length of a string
# name = "Nayana"
# print(len(name))   # prints 6

# 3. Convert to uppercase / lowercase
# name = "Nayana"
# print(name.upper())   # NAYANA
# print(name.lower())   # nayana

# 4. Check if a word is inside a string
# sentence = "I love Python programming"
# print("Python" in sentence)   # prints True
# print("Java" in sentence)     # prints False

# 5. Split a sentence into a list of words
# sentence = "I love Python programming"
# words = sentence.split(" ")
# print(words)
# prints: ['I', 'love', 'Python', 'programming']

# 6. Access individual letters (just like list index!)
# name = "Nayana"
# print(name[0])   # N
# print(name[1])   # a
# print(name[2])   # y


# 🎯 Mini Challenge
# Write a function called describe_student that:
# Takes a student dictionary as input
# Prints a sentence describing them
# Expected output:
# NAYANA is from Kerala and scored 92 marks
# Start like this:

# def describe_student(student):
#     # your code here

# student = {"name": "Nayana", "city": "Kerala", "marks": 92}
# describe_student(student)

# Hints:
# Use .upper() for the name
# Use + to join strings together
# To join a number with a string, wrap it like str(marks) — this converts number to text


def describe_student(student):
    print(student["name"].upper() + " is from " +  student["city"] + " and scored " + str(student["marks"]) + " marks")

student = {"name": "Nayana", "city": "Kerala", "marks": 92}
describe_student(student)