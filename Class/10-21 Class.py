
x = 5

print("Now enter another number")
# y = input()
y = 6

# print(x, ' ', y)

# Checks if one value is greater than another
if y > x:
    print('y is greater than x')

# Check if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Check if x != 1
if x != 1:
    print("x is not equal to 1")

# Checks for two conditions to be met using "end"
if x > 2 and y > 3:
    print("Both values returned true")

# Checks if etiher of two conditions is met
if x > 2 or v > 3:
    print("One or more of the statements were true")

# Nested if statements
if x > 2:
    if y > 3:
        print("Both values returned true")

# Loop through a range of numbers (0 through 4)
for i in range(5):
    print (i)

# Loop through a range of numbers (2 through 6 -  yes6! Up to, but not including 7)
for i in range (2,7):
    print (i)

# Iterate through letters in a string
for i in "hello":
    print (i)

# Iterate through a list
mylist = [10,20,30,40,50]
for i in mylist:
    print (i)

# Loop while a condition is being met
i = 0
while i < 5:
    print (i)
    i = i + 1

# Reverse
i = 0
while i < 5:
    i = i + 1
    print (i)

# Specify the file to write to
file_outpath = ""

# -----------------------

#Specify the file to write to
file_outpath = "Employee_Data.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file_outpath, 'w') as textfile:

    # Create a variable to hold text inside parentheis
    employee_data = "\nLast Name\tFirst Name\tEID\n" + "-----------------\n"

    #Write the text to the file
    textfile.write(employee_data)

    # Print the data to the screen
    print(employee_data)

# Can also use "append" mode
with open(file_outpathm 'a') as textfile:

    # Create a variable tp hold the text inside parenthesis
    employee_data = "Wong\t\Aaron\t\AB123\n"

    # Write the text to the file.
    textfile.write(employee_data)

    # Print the data to the screen
    print(employee_data)