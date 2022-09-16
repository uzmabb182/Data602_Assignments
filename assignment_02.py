# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
# print(numbers[1:-5])
# Can you debug and fix the output? The code should return the entire list

print(numbers[0:5])

# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
sales = []
# print(len(days))
# total_sales = 0
for i in range(0, len(days)):
   # print(days[i])
   sale = int(input(f"Please enter the sales for {days[i]}: "))
   # total_sales = total_sales + sale
   sales.append(sale)
   total_sales = sum(sales)
# Print the sales list
print(f"The total sales for the week is ${total_sales}")

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.

travel_list = []

count = 5

for i in range(count):
    choices = str(input(f"Enter the places you would like to travel: "))
    travel_list.append(choices)

# Print the original list
print(travel_list)

# Sorting the list
travel_list.sort()
print("The sorted list is: " + str(travel_list))

# Print the reverse
travel_list.sort(reverse=True)
print("The reverse list is: " + str(travel_list))

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time

student_dict = {}
room_dict = {}
inst_dict = {}
time_dict = {}

# Take user input for creating three dictionaries
for i in range(5):
    course = str(input("Please enter the course number: "))
    room = str(input("Please enter the room number: "))
    instructor = str(input("Please enter the instructor name: "))
    time = input("Please enter the class time: ")

    room_dict[course] = room
    inst_dict[course] = instructor
    time_dict[course] = time

print(room_dict)
print(inst_dict)
print(time_dict)

# Assign three sub dictionaries to a dictionary

student_dict["room_info"] = room_dict
student_dict["inst_info"] = inst_dict
student_dict["time_info"] = time_dict

print(student_dict)

course_num = str(input("Please enter the course number: "))

if course_num in student_dict["room_info"]:
    print("The course room number is: " + str(student_dict["room_info"][course_num]))
else:
    print("The room number is not assigned")

if course_num in student_dict["inst_info"]:
    print("The course instructor name is: " + str(student_dict["inst_info"][course_num]))
else:
    print("The course instructor is not assigned")

if course_num in student_dict["time_info"]:
    print("The course timing is: " + str(student_dict["time_info"][course_num]))
else:
    print("The course timing is not assigned")

# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# delete an existing name and email address.

person_dict = {}

# Take user input for creating dictionary
for i in range(5):
    name = str(input("Please enter the name: "))
    email = str(input("Please enter the email: "))
    # Assigning the key, a value
    person_dict[name] = email
  
print(person_dict)

# Look up a person’s email address

lookup_name = str(input("Please enter the lookup_name for email address: "))

if lookup_name in person_dict:
    print("The person email address is: " + str(person_dict[lookup_name]))
else:
    print("The person name is not found")

# Add a new name and email address

name = str(input("Please enter new person's name: "))
email = str(input("Please enter new person's email: "))

person_dict[name] = email
print(person_dict)

# change an existing email address
lookup_name = str(input("Please enter the lookup_name for changing existing email address: "))

if lookup_name in person_dict:
    email = lookup_name + "bb@gmail.com"
    person_dict[lookup_name] = email

print(person_dict)

 # delete an existing name and email address
lookup_name = str(input("Please enter the lookup_name for deleting existing name and email: "))
 
if lookup_name in person_dict:
    del(person_dict[lookup_name])


print(person_dict)