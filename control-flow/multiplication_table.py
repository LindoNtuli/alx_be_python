# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))
# Use a for loop to print the multiplication table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
