# PYTHON COLLECTION
# LIST :- A BUILT IN DATA THAT LETS US CREATE MUTABLE SEQUENCES OF VALUES

# INPUT FROM THE USER 
'''lst = list(map(int, input("Enter numbers separated by space: ").split()))
print(lst)'''



fruits = ["Apple","Orange","Cherry","Apple"]

'''print(fruits) 
print(type(fruits))''' # print type - <class 'list'>

# Mixed list
mix_list = [1,"Apple",3.14,True]
'''print(mix_list)
print(type(mix_list))''' # <class 'list'>

# Nested List
nes_list = [1,[2,3],[4,5,6]]
'''print(nes_list)
print(type(nes_list))''' # <class 'list'>

# Access List - Indexing
name = ["Prashant","Sameer","Dev","Mohit","Nikhil"]
'''print(name[0]) # first element
print(name[1]) # Second element
print(name[-2]) # Second last element
print(name[-1])''' # Last element

# SLICING IN LISTS AND TUPLES --> STARTING INDEX ELEMENT WILL PRINT BUT NOT ENDING INDEX ELEMENT
# POSITIVE INDEX --> INDEX COUNTING FROM FIRST CHARACTER OF STRING AND STARTED FROM 0
# MARKS = [45,33,56,34,67]
# INDEX--> 0 ,1 ,2 ,3 ,4 
student = ["Mohit",21,"MBA","Atwa","Redmi"]
'''print(student[0:])
print(student[ :3])
print(student[2:4])
print(student[0::2])'''

# NEGATIVE INDEX --> INDEX COUNTING FROM LAST CHARACTER OF STRING AND STARTED FROM -1
# MARKS = [45,33,56,34,67]
# INDEX--> -5,-4,-3,-2 ,-1 
student = ["Mohit",21,"BBA","Atwa","Redmi"]
'''print(student[-5:-1])
print(student[:-1])
print(student[-4:-2])
print(student[-5:])'''

# reverse list 
'''print(student[::-1])'''

# LIST METHOD IN STRING

subject = ["English","Hindi","Mathematics","Physics","Chemistry"]

# append() - Append object to the end of the list.
'''subject.append("Social Science")
print(subject)'''

# sort() - Sort the list in ascending order and return None.
'''subject.sort()
print(subject)'''

# extend() - Extend list by appending elements from the iterable.
extra_sub = ["Python"]
'''subject.extend(extra_sub)
print(subject)'''

# Sort Reverse - reverse flag can be set to sort in descending order.
'''subject.sort(reverse=True)
print(subject)'''

# reverse() - Reverse the list
'''subject.reverse()
print(subject)'''

# insert() - insert object before index.
'''subject.insert(4,"Physical")
print(subject)'''

# remove() - Remove first occurrence of value.
'''subject.remove("Physical")
print(subject)'''

# pop() - Remove and return item at index (default last).Raises IndexError if list is empty or index is out of range.
'''subject.pop(3)
print(subject)'''

# clear () - 
'''num = [1,2,3]
num.clear()
print(num)'''

# index() - Return first index of value.Raises ValueError if the value is not present.
'''find = subject.index("English")
print(find)'''

# finding index within range - return index after given index
numb = [1,2,3,4,1,2,5,6,7,8]
'''find2 = numb.index(1,3)
print(find2)'''

# count() - Return number of occurrences of value.
'''count = numb.count(1)
print(count)'''

# JOIN LIST 
list1 = [1,2]
list2 = ["a","b"]

# Method 1 :- using + operator 
final_list = list1+list2
'''print(final_list)'''

# Method 2 :- using append
'''for x in list2:
    list1.append(x)
print(list1)'''

# Method 3 :- 
'''list1.extend(list2)
print(list1)'''

# LIST COMPREHENSIONS 

# LIST 1
'''squares = [x**2 for x in range(1,11)]
print(squares)'''

# Filter even numbers 
'''even_list = [x for x in range(1,20) if x%2==0]
print(even_list)'''

# apply function to each element of a list 
'''my_list = ["apple","mango","cherry"]
upper_list = [x.upper() for x in my_list]
print(upper_list)'''

