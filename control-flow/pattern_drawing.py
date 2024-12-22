# pattern_drawing.py

# Prompt the user to input the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Initialize a counter for rows
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print asterisks (*) in each row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    row += 1

