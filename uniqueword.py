# PRINT UNIQUE WORD IN STRING

a = input().casefold()
res = ""
for i in a : 
    if i not in res:
       res +=i
print(res)