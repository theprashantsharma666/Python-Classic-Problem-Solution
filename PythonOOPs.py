#OOPS : OBJECT ORIENTED PROGRAMMING 

# USING LIST - CREATING STUDENT RECORDS
'''student_1 = ["Madhav",10]
student_2 = ["Vishakha",12]

student_1.append("A")
print(student_1)
print(f'{student_1[0]} is in class {student_1[1]}.')
print(f'{student_2[0]} is in class {student_2[1]}.')'''

# USINGS OOPS - CREATING STUDENT RECORDS
# Class - blueprint or template
'''class Student:
    pass
# Object - Instance of class
student1 = Student()
print(student1)'''

# output :  <__main__.Student object at 0x00000260C5766A50>

# It's only for a single Value 
# Note : Class takes no arguement.Here,Class is Student.
'''class Student:  
    name = "Madhav"
    grade = 10

student1 = Student()
print(student1.name , student1.grade)''' # Output : Madhav 10
  
# For solving this problem - for different values 
# In class , method is called function
# __init__ method :- contructor,value initailize - fix
# self parameter :- reference or connection between class and object - fix

class Student:
    def __init__(self,name,grade,percentage ): # Method
        self.name = name # Atrribute/Property
        self.grade =  grade # Atrribute/Property
        self.percentage =  percentage # Atrribute/Property
    def student_details(self):
        print(f'{self.name} is in class {self.grade} with {self.percentage}%.')

# Object : instance of class
student1 = Student("Madhav",10,92)
#print(student1.name , student1.grade) # Output = Madhav 10

student2 = Student("Vishakha",12,93)
#print(student2.name , student2.grade) # Output = Vishakha 12

#student1.student_details()
#student2.student_details()
#print(student1.__dict__)

'''MODIFY OBJECT PROPERTY'''

#print(student1.percentage) # Output : 92
#student1.percentage=95
#print(student1.percentage)  # Output : 95

'''DELETE STUDENT PROPERTY'''

#print(student1.__dict__) # Output : {'name': 'Madhav', 'grade': 10, 'percentage': 92}
#del student1.percentage
#print(student1.__dict__) # Output : {'name': 'Madhav', 'grade': 10}

'''OBJECT DELETE'''

#del student1
#print(student1) # Output : NameError: name 'student1' is not defined. Did you mean: 'student2'?

#OOPS : OBJECT ORIENTED PROGRAMMING 


#print(student1.name , student1.grade) # Output = Madhav 10

student2 = Student("Vishakha",12,93)
#print(student2.name , student2.grade) # Output = Vishakha 12

#student1.student_details()
#student2.student_details()
#print(student1.__dict__)

'''MODIFY OBJECT PROPERTY'''

#print(student1.percentage) # Output : 92
#student1.percentage=95
#print(student1.percentage)  # Output : 95

'''DELETE STUDENT PROPERTY'''

#print(student1.__dict__) # Output : {'name': 'Madhav', 'grade': 10, 'percentage': 92}
#del student1.percentage
#print(student1.__dict__) # Output : {'name': 'Madhav', 'grade': 10}

'''OBJECT DELETE'''

#del student1
#print(student1) # Output : NameError: name 'student1' is not defined. Did you mean: 'student2'?

# 4 FEATURES OF OOPS 
# Abstraction
# Encapsulation
# InheritenceD
# Polymorphism

# 1. Abstraction :- Hiding Unnecessary details from the user through class , methods 

'''class Student:
    def __init__(self,name,grade,percentage,team): # Method
        self.name = name # Atrribute/Property
        self.grade =  grade # Atrribute/Property
        self.percentage =  percentage # Atrribute/Property
        self.team =  team # Atrribute/Property
     
    def student_details(self): # method - abstraction :> hidden from user [ 2 lines ]
        print(f'{self.name} is in class {self.grade} with {self.percentage}%. He is a member of Team {self.team}.') 

team1 = "A"
team2 = "B"

# Object : instance of class
student1 = Student("Madhav",10,92,team1)
#print(student1.name , student1.grade) # Output = Madhav 10

student2 = Student("Vishakha",12,93,team2)
#print(student2.name , student2.grade) # Output = Vishakha 12

student1.student_details()
#print(student1.team)
student2.student_details()
#print(student1.__dict__)'''

