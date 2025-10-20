# LIST

# SECOND HIGHEST SCORE 
'''lst = eval(input())
b = set(lst)
a = list(b)
a.sort()
if len(a)<2:
    print("No Highest Second Score ")
else:
    print(a[-2])'''

# NUMBER MISSING FROM THE SERIES
'''a = eval(input())
n1 = a[0]
n2 = a[-1]
suma = 0
sum = 0
for i in range(n1,n2+1):
    sum+=i 
for i in a :
    suma+=i
b = sum - suma
print(b)'''

#  ROTATE A LIST BY K ELEMENTS
'''a,k = input().rsplit(',',1)
a = eval(a)
k = int(k)
k = k % len(a)             # Normalize k to avoid out-of-range slicing
f = a[-k:] + a[:-k]        # Perform right rotation
print(f)'''

# EXACTLY ONE SOLUTION 
'''a,k = input().rsplit(',',1)
a = eval(a)
k = int(k)
lst = []
for n in range(len(a)):
    for m in range(n+1,len(a)):
        if a[n]+a[m]== k :
            lst = [n,m]
print(lst)
'''
# COUNTING WORDS WITH GIVEN PREFIX
'''a,k = input().rsplit(',',1)
a = eval(a.strip())        
k = k.strip()
count=0
for i in a:
    if i.startswith(k):
        count+=1
print(count) '''

# SUM OF ROW AND COLUMN 
'''A = eval(input())   # Example: [[1, 2], [4, 5], [8, 9]]
result = []
for row in A:
    result.append(sum(row))
for col in range(len(A[0])):
    col_sum = 0
    for row in A:
        col_sum += row[col]
    result.append(col_sum)

print(result)'''

# TUPLE

# SECOND HIGHEST SCORE 
'''lst = eval(input())
b = set(lst)
a = list(b)
a.sort()
if len(a)<2:
    print("No Highest Second Score ")
else:
    print(a[-2])'''

# NUMBER MISSING FROM THE SERIES
'''a = eval(input())
n1 = a[0]
n2 = a[-1]
suma = 0
sum = 0
for i in range(n1,n2+1):
    sum+=i 
for i in a :
    suma+=i
b = sum - suma
print(b)'''

#  ROTATE A LIST BY K ELEMENTS
'''a,k = input().rsplit(',',1)
a = eval(a)
k = int(k)
k = k % len(a)             # Normalize k to avoid out-of-range slicing
f = a[-k:] + a[:-k]        # Perform right rotation
print(f)'''

# EXACTLY ONE SOLUTION 
'''a,k = input().rsplit(',',1)
a = eval(a)
k = int(k)
lst = []
for n in range(len(a)):
    for m in range(n+1,len(a)):
        if a[n]+a[m]== k :
            lst = [n,m]
print(lst)
'''
# COUNTING WORDS WITH GIVEN PREFIX
'''a,k = input().rsplit(',',1)
a = eval(a.strip())        
k = k.strip()
count=0
for i in a:
    if i.startswith(k):
        count+=1
print(count) '''

# SUM OF ROW AND COLUMN 
'''A = eval(input())   # Example: [[1, 2], [4, 5], [8, 9]]
result = []
for row in A:
    result.append(sum(row))
for col in range(len(A[0])):
    col_sum = 0
    for row in A:
        col_sum += row[col]
    result.append(col_sum)

print(result)'''

# SET






