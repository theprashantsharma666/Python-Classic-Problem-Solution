# Diamond Pattern
n = int(input("Enter n : "))
# Top half
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Bottom half
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
