# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))
# Use nested loops to print a square pattern
for i in range(size):
    for j in range(size):
        print('*', end=' ')
    print()
    # Move to the next line after each row
def main():
    while True:
        try: user_input = int(input("Enter a positive integer: "))
        except ValueError:
                print("Invalid input. Please enter a positive integer.")
                if __name__ == "__main__": main()

    if user_input > 0: draw_square_pattern(user_input)


            
