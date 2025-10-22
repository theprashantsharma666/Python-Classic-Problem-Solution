#  STRING 
'''
name = "Prashant"
print(name)
print(type(name))
'''

# Differnt ways to string
'''
print('Hello World.')
print("It's easy.")
print(''' "Hey !! " ''')
'''

# Formatted String
# i) Old Style formatting
'''name = "Prashant"
age = 19
print("My name is %s and I'm %d old."%(name,age))''' # %s and %d are placeholdersfor strings ans integers

# ii) str.format() method
'''name = "Prashant"
age = 19
print("My name is {} and I'm {} years old.".format(name,age))

# Reference by index or keyword
print("My name is {0} and I'm {1} years old.".format(name,age))
print("My name is {name} and I'm {age} years old.".format(name="Charlie",age=28))'''

# F-Strings

'''name = "Madhav"
age = 20
print(f"My name is {name} and I'm {age} years old.")
# expressions inside the placeholders
print(f"In 5 years,my age will be {age+5}.")'''

# Escape charscters
'''
print("Hello\nWorld") # For new line
print("Hey\tPrashant") # For one tab space 
print('" \'kw-single quotes\' ")
'''

# String Operators in Python
'''a = "Hello"
b = "Python"

print(a+b) # Concatenation
print(a*2) # Repetition
print(a[1]) # Slice
print(a[1:4]) # Range Slice

if("a" in a):
    print("Exist")
else :
    print("Not Exist")

print(r"Hello\n World.")'''

# INDEXING
'''my_name = "Prashant"
print(my_name[0])
print(my_name[1])
print(my_name[-1])
print(my_name[-2])'''

# SLICING

'''name ="MADHAV"
print(name[::]) # 'MADHAV'
print(name[0:2]) # 'MA'
print(name[0:5:2]) # 'MDA'
print(name[-3:-1]) # 'HA'
print(name[::-1]) # 'VAHDAM'''

# STRING METHODS 
'''
a = "Returns an encoded version of the string"
# i) len()-Return the number of items in a container.
print(len(a))
# ii) upper()-Return a copy of the string converted to uppercase
print(a.upper())
# iii) lower()-Return a copy of the string converted to lowercase.
print(a.lower())
# iv) count()-Return the number of non-overlapping occurrences of substring sub in string S[start:end].
print(a.count("e"))
# v) find()- Return the lowest index in S where substring sub is found, such that sub is contained within S[start:en
print(a.find("e"))
# vi) split()-Return a list of the substrings in the string, using sep as the separator string
print(a.split(" "))
# vii) replace()-
print(a.replace("a","e"))
# viii) title()-Return a version of the string where each word is titlecased.
print(a.title())
# ix) strip()-Return a copy of the string with leading and trailing whitespace removed.
b = "        Return a copy of the string converted to lowercase.            "
print(b.strip())
# x) join()-Concatenate any number of strings.
zwords = ("Madhav","is","great.")
print("_".join(zwords))

'''

# STRING INDEXING
'''str1 = "Hello"
str2 = "Prashant"
final_str = str1 + str2
print(final_str)

lenght1 = len(final_str)
print(lenght1)

final_str2 = str1 + " " + str2
print(final_str2)
lenght2 = len(final_str2)
print(lenght2)

print("\n")'''

# INDEX --> POSITION FOR ACCESS CHARACTERS 

'''print(str1[0])
print(str2[0])
print(final_str[0])
print(final_str2[1])'''

# STRING FUNCTIONS 
str = "the dog barked loudly at the strangers."

# check whether given string ends with given word or not
'''print(str.endswith("gers.")) 
print(str.endswith("ger"))

# capital first letter of a string
str = str.capitalize() 
print(str)

# replace the old word with new word
str = str.replace("strangers","people")
print(str)

# return 1st index of 1st occurrer , if word don't exist it give -1 as a result
str=str.find("d")
print(str)'''

'''str = str.lstrip()
print(str)

a = "Mohit Saraswat"
print(a.split()) 

b = "Mayank Saxena"
print(b.split('n')) 

c = "Sachin Dagar"
print(c.split('a',1)

d ="Sachin Dagar"
print(c.split('a',-1))

d= "Sachin Dagar"
print(d.split('a',-100))

e= "Sachin Dagar"
print(e.split(maxsplit=2))

print(1, 2,sep="John")'''


