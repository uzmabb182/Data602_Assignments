#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95
 
# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))



# Calculate the average test score.
# Add the bracket around the three variables
average = (test1 + test2 + test3 )/ 3
# Print the average.
print('The average score is', str(average))
# If the average is a high score,
# congratulate the user.

if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')

# To find the datatype of "average"
print(type(average))

format_float = "{:.2f}".format(average)
print(format_float)

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

def area_calc(length, width):
    area = length * width
    return area

# Taking the input  for two rectangles in a loop
for n in range(2):
    length = int(input(f"Enter the length of a rectangle {n+1}: "))
    width = int(input(f"Enter the width of a rectangle {n+1}: "))

    # Calling the function
    rectangle_area = area_calc(length, width)
    print(f"The area of rectangle {n+1} is: " + str(rectangle_area))
#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

# Asking for the name of the user

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

print(f"Happy birthday, {name}! You ae {age} years old today!")


