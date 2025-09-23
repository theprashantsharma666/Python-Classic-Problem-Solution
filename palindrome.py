# PALINDROME
'''n = input()
a = int(n)
if a < 0:
    print("Given number is not Palindrome Number")
else:
    b = int(n[::-1])
    if n == b:
        print("Given number is Palindrome Number")
    else:
        print("Given number is not Palindrome Number")'''

# FOR CHECKING IS STRING PALINDROME 

n = input().casefold()
a = len(n)
if a <= 1 :
    print("Given string is not Palindrome String")
else:
    b = n[::-1]
    if n == b :
        print("Given string is Palindrome String")
    else:
        print("Given string is not Palindrome String")

