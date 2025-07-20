# pattern_drawing.py

# Ask user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: while loop for each row
while row < size:
    # Inner loop: for loop for printing stars in each row
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
