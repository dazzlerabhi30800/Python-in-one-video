# import cv2
# import math

print("Hello world\n");
# print(math.gcd(4,16))

# This is a comment
# print(5+18)

'''
This is multiline comment
'''
# age = 14
# if(age<18):
#     print("Your age is less than 18")


# Variables 
# myVar = 45
# my_var = 56
# MyVar = 88
# # print(MyVar)

# a = 98
# b = "Abhi"
# # print(type(b))
# # typeA = type(a)
# # print(typeA)
# # print(a+45)


# # Typecastin in python
# e = "45"
# e = int(e)
# print(e+my_var)

# Strings
# myStr = '''This is my string,
# in Python '''
# print(myStr)

# my_str = "Abhishek,Michael,Franklin"
# print(my_str[2:7])
# print(len(my_str))
# lower_str = my_str.lower()
# print(lower_str)
# lower_str = my_str.replace("bhi","ihb")
# lower_str = my_str.replace("," , "\n")
# print(lower_str)


# str1 = "This is str1 "
# str2 = "This is str2"
# print(str1 + str2)
# print("print {1} and {0}".format(str2,str1))
# name1 = "Franklin"
# name2 = "Trevor"
# temp = f"{name1} is better protagonist than {name2}"
# print(temp)

# a = 3
# b = 5
# print(a ** b)

# List 
# thislist = ["Apple","Banana","Cherry","Papaya"]
# thislist.append("Avacado")
# thislist.insert(1,"Kiwi")
# thislist.remove("Avacado")
# thislist.pop()
# # print(thislist)
# del thislist[2]
# # print(thislist)
# thislist.clear()
# # print(thislist)
# newlist = list(("One Piece","Bleach","Naruto","DragonBall"))
# # print(newlist)


# # Tuples
# a  = ("American Psycho","Donnie Darko","Pulp Fiction")
# # print(a[0])


# #Sets
# b = {45,454,56}
# c = {34,88,12,23}
# # b.add(88)
# # b.delete(77)
# b.discard(77)
# print(b)
# print(c)


# Dictionaries
# abhiDict = {
#     "Name" : "Michael",
#     "Age" : 45,
#     "Marks" : 88
# }
# print(abhiDict)
# abhiDict["Marks"] = 99
# print(abhiDict)


# Conditionals

# age = input("Enter your age\n")
# age = int(age)
# # print(age)
# if age>18:
#     print("You are above 18")
# elif age<8:
#     print("You are below 18")
# else:
#     print("You are an asshole")


# For Loops
# for x in range(1,12):
#     print(x)

# fruits = ['Apple','Banana','Avacado']
# for x in fruits:
#     print(x)


# i = 0
# while(i<22):

#     i= i + 1
#     if i == 20:
#         continue
#     print(i)


# Functions
# def my_func():
#     print("Hello world")

# my_func()


# def my_func2(**kid):
#     print("My first name is " + kid["fname"] + " and last name is " + kid["lname"])

# my_func2(fname = "Abhishek", lname = "Singh")


# def my_func3(a = 44,b):
#     print("Running Sum")
#     return a+b

# a = my_func3(b = 55)
# print(a)


# Classes

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

   


# employe = Employee("Abhi",21,345435)
# print(employe.name)
# print(employe.age)
# print(employe.salary)


# Inheritance
# class Employee1:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
        

#     def printname(self):
#         print(self.fname,self.lname)

# class Student(Employee1):
#     def __init__(self,fname,lname):
#         Employee1.__init__(self,fname,lname)



# x = Student("Abhishek","Choudhary")
# x.printname()


# Iterators
# mytuple = ("apple", "banana", "cherry")
# myiter = iter(mytuple)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# str = "Michael"
# myit = iter(str)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple = ("apple","banana","cherry")
# for x in mytuple:
#     print(x)


# Create an iterator

# class Mynumbers():
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x


# myclass = Mynumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



# class Mynumbers():
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#                 x = self.a
#                 self.a +=1
#                 return x
#         else:
#             raise StopIteration


# myclass = Mynumbers()
# myiter = iter(myclass)


# for x in myiter:
#     print(x)



# Lambda Functions

# def my_func(n):
#     return lambda a : a * n

# mynumber = my_func(5)
# print(mynumber(9))

# x = lambda a : a + 10
# print(x(6))


# Modules
import code
# code.greeting("Abhishek")

from code import person
c = code.person["Name2"]
print(c)











