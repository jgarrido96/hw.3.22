
# 1. The Calculator App

# Task 1: Create functions for each arithmetic operation.

def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)

def mul(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    print(num1 // num2)

def choose():
    op = input("Choose an operation: (add, substract, multiply, divide) ")
    num1 = int(input("Choose a number: "))
    num2 = int(input("Choose another number: "))
    if op == "add":
        try:
            add(num1, num2)
        except:
            pass
    if op == "substract":
        try:
            sub(num1, num2)
        except:
            pass
    if op == "multiply":
        try:
            mul(num1, num2)
        except:
            pass
    if op == "divide":
        try:
            div(num1, num2)
        except ZeroDivisionError:
            print("You can't do that!!")

choose()

print('\n')

# 2. The shopping list maker

my_list = []
def shopping():
    while True:
        user_input = input("What would you like to add to your shopping list today? Type 'next' to move on. ")
        if user_input == "next":
            break
        my_list.append(user_input)

shopping()

def show_list():
    print("Here's your list!!")
    for list  in my_list:
        print(list)

def unlist():
    while True:
        user_input = input("What would you like to remove? Type 'next' to move on. ")
        if user_input == "next":
            break
        try:
            my_list.remove(user_input)
        except:
            print("Uh oh, item not found!")
        
unlist()

show_list()

print('\n')

# 3. Grade Analyzer

grades = [97, 65, 81, 57, 95, 48, 83, 69, 77, 50]
def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

def grades_average(grades):
    return grades_sum(grades) / float(len(grades))

print(grades_average(grades))

def highest_grade():
    print(max(grades))

def letter_grade():
    while True:
        for grade in grades:
            if grade >= 90:
                print(f"You have an A with a score of {grade}!")
            elif grade >= 80:
                print(f"You have a B with a score of {grade}!")
            elif grade >= 70:
                print(f"You have a C with a score of {grade}.")
            elif grade >= 60:
                print(f"You have a D with a score of {grade}.")
            else:
                print(f"Woof, you got an F.")
        break
                
highest_grade()

letter_grade()