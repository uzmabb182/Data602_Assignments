# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements
# and else statements print the user a message recommending a meal. For example, if the meal was breakfast,
# you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.


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

hours_worked = float(input("Please enter the number of hours worked: "))
pay_rate = float(input("Please enter the pay rate per hour: "))
fix_hours = 20

if hours_worked > fix_hours:
    extra_hours = hours_worked - fix_hours
    extra_hours_pay_rate = pay_rate * 1.5
    extra_hours_pay = extra_hours * extra_hours_pay_rate
    gross_pay = (fix_hours * pay_rate) + extra_hours_pay
    print("Your gross pay including extra hours is: " + "$" + str(gross_pay))
else:
    gross_pay = fix_hours * pay_rate
    print("Your gross pay is: " + "$" + str(gross_pay))


# 3: Write a function named times_ten. The function should accept an argument
# and display the product of its argument multiplied times 10.

def times_ten(num):
    product_ten = num * 10
    print("The product of number times ten is: " + str(product_ten))


number = int(input("Please enter the number: "))
# Calling the function

times_ten(number)

# Q4: Find the errors, debug the program, and then execute to show the output.

def show_calories(calories1, calories2):
    print("The total calories you ate today"+ ", " + str('{:.2f}'.format(calories1 + calories2)))

def main():
    calories1 = int(input("How many calories are in the first food?"))
    calories2 = int(input("How many calories are in the first food?"))
    show_calories(calories1, calories2)


if __name__ == "__main__":
    main()

# Q5: Write a program that uses any loop (while or for) that calculates
# the total of the following series of numbers:

a = 1
b = 30
sum_fraction = 0

while b >= 1:
    print(a)
    print(b)

    fraction = a/b
    print(fraction)
    a += 1
    b -= 1

    sum_fraction = sum_fraction + fraction
    print(sum_fraction)


print("The total sum of the series of fractions is: " + str('{:.2f}'.format(sum_fraction)))

# Q6: Write a function that computes the area of a triangle given its base and height.
# For example, if the base was 5 and the height was 4, the area would be 10.

def area_triangle(base, height):
    area = round((1/2) * (base * height))
    print("The area of a triangle is: " + str(area))


base = int(input("Enter the base of a triangle: "))
height = int(input("Enter the height of a triangle: "))

# Calling the function
area_triangle(base, height)