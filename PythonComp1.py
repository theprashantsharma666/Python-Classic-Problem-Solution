# FIRST PROGRAM
# print("Hello World")

# VARIABLE
'''marks = 92 # Integer
name = "Prashant Sharma" # String
price = 199.99 # Float
value = True # Boolean 
print(marks,name,price,value)

# data types 
print(type(marks)) 
print(type(name))
print(type(price))
print(type(value))'''

# Assigning values
'''name = "Prashant Sharma"
roll_no = 2415001154
print("My name is",name,"and my rollno is",roll_no,".")
print(name,roll_no,sep="-") # By Default is Space '''

# Ascii and unicode values
'''char1,char2,char3,char4,char5 = "A","Z","a","z"," "
print("Asscii value of",char1,"is",ord(char1),"\nAsscii value of",char2,"is",ord(char2),"\nAsscii value of",char3,"is",ord(char3),"\nAsscii value of",char4,"is",ord(char4),"\nAsscii value of (space) is",ord(char5))

alp1 = 65
print(chr(alp1)) # A ''' # reverse of ascii

# INPUT,OPERATORS AND TYPE CASTING
'''strinput = input("Enter your name : ")
intinput = input("Enter your age : ")
floatinput = input("Enter your percentage : ")'''

# PROBLEM 1 :- SUM OF TWO NUMBERS (ADDITIONALLY SUBTRACTION,MULTIPLICATION,DIVISION,MODULUS,EXPONENTIATION,FLOOR DIVISION)
'''first_no = int(input("Enter first number : "))
second_no = int(input("Enter second number : "))
sum,diff,mul,div,mod,exp,floor = first_no+second_no,first_no-second_no,first_no*second_no,first_no/second_no,first_no%second_no,first_no**second_no,first_no//second_no
print("Addition of two numbers are ",sum)
print("Subtraction of two numbers are ",diff)
print("Multiplication of two numbers are ",mul)
print("Diivision of two numbers are ",div)
print("Modulus of two numbers are ",mod) # Return Remainder
print("Value of ",first_no," raised to the power ",second_no,"is ",exp)
print("Floor division of two numbers are ",floor) # Return nearest whole number'''

# Assignment Operators :- =,+=,-=,*=,/=,%=.//=,**=,&=,|=,^=>>=,<<=
# Basic assignment operator :- +=,-=,*=,/=,%=,//=,**=
'''x1=7
y1=3
x1+=y1
print(x1) # x1=x1+y1

x2=7
y2=3
x2-=y2
print(x2) # x2=x2-y2

x3=7
y3=3
x3*=y3
print(x3) # x3=x3*y3

x4=7
y4=3
x4/=y4
print(x4) # x4=x4/y4

x5=7
y5=3
x5%=y5
print(x5) # x4=x4%y4

x6=7
y6=3
x6//=y6
print(x6) # x4=x4//y4

x7=7
y7=3
x7**=y7
print(x7) # x4=x4**y4'''

# Bitwise Operators :- &=,|=,^=>>=,<<= . 
# And(&),Or(|) and Xor(^) work based on truth table .
# Shift  Right (>>) decreases 0 or 1 from most right of the binary number 
# Shift  Left (<<) increases 0 from most right of the binary number

'''x1=6
y1=3
x1&=y1
print(x1) # x1=x1&y1

x2=6
y2=3
x2|=y2
print(x2) # x2=x2|y2

x3=6
y3=3
x3^=y3
print(x3) # x3=x3^y3

x4=16
y4=2
x4>>=y4
print(x4) # x4=x4>>y4

x5=4
y5=3
x5<<=y5
print(x5) # x5=x5<<y5 '''

# Comparison Operators := ==,!=,>,<,,>=,<=
'''x=6
y=5
print(x==y) # False
print(x!=y) # True
print(x>y) # True
print(x<y) # False
print(x>=y) # True
print(x<=y) # False'''

# Logical Operators :- and,or,not
# and : Returns True if both statements are True
# or : Returns True if one of the statements are True
# not : Reverse the result , returns False if the result is True
'''exp1 = 2>1 # True
exp2 = 5<4 # False
print(exp1 and exp2) 
print(exp1 or exp2) 
print(not(exp1)) 
print(not(exp2)) '''

# Identity Operators :- is , is not
# is : Returns True if both variables are the same object
# is not : Returns True if both variables are not the same object
'''x = 5
y = 5 
print("If",x,"is equal to",y,":",x is y)
print("If",x,"is not equal to",y,":",x is not y)'''

# Membership Operators :- in , not in 
# in : Returns True if a sequence with a specified value is present in the object
# not in : Returns True if a sequence with a specified value is not present in the object
'''fruits = ["Apple","Mango","Cherry","Banana"]
des_fruit = input("Desired Fruit : ")
print("If",des_fruit,"is present in fruits :",des_fruit in fruits)
print("If",des_fruit,"is not present in fruits :",des_fruit not in fruits)'''

# Operators Precedence :- () <- ** <- /,//,% <- * <- =,- <- <<,>> <- &,\,^ <- ==,<=,>=,<,>,!= <- and,or,not
'''a = 3+2**4/2*5-8//2
print(a)'''

