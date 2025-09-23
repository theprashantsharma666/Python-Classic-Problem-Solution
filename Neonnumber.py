n=int(input()) # 9
a = n*n # 81
c=0 
while a>0:
    b = a%10 # 81%10=1 --> 8%10=8
    c += b # c = 0+1 =1 --> 1+8=9
    a//=10 # 81//10 = 8 --> 
if(n==c):
    print(n,"is a neon number.")
else:
     print(n,"is not a neon number.")

