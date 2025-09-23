# ANAGRAM STRING

a = input().casefold()
sort1 = sorted(a)
b = input().casefold()
sort2 = sorted(b)
if (sort1 == sort2):
    print("True")
else :
    print("False")