# flatten a nested list using list comprehension
'''nested_list = [[1,2],[3,4],[5,6]]
result = [item for sublist in nested_list for item in sublist]
print(result)'''

# TUPLES IN PYTHON
# TUPLES = A BUILT IN DATA THAT LETS US CREATE IMMUTABLE SEQUENCES OF VALUES
'''tup = (3,1,5,7,8)
print(tup[0])
print(tup[2])'''

'''tup1 = () 
print(tup1) # SHOW () AS AN OUTPUT
print(type(tup1))'''

# for creating single value tuple --> if we write tup2 = (1) , it should be treated as an integer
'''tup2 = (2,)
print(tup2)
print(type(tup2))'''

# without parentheses 
'''tup_a = 1,2,3,4
print(tup_a)
print(type(tup_a))'''  # <class 'tuple'>

# type constructor
'''tup_b = tuple((1,2,3))
print(tup_b)
print(type(tup_b))''' # <class 'tuple'>

'''list_1 = [10,20,30]
new_tup = tuple(list_1)
print(new_tup)'''  # (10,20,30)

# indexing 
'''fruits_tup = ("Apple","Orange","Cherry","Apple","grapes")
print(fruits_tup[0])
print(fruits_tup[1])
print(fruits_tup[2])
print(fruits_tup[-1])'''

# slicing
'''numbers_tup = (10,20,30,40,50,60,70,80,90)
print(numbers_tup[1:4])
print(numbers_tup[:3])
print(numbers_tup[0::2])
print(numbers_tup[-4:-1])
print(numbers_tup[::-1])'''

# Tuple operation
# i) Concatenate :- Join tuple
'''tuple1 = (1,2,3)
tuple2 = ("a","b")
combine = tuple1+tuple2
print(combine) '''     # (1, 2, 3, 'a', 'b')
# ii)Repetition
'''tuple2 = ("a","b")*2
print(tuple2)'''
#Checking an element in a tuple
'''tuple1 = (1,2,3)
print(2 in tuple1)''' # True

# Tuple Iteration
# For loop
'''fruits = ("Apple","Orange","Cherry","Apple","grapes")
for i in fruits:
    print(i)'''
# While loop
'''fruits = ("Apple","Orange","Cherry","Apple","grapes")
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1''' # Output :- Apple Orange Cherry Apple grapes --> separate lines

# Tuple Methods
# count() :- Return number of occurrences of value. 
'''colors = ("red","green","blue","voilet","green","silver","gold","yellow")
print(colors.count("green"))''' # 2

# index() :- Return first index of value.Raises ValueError if the value is not present. 
'''colors = ("red","green","blue","voilet","green","silver","gold","yellow")
print(colors.index("green"))''' # 1

# Tuple Functions :-

# INPUT FROM THE USER 
'''tup =tuple(map(int, input("Enter numbers separated by space: ").split()))
print(tup)'''

Marks = (45,65,67,54,67,98,78,65,87)
# i) len():- Return the number of items in a container
'''print(len(Marks))''' # 9
# ii) sorted() :- Return a new list containing all items from the iterable in ascending order.
'''a = sorted(Marks)
print(a)''' # [45, 54, 65, 65, 67, 67, 78, 87, 98]
# iii) sum() :- Return the sum of a 'start' value (default: 0) plus an iterable of numbers
'''print(sum(Marks))''' # 626
# iv) min() :- 
'''print(min(Marks))''' # 45
# v) max() :- 
'''print(max(Marks))''' # 98

# Packing and Unpacking tuples

# a) Packing is the process of putting multiple values i nto a single value
'''a = "Prashant"
b = 19
c = "Engineer"
pack_tuple =a,b,c
print(pack_tuple)

# b) Unpacking is extracting the values from a tuple into separately 
name,age,profession=pack_tuple
print(name)
print(age)
print(profession)'''

# SET IN PYTHON 
# set is the collection of the unordered items - no indexing and set is mutable
# each element in the set must be unique & immutable
# List and dictionary can't be stored in sets

# INPUT FROM USER
'''s = set(map(int, input("Enter numbers separated by space: ").split()))
print(s)'''


''''collection ={1,2,3,"Hello","World",3,2}
print(type(collection))
print(collection)'''

