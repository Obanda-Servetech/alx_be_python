# multiplication_table.py

# Prompt the user to input a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

