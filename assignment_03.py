# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements
# and else statements print the user a message recommending a meal. For example, if the meal was breakfast,
# you could say something like, “How about some bacon and eggs?”
#The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.


selection = input("Please enter the meal you like to order from breakfast, lunch or dinner: ")

if selection == "breakfast":
        print("How about some bacon and eggs?")
elif selection == "lunch":
        print("How about some grilled chicken with salad?")
elif selection == "dinner":
        print("How about some shrimp scampi with soup?")
else:
        print("Sorry we don't serve that")


# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay,
# including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them
# 1.5 times their regular hourly pay rate for all hours over 20.
# You should take in the user’s input for the number of hours worked, and their rate of pay.


# 3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.


# Q4: Find the errors, debug the program, and then execute to show the output.

def main()
      Calories1 = input( "How many calories are in the first food?")
      Calories2 = input( "How many calories are in the first food?")
      showCalories(calories1, calories2)

def showCalories()
   print(“The total calories you ate today”, format(calories1 + calories2,.2f))

# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
         1/30 + 2/29 + 3/28 ............. + 30/1

# Q6: Write a function that computes the area of a triangle given its base and height.
The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT

# For example, if the base was 5 and the height was 4, the area would be 10.
triangle_area(5, 4)   # should print 10
