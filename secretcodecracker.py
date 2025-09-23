# SECRET CODE CRACKER

n = input()
y = n.split()
r = ""
for i in y:
    a = int(i)
    if 1<=a<=26:
        r+=chr(a+64)
    elif 27<=a<=52:
        r+=chr(a+70)
print(r)
