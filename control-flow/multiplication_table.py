# multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Generating and print multiplication table using a for loop

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")