# Null set
'''collection1 = set()
print(collection1)
print(type(collection1))'''

# create set by set constructor
'''my_set2 = set([4,5,6])
print(my_set2)''' # {4,5,6}

# Set operations 
# add() :- Add an element to a set.This has no effect if the element is already present.
'''numbers = {1,2,3,4}
numbers.add(100)
print(numbers) '''

# remove() :- Remove an element from a set; it must be a member.If the element is not a member, raise a KeyError.
'''fruits = {"Apple","Orange","Cherry","Apple"}
fruits.remove("Orange")
print(fruits)'''

# discard() :- Remove an element from a set if it is a member.
# Note :- Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
'''fruits = {"Apple","Orange","Cherry","Apple"}
fruits.discard("Papaya")
print(fruits)'''

# Set Methods 
# i) union() :-Return a new set with elements from the set and all others.
'''set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

# Alternative method 
union_alternative = set1 | set2 
print(union_alternative)'''

# intersection() :- Return a new set with elements common to the set and all others.
'''set1 = {1,2,3}
set2 = {3,4,5}
intersection_set = set1.intersection(set2)
print(intersection_set)

# Alternative method 
union_alternative = set1 & set2 
print(union_alternative)'''

# set_difference() :- Return a new set with elements in the set that are not in the others.
'''set1 = {1,2,3}
set2 = {3,4,5}
diffference_set = set1.difference(set2)
print(diffference_set)

# Alternative method 
difference_alternative = set1 - set2 
print(difference_alternative)
'''
# symmetric_difference() :- Return a new set with elements in either the set or other but not both.
'''set1 = {1,2,3}
set2 = {3,4,5}
symm_diff_set = set1.symmetric_difference(set2)
print(symm_diff_set)

# Alternative method 
symm_diff_set_alternative = set1 ^ set2 
print(symm_diff_set_alternative)'''

# Set iteration 
# for loop
'''numbers = {1,2,3,4,5,6,7,8,9,10}
for i in numbers:
    print(i)'''

# while loop :- doesn't support because sets doesn't support indexing 

# Set Comprehension
'''cubes = {x**3 for x in range(1,6)}
print(cubes)'''

# DICTIONARY IN PYTHON
# dictionaries are used to store data values in key : values pairs
# they are ordered ( after 3.6 version), mutable(changeable) & don't allow duplicate keys 
# if there is duplicate key , then intial key is updated with last key .

# INPUT FROM THE USER
'''items = input("Enter key:value pairs separated by space: ").split()
d = dict(item.split(":") for item in items)
print(d)'''


# i) Create dictionary using curly braces 
'''grade = {"First":"A","Second":"B","Third":"C"}
print(grade)
print(type(grade))'''

# ii) using dict() constructor
'''grade = dict(First="A",Second="B",Third="C")
print(grade)
print(type(grade))'''

# iii) using list of tuples
'''grade = dict([("name","Prashant"),("age",19)])
print(grade)
print(type(grade))'''

# Create a dictionary with some initial key-value pairs
'''student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}
print(type(student_grades))
# Display the dictionary
print("Student Grades Dictionary : ",student_grades)

# Access a value using a key
print("\nAlice's grade : ",student_grades["Alice"])

# Update a value
student_grades["Alice"] = "A+"
print("\nAlice's updated grade : ",student_grades["Alice"])

# Add a new key-value pair
student_grades["David"] = "D"
print("\nDictionary after adding David's grade : ",student_grades)'''

# DICTIONARY METHOD 
'''student = {
    "name" : "Mayank",
    "age" : 17,
    "subjects" : 
    {
        "physics" : 94,
        "chemistry" : 94,
        "mathematics" : 83
    }
}

# RETURN ALL KEYS
print(student.keys())

# RETURN ALL VALUES
print(student.values())

# RETURN ALL KEYS (key,val) PAIRS AS TUPLES
print(student.items())

# RETURN THE KEY ACCORDING TO VALUE
print(student.get("age"))

# INSERTS THE SPECIFIED ITEMS TO THE DICTIONARY
new = {"name" : "Bhavuk" , "age": 21}
student.update(new)
print(student)

# NULL DICTIONARY 
null_dict = {}
print(type(null_dict))
print(null_dict)'''