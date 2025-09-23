# 1
# 2 3
# 4 5 6 
# 7 8 9 10

'''n = int(input())
a = 1
for i in range (1,n+1):
    for j in range (1,i+1):
        print(a , end = " ")
        a+=1 
    print("")'''

# 1
# 3 5 
# 7 9 11

'''n = int(input())
a = 1
for i in range (1,n+1):
    for j in range (1,i+1):
        print(2*a-1 , end = " ")
        a+=1 
    print("")'''

# 1
# 0 1
# 1 0 1
'''n = int(input())
for i in range(1, n + 1):
    for j in range (1,i+1):
        if ((i+j)%2==0):
            print(1,end=" ")
        else :
           print(0,end=" ")
    print("")'''

#     1
#   1 2
# 1 2 3

'''n = int(input())
for i in range (1,n+1):
    for j in range (1,n-i+1):
        print(" ",end = " ")
    for k in range (1,i+1):
        print(k , end = " ")
    print("")'''

#     A
#   A B 
# A B C

'''n = int(input())
for i in range (1,n+1):
    for j in range (1,n-i+1):
        print(" ",end = " ")
    for k in range (1,i+1):
        print( chr(k+64) , end = " ")
    print("")'''

#       1
#     1 2 3 
#   1 2 3 4 5
# 1 2 3 4 5 6 7

'''n = int(input())
for i in range(1, n + 1):
    for j in range(n-i,0,-1):
        print(" ", end=" ")
    for k in range(1,2*i):
        print(k, end=" ")
    print("")'''  

#       A
#     A B C 
#   A B C D E
# A B C D E F G 

n = int(input())
for i in range(1, n + 1):
    for j in range(n-i,0,-1):
        print(" ", end=" ")
    for k in range(1,2*i):
        print(chr(k+64), end=" ")
    print("")  
