# Q1: Create a class called BankAccount that has four attributes:
# bankname, firstname, lastname, and balance.
# The default balance should be set to 0.
# In addition, create ...
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
# in your withdrawal() method.
# ● Use the __str__() method in order to display the bank name, owner name,
# and current balance.
# ● Make a series of deposits and withdrawals to test your class.


class BankAccount:

    # Defining the attributes in a constractor
    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    # Declaring methods
    def deposit(self):
        amount_deposit = int(input("Enter the amount you want to deposit: "))
        self.balance = self.balance + amount_deposit
        return self.balance

    def withdrawal(self):
        amount_withdrawal = int(input("Enter the amount you want to withdraw: "))
        if amount_withdrawal < self.balance:
            self.balance = self.balance - amount_withdrawal
        else:
            print("Sorry your withdrawal amount exceed the available balance.")

        return self.balance

    def __str__(self):
        return "The bank name is: {}, the owner name is: {} {}, and the current balance is: ${}".format(self.bankname, self.firstname, self.lastname,  self.balance)


obj1 = BankAccount('chase', 'Uzma', 'Zafar')
total_balance = obj1.deposit()

# looping for depositing the amount
response = input("Do you want to deposit the amount? (yes/no): ")
while response == "yes":
    total_balance = obj1.deposit()
    print("Your total balance is: " + str('${}'.format(total_balance)))
    response = input("Do you want to deposit the amount? (yes/no): ")
# print with $ sign format
print("Your total balance is: " + str('${}'.format(total_balance)))

# Looping for withdrawing the amount
response = input("Do you want to withdrawal the amount? (yes/no): ")
while response == "yes":
    total_balance = obj1.withdrawal()
    print("Your current balance is: " + str('${}'.format(total_balance)))
    response = input("Do you want to withdrawal the amount? (yes/no): ")
# print with $ sign format
print("Your total balance is: " + str('${}'.format(total_balance)))

# Calling the __str__ function
print(obj1.__str__())


# Q2: Create a class Box that has attributes length and width that takes values for length
# and width upon construction (instantiation via the constructor)

import math

class Box:
    asterisk = '* '

    # Defining the attributes in a constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # A method called render() that prints out to the screen a box made with asterisks of
    # length and width dimensions.
    def render(self):
        while self.length > 0:
            print(self.asterisk * self.width)
            self.length = self.length-1

    # A method called invert() that switches length and width with each other
    def invert(self):
        a = self.length
        b = self.width
        self.length = b
        self.width = a
        print("The box with switched length and width")
        while self.length > 0:
            print(self.asterisk * self.width)
            self.length = self.length-1

    # Methods get_area() and get_perimeter() that return appropriate geometric calculations
    def get_area(self):
        area = self.length * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        return perimeter

    # A method called double() that doubles the size of the box. Hint: Pay attention to return
    # value here
    def double(self):
        self.width = 2 * self.width
        return self.length * self.width

    # Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
    # their respective lengths and widths are identical.
    def __eq__(self, other):
        return (self.length, self.width) == (other.length, other.width)

    # A method print_dim() that prints to screen the length and width details of the box
    def print_dim(self):
        print("The length of the box is: " + str('{} cm'.format(self.length)))
        print("The width of the box is: " + str('{} cm'.format(self.width)))

    # A method get_dim() that returns a tuple containing the length and width of the box
    def get_dim(self):
        return self.length, self.width

    # A method combine() that takes another box as an argument and increases the length
    # and width by the dimensions of the box passed in
    def combine(self, length, width):
        self.length = self.length + length
        self.width = self.width + width
        print("The increased length of the box is: " + str('{} cm'.format(self.length)))
        print("The increased width of the box is: " + str('{} cm'.format(self.width)))

    # A method get_hypot() that finds the length of the diagonal that cuts through the middle
    def get_hypot(self):
        diagonal = round(math.sqrt((self.width**2) + (self.length**2)), 4)
        return diagonal


x = int(input("Please enter the length of a box: "))
y = int(input("Please enter the width of a box"))
# Creating object instance
obj_render = Box(x, y)
obj_invert = Box(x, y)
obj_area = Box(x, y)
obj_perimeter = Box(x, y)
obj_double = Box(x, y)
obj_dim = Box(x, y)
obj_dimension = Box(x, y)
obj_combine = Box(x, y)
obj_diagonal = Box(x, y)

# Calling the methods
obj_render.render()
obj_invert.invert()
obj_dim.print_dim()
obj_combine.combine(2, 3)
obj_diagonal.get_hypot()

dim = obj_dimension.get_dim()
print("The dimensions of the box in a tuple is: " + str('{} cm'.format(dim)))

calc1 = obj_area.get_area()
print("The area of a box is: " + str('{} cm'.format(calc1)))

calc2 = obj_perimeter.get_perimeter()
print("The perimeter of a box is: " + str('{} cm'.format(calc2)))

calc3 = obj_double.double()
print("Double the area of a box is: " + str('{} cm'.format(calc3)))

calc4 = obj_double.double()
print("The diagonal of a box is: " + str('{} cm'.format(calc4)))

# Instantiating the box objects
obj_box1 = Box(5, 10)
obj_box2 = Box(3, 4)

# After Implement __eq__  two boxes are compared using ==. Two boxes are equal if
# their respective lengths and widths are identical.
print("The comparison of two boxes is: " + str(obj_box1 == obj_box2))

# Instantiating three boxes objects
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

# Print dimension info for each using print_dim()
box1.print_dim()
box2.print_dim()
box3.print_dim()

# Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
# screen accordingly

print("The comparison of two boxes is: " + str(box1 == box2))
print("The comparison of two boxes is: " + str(box1 == box3))

# Combine box3 into box1 (i.e. box1.combine())
box1.combine(3, 4)

# Double the size of box2
box2.double()

# Combine box2 into box1
box2.combine(5, 10)