# ENCAPSULATION : RESTRICT ACCESS TO CERTAIN ATTRIBUTES OR METHODS TO PROTECT DATA AND ENFORCED CONTROLLED ACCESS
# FOR ENCAPSULATION :- double undescore limits access
'''class Student:
    def __init__(self,name,grade,percentage,team): # Method
        self.name = name 
        self.grade =  grade
        self.__percentage =  percentage # double undescore limits access
        self.team =  team

# best practice for method to remove encapsulation using get - METHOD
#    def get_percentage(self): 
#       return self.__percentage
    
    def student_details(self): # method - abstraction  hidden from user 2 lines 
        print(f'{self.name} is in class {self.grade} with {self.percentage}%. He is a member of Team {self.team}.') 

team1 = "A"
team2 = "B"

# Object : instance of class
student1 = Student("Madhav",10,92,team1)
student2 = Student("Vishakha",12,93,team2)

#print(student1.percentage) 
# AttributeError: 'Student' object has no attribute 'percentage'
print(student1.get_percentage()) # Use only after removing encapsulation
#student1.student_details() 
# AttributeError: 'Student' object has no attribute 'percentage' 
'''

# INHERITENCE : Allows one class(child) to reuse the property and methods of another class(parent).
# Parent Class 
class Student:
    def __init__(self,name,grade,percentage): # Method
        self.name = name # Atrribute/Property
        self.grade =  grade # Atrribute/Property
        self.percentage =  percentage # Atrribute/Property
     
    def student_details(self): 
        print(f'{self.name} is in course {self.grade} with {self.percentage}%.') 

# Object : instance of class
student1 = Student("Madhav",10,92,)
student2 = Student("Vishakha",12,93)

# Child Class 
class GraduateStudent(Student): # GraduateStudents = Child Class inherit prop and methods student parent class
    def __init__(self,name,grade,percentage,stream): # old parameters from parent class and new in child class
        super().__init__(name,grade,percentage) # call prent class init 
        self.stream = stream # new attribute

#object : instance of class
Grad_student1 = GraduateStudent('Keshav','BCA',87,'DS')
print(Grad_student1.stream) # Output : DS
Grad_student1.student_details() # Output : Keshav is in class BCA with 87%.

# POLYMORPHISM : 
# ALLOWS METHODS IN DIFFERENT CLASSES TO HAVE SAME NAME BUT DIFFERENT BEHAVIOUR DEPENDING ON OBJECTS

'''class Student:
    def __init__(self,name,grade,percentage): # Method
        self.name = name # Atrribute/Property
        self.grade =  grade # Atrribute/Property
        self.percentage =  percentage # Atrribute/Property
     
    def student_details(self): # method 
        print(f'{self.name} is in class {self.grade} with {self.percentage}%.') 

# Object : instance of class
student1 = Student("Madhav",10,92)
student2 = Student("Vishakha",12,93)

# Child Class 
class GraduateStudent(Student): 
    def __init__(self,name,grade,percentage,stream): # old parameters from parent class and new in child class
        super().__init__(name,grade,percentage) # call prent class init 
        self.stream = stream # new attribute

    def student_details(self): # method
        print(f'{self.name} is in {self.grade} with {self.percentage}% and Stream is {self.stream}.')

#object : instance of class
student1 = Student("Madhav",10,92) # Student class
Grad_student1 = GraduateStudent('Keshav','BCA',87,'DS') # Graduatestudent class

student1.student_details() # Output :- Madhav is in class 10 with 92%.
Grad_student1.student_details() # Output :- Keshav is in BCA with 87% and Stream is DS.'''