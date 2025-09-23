# Hollow Pyramid Pattern
n = int(input("Enter size n: "))

for i in range(1, n + 1):
    # Leading spaces
    spaces = ' ' * (n - i)
    
    # Determine stars for each row
    if i == 1 or i == n:
        stars = '*' * (2 * i - 1)  # Full stars for top and bottom row
    else:
        stars = '*' + ' ' * (2 * i - 3) + '*'  # Hollow sides for middle rows
    
    # Print the row
    print(spaces + stars)
