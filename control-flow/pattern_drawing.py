# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))
# Use nested loops to print a square pattern
for i in range(size):
    for j in range(size):
        print('*', end=' ')
    print()
    # Move to the next line after each row
