# FIBBONACCI SEQUENCE

num = int(input())
num1 = 0 
num2 = 1
count = 0
fib_sequence = [num1,num2]
while (count<(num-2)):
    result = num1+num2
    fib_sequence.append(result)
    num1 = num2
    num2 = result
    count+=1

print(fib_sequence)