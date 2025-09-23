# PRIME NUMBERS UPTO N
n = int(input())
m = int(input())
prime=[]
for num in range (n,m+1):
    isPrime = 1
    for k in range (2,num):
        if(num%k==0):
            isPrime = 0
            break
    if(isPrime==1 and num>1 and n>1):
        prime.append(num)
print(",".join(map(str,prime)))

# IS IT PRIME NUMBER OR NOT
'''n = int(input("Enter a number : "))
isPrime = 1
if n > 1:
    for k in range(2, n):
        if n % k == 0:
            isPrime = 0
            break
    if isPrime==1:
        print("Prime Number")
    else:
        print("Not a Prime Number")
else:
    print("Not a Prime Number")
'''
