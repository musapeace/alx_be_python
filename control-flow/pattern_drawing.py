# drawing pattern with nested loop
size = int(input("Enter the size of the pattern: "))

# Initializing the row counter
row = 0

# Use a while loop to iterate through each row of the pattern
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1