# Type() Function :- Used to find type of vvariable
'''marks = 92 # Integer
name = "Prashant Sharma" # String
price = 199.99 # Float
value = True # Boolean 
print(marks,name,price,value)

# data types 
print(type(marks)) 
print(type(name))
print(type(price))
print(type(value))'''

# Typecasting :- Converting one data type to another
'''a = 2
b = 3
c = 5
a_str = str(a)
b_str = str(b)
c_str = str(c)
final_str = a_str+b_str+c_str
final_int = int(final_str)
print(final_int,type(final_int))'''

# ques :- Write a program to convert temperature from celcius to fahrenheit

'''temp_cel = float(input("Enter temperture in celcius : "))
temp_fah = ((temp_cel*9)/5)+32
print("Temperature in fahrenheit from celcius is",temp_fah)'''

# CONDITION AND LOOPS 
# Control Statements :- They allow us to control the flow of our program

# if-else
# Take integer input and tell if it positive and negative
'''n = int(input("Enter n : "))
if (n<0):
    print(n,"is negative.")
else:
    print(n,"is positive.")'''

# Take positive integer input and tell if it even or odd
'''n = int(input("Enter n : "))
if (n%2==0):
    print(n,"is even number.")

else:
    print(n,"is odd number.")'''

# elif
# Profit or Loss
'''cost_price = float(input("Enter cost price of an item : "))
selling_price = float(input("Enter selling price of an item : "))
if (cost_price>selling_price):
    profit = cost_price-selling_price
    print("The seller has made profit and profit is",profit,"rupees.")
elif (cost_price<selling_price):
    loss = selling_price-cost_price
    print("The seller has made profit and profit is",loss,"rupees.")
else:
    print("The seller has no profit or no loss.")'''

# Take input percentage of a student and print the grade according to marks 
'''percentage = float(input("Enter percentage : "))
if(81<=percentage<=100):
    print("Result is Very Good.")
elif(61<=percentage<=80):
    print("Result is Good.")
elif(41<=percentage<=60):
    print("Result is Average.")
else:
    print("Result is Fail.")'''

# Multiple Condition Using 'and' and 'or'
# Grade system for marks 
'''eng_marks = int(input("Enter english marks : "))
math_marks = int(input("Enter math marks : "))

if(eng_marks>80 and math_marks>80 ):
    print("Grade : A")
elif(eng_marks>80 or math_marks>80):
    print("Grade : B")
else:
    print("Grade : C")'''

# Take 3 positive integers input and print the greatest of them
'''x1 = int(input("Enter first number : "))
x2 = int(input("Enter second number : "))
x3 = int(input("Enter third number : "))
if(x1>x2 and x1>x3):
    print(x1,"is greatest.")
elif(x2>x1 and x2>x3):
    print(x2,"is greatest.")
else:
    print(x3,"is grestest.")'''

# Nested if-else
# Take 3 positive integers input and print the greatest of them
'''x1 = int(input("Enter first number : "))
x2 = int(input("Enter second number : "))
x3 = int(input("Enter third number : "))
if(x1>x2):
    if (x1>x3):
        print(x1,"is greatest.")
    else:
        print(x3,"is greatest.")
else:
    if(x2>x3):
        print(x2,"is greatest.")
    else:
        print(x3,"is grestest.")'''

# Take positive integer input and tell if it is divisible 5 or 3 but not divisible by 15
'''n = int(input("Enter number : "))
if(n%15==0):
    print(n,"is divisible by 15.")
else:
    if(n%3==0 or n%5==0):
        print(n,"is not divisible by 15 but divisible 3 or 5.")
    else:
        print(n,"is neither divisible 3 or 5.")'''

# Ternary Operator
# Checking Age if is it Adult or Minor
'''age = int(input("Enter Age : "))
status = "Adult" if age >= 18 else "Minor"
print(status) ''' 

# LOOPS
# for loop
# Print something upto n time
'''my_name = "Prashant Sharma"
n = int(input("Enter how many times: "))
for i in range(0, n, 1):   
    print(my_name)'''

# Printing list elements 
'''fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)'''

# while loop 
# Countdown
'''num = 5
while num > 0:
    print(num)
    num -= 1'''

# Sum of digits
'''num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10   # remove last digit

print("Sum of digits =", total)'''

# Keep asking until user guesses the number
'''secret = int(input("Enter Secret number : "))
while True:
    guess = int(input("Guess the number (1–10) : "))
    if guess == secret:
        print("Correct! You guessed it.")
        break  
    else:
        print("Wrong! Try again.")'''


# match Case
# Calculator
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+':
        print("Result =", a + b)
    case '-':
        print("Result =", a - b)
    case '*':
        print("Result =", a * b)
    case '/':
        print("Result =", a / b if b != 0 else "Division by zero error")
    case _:
        print("Invalid operator")'''

# PYTHON COLLECTION 

n = int(input())
for i in range(1,11,1):
    print(n,"x",i,"=",n*i)
