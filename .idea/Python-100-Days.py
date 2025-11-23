# print("Hello\nWorld")
#
# name = "Kanika"
# age = 23
# price = 45.67
#
# age1 = age
# print("My name is: ",name)
# print("My age is: ",age)
# print(age1)
#
# print(type(name))
# print(type(price))
#
# age2 =20
# old = True
# a = None
# print(type(old))
# print(type(a))
#
# a =67
# b =65
# sum = a+b
# print(sum)
#
# a1 = 5
# b1 = 2
#
# #arthmetic operators
# print(a1 + b1)
# print(a1 - b1)
# print(a1 * b1)
# print(a1 / b1)
# print(a1 % b1)#reminder
# print(a1 ** b1)# a1^b1
#
# #relational operators
# print(a1 == b1)
# print(a1 != b1)
# print(a1 > b1)
# print(a1 >= b1)
# print(a1 <= b1)
# print(a1 < b1)
#
# #assigment operators
# num1 = 10
# num2 = 5
# num3 = 4
# num4 = 10
# num5 = 10
# # num = num + 10
# num1 += 10
# num2 -= 10
# num3 *= 10
# num4 /= 10
# num5 **= 5 #power operator
# print("num ",num1)
# print("num ",num2)
# print("num ",num3)
# print("num ",num4)
# print("num ",num5)
#
# #logical operators
# a = 20
# b = 10
# print(not True)
# print(not (a > b))
#
# val1 = True
# val2 = False
# print("And operator: ",val1 and val2)
# # print("Or operator: ",val1 or val2)
# print("Or operator: ",(a == b) or (a>b))
#
# #Type Conversion
# #Type Casting
# #man lo agar hum normlly
# a = 6
# b = 7
# print(a+b) # so this is a type conversion but when
# # a = "2"
# # b = 4
# print(a+b) # then error throw karega becoz ek string or integer add nhi ho sakta h
# # jab hum isse type casting me convert kr de do kuchh is tarah ka hoga
# a = int("2")
# b = 4
# print(a+b)
#
# a = 3.14
# b = str(a)
# print(type(b))
#
# # So this is type casting
# int ("6")
# val = int(input("enter some value: "))
# print(type(val),val)
#
# name = input("enter your name: ")
# age = int(input("enter your age: "))
#
# print("welcome: ",name)
# print("my age: ",age)
# from distlib.resources import finder
# from numpy.ma.core import append
# from pandas.compat.numpy.function import validate_prod

# Practice question
#solve 1st
# var1  = int(input("enter your first value: "))
# var2  = int(input("enter your second value: "))
# sum = var1 + var2
# print("the Sum is: ",sum)

# area = int(input("enter the square value"))
# print(area*area)
# print(area**2)

# var1  = int(input("enter your first value: "))
# var2  = int(input("enter your second value: "))
# avg = (var1 + var2)/2
# print(avg)

# a  = int(input("enter your first value: "))
# b  = int(input("enter your second value: "))
# if a>=b:
#     print("True")
# else:
#     print("False")
# print(a>=b)

#strings
#basic operation in strings
#1.concatenation
# str1= "hello"
# print(len(str1))
# str2 = "world"
# final = str1+str2
# final_str= str1+" "+str2
# print(final)
# print(final_str)
# #indexing in string
# str = "apna college"
# print(str[5])
#
# #Slicing (accessing parts of a string)
# #str[starting_index:ending_index]
# print(str[0:4])
# print(str[5:len(str)])
# print(str[:4])
# print(str[5:])
# #Negative index
# str = "Apple"
# print(str[-5:-1])
#
# #String Functions
# str = "I am a studing python from Apna collage"
# print(str.endswith("age"))
# print(str.startswith("I"))
# print(str.capitalize()) #1st char capital hota h bs
# print(str.replace("python","java"))
# print(str.find("a")) #jaha bhi ye exist karta h vaha ka 1st index return hojata h
# print(str.count("l")) #substr ko count karta h

#Practice
#1st
# username = input("Enter your name")
# print(len(username))
#2nd
# string = "This is our $ sign"
# print(string.count("$"))
# string = "This is our $ sign"
# print(string.find("$"))

#Condition Statement
# age = 21
# if (age>=18):
#     print("You can Vote,,,")
# else:
#     print("You can't Vote...")

# light = input("Enter the color of Light:  ")
# if(light == "Red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("Wait")
# elif(light == "Green"):
#     print("Go......") #indentation (jo print likhne k pehle tabb diya h use bolte h)
# else:
#     print("Idk")
#
# print("End the code")
#Note:  agar if statement true hai to bs vhi print hogi , agar  if statement false hui tabhi elif
# statement per aaenge
#
# marks = int(input("Enter your Marks: "))
# if (marks>=90):
#     print("Grade A...")
# elif (90>marks>=80):
#     print("Grade B...")
# elif (80>marks>=70):
#     print("Grade C...")
# elif (70>marks):
#     print("Grade D...")
# else:
#     print("You Fail...")
#
marks = int(input("Enter your Marks: "))
if  (marks>=90):
    grade = "A"
elif (marks>=80 and marks<90):
    grade = "B"
elif (marks>=70 and marks<80):
    grade = "C"
elif (marks>=40 and marks<70):
    grade = "D"
else:
    print("You Fail...")
print("The grade of the students: ",grade,marks)

#nesting condition
# age = 90
# if (age>=18):
#     if(age>=80):
#         print("You can't Drive..")
#     else:
#         print("You can Drive..")
# else:
#     print("You can't Drive")

#Practice Questions
#1st
# num = 14
#
# if (num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")


# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# num3 = int(input("Enter third num: "))
#
# if(num1>=num2 and num1>=num3):
#     print("First nummber is largest: ",num1)
# elif(num2>=num3):
#     print("Secon number is larest: ",num2)
# else:
#     print("Third number is largest: ",num3)

# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# num3 = int(input("Enter third num: "))
# num4 = int(input("Enter forth num: "))
#
# if(num1>=num2 and num1>=num3 and num1>=num4):
#     print("First nummber is largest: ",num1)
# elif(num2>=num1 and num2>=num3 and num2>=num4):
#     print("Second number is larest: ",num2)
# elif (num3 >= num1 and num3 >= num2 and num3 >= num4):
#     print("Third number is larest: ", num3)
# else:
#     print("Forth number is largest: ",num4)

# x = int(input("Enter  num: "))
# if(x % 8 == 0):
#     print("Multiple of 8..")
# else:
#     print("Not a Multiple..")

#list(mutable) and tuples
# marks = [3,4,5,6,7]
# print(marks)
# print(marks[3]) #indexing
# print(type(marks))
#
# student = ["Kanika",56,"Goa"]
# print(student[0])
# student[0] = "Arjun"
# print(student) #replace
# print(len(student))
# #Slicing
# marks = [56,65,43,56,77]
# print(marks[1:3])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])
# #list Methods
# list = [2,1,3]
# list.append(4)#add one element in the end
# print(list)
# list.append(5)
# print(list)
# list.sort()#sorts in ascending order
# print(list)
# list.sort(reverse=True)#sorts in descending order
# print(list)
# list.reverse()#jo last ab tk list bn gai h use reverse karna
# print(list)
# list.insert(4,6)# insert element at index
# print(list)
# list.remove(2)# element remove
# print(list)
# list.pop(2)#last ka element remove
# print(list)
#
# #Tuples(immutable)(no changes available)
# tup = (3,4,5,6,7)
# print(tup)
# tup1 = (1,)#agar ek element bhi le re h tuple me to "," lagana jaruri h
# print(tup1)
# print(type(tup))
# print(tup[0])
# #Slicing
# names = ("a","p","p","l","e")
# print(names)
# print(names[0])
# print(names[1:4])
# print(names[:4])
# print(names[1:])
# print(names[-3:-1])
#
# names1  = ('e','l','e','p','h','a','n','t')
# print(names1.index('e'))
# print(names1.count('e'))

#Practice
# list = ["Saiyaara","My Fault","Our Fault"]
# print(list)
#
# movies = []
# mov1 = input("Enter 1st movie: ")
# mov2 = input("Enter 2nd movie: ")
# mov3 = input("Enter 3rd movie: ")
#
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# movies = []
# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2nd movie: "))
# movies.append(input("Enter 3rd movie: "))
# print(movies)

#2nd
# list = [1,2,3,2,1]
# list2 = [1,2,3]
#
# copy_list = list.copy()
# copy_list.reverse()
#
# if(copy_list == list):
#     print("Palindrome")
# else:
#     print("Not Palindrome")
#
# #3rd
# tup = ("C","D","A","A","B","B","A")
# print(tup.count("A"))
#
# #4th
# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

#Dictionary & Sets
# dict = {"Name":"Kanika",
#         "Age":20,
#         "Marks":8,
#         "list":[1,2,3,4],
#         "Tuple":(1,2,3,4)
#         }
# print(dict)
# print(type(dict))
# print(dict["Name"])
# print(dict["Tuple"])
# dict["Name"] = "Sradha" #Replace the value (Overwerite)
# dict["Surname"] = "Kapoor"#Add new key and value
# print(dict)
#
# null_dict = {}
# null_dict["name"] = "Kanika"
# print(null_dict)
#
#Nested Dictionary
# student = {
#     "Name" : "Kanika Sharma",
#     "Subjects" : {
#         "Physics" : 87,
#         "Chemistry" : 90,
#         "Maths" : 79
#     }
# }
# print(student)
# print(student["Subjects"])
# print(student["Subjects"]["Maths"])
#
# # Dictionary Methods
# print(student.keys())
# print(list(student.keys()))
# print(len(list(student.keys())))
#
# print(student.values())
# print(list(student.values()))
#
# print(student.items())
# print(list(student.items()))
#
# pairs = list(student.items())
# print(pairs[0])

# print(student["Name"])
# print(student.get("Name"))
#
# print(student["Name2"]) #error
# print(student.get("Name2")) #no error -> None

# student.update({"City":"Delhi"})
# print(student)
# new_dict = {
#     "Name" : "Shradha Kapoor",
#     "City" : "Mumbai"
# }
# student.update(new_dict)
# print(student)

#Sets(mutable) but uskeelements immutable hai
#list and dict ko set ke andar store nhi kr sakte
# collection = {1,2,3,4}
# print(collection)
# print(type(collection))
# set2 = {1,2,2,2}
# print(set2)
# null_set = set()
# print(null_set)
#
# #sets Method
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("Kanika")
# collection.add((1,2,3))
# print(collection)
#
# collection.remove(1)
# print(collection)
#
# collection.pop()
# print(collection)
# collection.pop()
# print(collection)
#
# collection.clear()
# print(collection)
#
#
# set1 = {1,2,3}
# set2 = {2,3,4}
#
# print(set1.union(set2))
# print(set1.intersection(set2))

#Practice
# dictionary = {
#     "cat":"a small animal",
#     "table":{"a piece of furniture","list of facts and figures"}
# }
# print(dictionary)
#
# subjects= {"python","java","c++","python","javascript","java","python","java","c++","c"
# }
# print(subjects)
# print(len(subjects))

# marks = {} #None
# print(marks.update({"Physics":89,
#     "Chemistry":90,
#     "Maths":81}))
# print(marks)
#
# marks["Physics"] = 79
# marks["Chemistry"] = 89
# marks["Maths"] = 90
# print(marks)

# marks = {}
# x = int(input("enter the physics marks: "))
# marks.update({"Your Physics Marks is: ":x})
# x = int(input("enter the chemistry marks: "))
# marks.update({"Your Chemistry Marks is:":x})
# x = int(input("enter the maths marks: "))
# marks.update({"Your Maths Marks is:":x})
# print(marks)

# values = {9,'9.0'}# set ke andar python me 9.0 and 9 ko same karike se treate kiya jata h
# print(values)
# values1 = {
#     ("int",9),
#     ("float",9.0)
# } #built-in use karna h(int, float)
# print(values1)

#loops in Python

# count = 1 #iterator
# while count<=5: #iteration
#     print("Hi",count)
#     count += 1
# print(count)

# i = 5
# while i >=1:
#     print(i)
#     i -= 1
# print("Loop ended")
#
# #Practice
# i = 1
# while i <=100:
#     print(i)
#     i += 1
#
# i = 100
# while i>=1:
#     print(i)
#     i -= 1

# i = 1
# n = int(input("enter: "))
# while i <= 10:
#     print(n*i)
#     i += 1

# nums = [1,4,9,16,25,36,49,64,81,100]
# print(len(nums))
#traverse(travel karna)
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1
#searchig x value
# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# i = 0 #initialization
# while i < len(nums):
#     print(nums[i])
#     i += 1

# while i < len(nums):
#     if(nums[i])==x:
#         print("found at index",i)
#         # break
#     print("finding")
#     i += 1
# print("end of loop")

#break & continue
# i = 1
# while i<=5:
#     print(i)
#     if i == 3:
#         break #break condition
#     i+=1
# print("end of loop")

# i = 0
# while i <= 5:
#     if i==3:
#         i += 1
#         continue #skip
#     print(i)
#     i += 1
#
# i = 1
# while i <= 10:
#     if i%2 == 0:
#         i += 1
#         continue #skip even numbers
#     print(i)
#     i += 1

# i =1
# while i <= 10:
#     if i%2 != 0:
#         i += 1
#         continue #skip odd numbers
#     print(i)
#     i += 1

# for loop
#traversal , for traversing "list,string,tuple,"etc
# for i in range(1,11):
#     print(i)
#
# list = {1,2,3,4,5}
# for el in list:
#     print(el)
# else:
#     print("End")
#
# n = 2
# for i in range(1,11) :
#     print(n*i)
#
# str = "Kanika Sharma"
# for char in str:
#     if char == "S":
#         print("found",char)
#         break
#     print(char)

# nums = [1,4,9,16,25,36,49,64,81,100]
# for i in nums :
#     print(i)
#
# nums1 = (1,4,9,16,25,36,49,64,81,100)
# x = 25
# for i in nums1:
#     if i == x:
#         print("found",i)
#         break

# range
# seq = range(5)
# for i in seq:
#     print(i)
# for i in range(11): # range (stop)
#     print(i)
# for i in range(1,11): # range (start, stop)
#     print(i)
# for i in range(2,10,2): # range (start,stop,stop)
#     print(i)
# for i in range(2,101,2): # even numbers
#     print(i)
# for i in range(100,0,-1): # reverse number
#     print(i)

#pass(null statement)
# for i in range(5):# agar kisi statement ko khali chhodna h to pass ko use kiya jata h
#     pass #skip
#
# if i < 5:
#     pass

#Practice
# n = 9
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Sum= ",sum)
#
# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i+=1
# print("Sum= ",sum)

#factorial
#factorial = 1*2*3*4........n
# n =5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial number: ",fact)
#
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("Factorial number: ",fact)

#Function and Recursion

#Function
# def cal_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# cal_sum(1,2) #function call (argument)
# cal_sum(1,2)
# cal_sum(1,2)
#
# def cal(a,b):
#     return a+b
# sum = cal(1,3)
# print(sum)
#
# def print_hello():
#     print("hello")
# output = print_hello()
# print(output) #None

# def avg(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg
# avg(1,2,3)

#Functions (Built-in(print(),len(),type(),range()). User defined function)
# print("apnacollege",end=" ") #seq = " "  # Built-in Function
# print("Kanika") #end = "\n"

#Default parameters
# def cal_prod(a=1,b=5): #default
#     print(a*b)
#     return a*b
# cal_prod()

#Practice
# cities = ["delhi","goa","noida","mumbai","chennai","indore"]
# print(len(cities)) # len parameter
# # in the form of function
# def print_len(list): #length with functions
#     print(len(list))

# print_len(cities)

#single line me print kana h
# def print_single(lists):
#     for list in cities:
#         print(list,end=" ,")
# print_single(cities)

#factorial
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("Factoial number: ",fact)
#
# i = 1
# n =5
# fact = 1
# while i <= n:
#     fact *= i
#     i+=1
# print(fact)
#
#
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print("Factorial is : ",fact)
# factorial(5)
#
# def factorial(n):
#     i = 1
#     fact = 1
#     while i <= n:
#         fact *= i
#         i+=1
#     print("Factoial num is : ",fact)
# factorial(5)
#
# #convert USD to INR
# #1usd = 83
# #usd = 166
# def conveter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD= ",inr_val, "INR")
# conveter(100)
#
# def func(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")
# func(4)

#Recursion
# when function calls itself repeatedly
# def sh(n):
#     print(n)
# sh(4)
# #
# def show(n):
    # if(n == 0): # condition dete hai recusion ke andar to usi ko ''Base Case'' kehte h
    #     return # contol return
    # print(n)
    # show(n-1) #show ko def ke andar hi call karne ko recursion kehte h
    # print("END")
# show(5)

#Factorial with recursion
#with function
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# factorial(4)
# #with recursion
# #n! = 1x2x3...(n-1)xn
# #n! = (n-1)xn #recursion relation
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(4))

#practice
# def natural_num(n):
#     if n == 0:
#         return
#     print(n)
#     natural_num(n-1)
# natural_num(4)
#
# #sum of natural number using recursion
# n = 9
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)
#
# #with Function
# def nat(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     print(sum)
# nat(9)

#with Recursion
# def cal_sum(n):
#     if n== 0: # base case
#         return 0
#     return cal_sum(n-1) + n #in recursion add function in is important
# print(cal_sum(9))

#with recursion print list values
# def print_list(list,idx=0):
#     if idx == len(list): #base case
#         return
#     print(list[idx])
#     print_list(list,idx+1)
#
# fruits = ["apple","mango","banana","grapes"]
# print_list(fruits)

#File I/o
#types of files
#Text files : .txt , .docx , .log etc.
#Binary Files: .mp4 , .mov , .png , .jpeg etc.
##########################################################

# f = open("demo.txt","rt")
# data = f.read()
# print(data)
#
# line1 = f.readline() #first readline ke baad ek line ka space hota h \n ki vajah se
# print(line1)
#
# # print(type(data))
# f.close()
#
# f = open("demo.txt","a") #append k pehle ''write'' likha tha
# f.write("\nI want to learn Python advance")
# f.close()
#
# f = open("sample.txt","w")
# f.close()

# f = open("demo.txt","r+") # overwrite karne ka kaam karta h vo bhi suru se
# f.write("abc")
# print(f.read())
# f.close()


# f = open("demo.txt","w+") #data khali ho jaega
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# 'r'
# 'w'
# 'a'
# 'rt'
# 'wt'
# 'rb'
# 'wb'
# 'r+'
# 'w+'
# 'a+'

# ''with'' syntax
# with open("demo.txt","r") as f: # 'as' is a alias
#     data = f.read()
#     print(data)
#
# with open("demo.txt","w") as f:
#     f.write("new data")
#
#Deleting a file
#using the os module
# import os
# os.remove("sample.txt")

#Practice
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","python")
# print(new_data)
#
# with open("practice.txt","w") as f:
#       f.write(new_data)

# def check():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if data.find(word) != -1 :  #''if word in data:''
#             print("found")
#         else:
#             print("Not found")
# check()

# def check_line():
#     word = "python"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#             line_no += 1
#     return -1
#
# check_line()


# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)
#
#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             print(int(num))
#             num= ""
#         else:
#             num += data[i]

#ek or tarika h isi ka
# count = 0
# with open("practice.txt","r") as f:
#      data = f.read()
#
#      nums = data.split(",")
#      for val in nums:
#          if(int(val) % 2 == 0):
#              count += 1
# print(count)


#'''''OOps''''''#
#Object Oriented Programming
#class & objects
# class Student:
#     name = "Kanika"
#
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)

# class Car:
#     color = "Blue"
#     brand = "BMW"
# car1 = Car()
# print(car1.color)
# print(car1.brand)

# Constructor(__init__()) initialization
# attribute => data, variable

# class Student:
#     #default constructor
#     def __init__(self):
#         pass
#
#     #parameterized constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("I am a beginner")
#
# s1 = Student("Kanika", 90)
# print(f"Your name is {s1.name} and your marks is {s1.marks}")

#Class and Instance attribute
# In class only things can store => data(attributes) and methods
#
# class Student :
#     def __init__(self, name,age,hobby,marks): #data(attributes)
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         self.marks = marks
#
#     def display(self): #method  #self=> argument
#         print(f"Hello!\n My beginner {self.name}. I know your age is {self.age} and hobby is {self.hobby}...")
#
#     def get_marks(self):
#         return self.marks
#
# s1 = Student("Kanika","20","Drawing",89)
# s1.display()
# print("Your Marks is..",s1.get_marks())


# Practice
# class Student:
#     def __init__(self,name,physics,chemistry,maths):
#         self.name = name
#         self.physics = physics
#         self.chemistry = chemistry
#         self.maths = maths
#     def average(self):
#         print(f"{self.name} Average is",((self.physics+self.chemistry+self.maths)//3))
# s1 = Student("Kanika",89,78,87)
# s1.average()
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi",self.name, "Your Average is : ",sum//3)
#
# s1 = Student("Kanika",[78,87,67])
# s1.get_avg()
#
# s1.name = "Kartik"
# s1.get_avg()

#Static Method
# without using  self

# class Student:
    # @staticmethod # decorator
    # def college():
    #     print("ABC college")
# s1 = Student()
# s1.college()

# Pilar of OOPS
#Abstraction  (Hiding the implementation details of a class and only
# showing the essential features to the user.)
# (** unnecessary data ko hide karna or sirf essential features show karna)

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True  # unesscary details hide
#         self.acc = True
#         print("car started..") # essential features show
# car1 = Car()
# car1.start()
#
# #Encapsulation  (Wrapping data and functions into a single unit (object))
# # capsule bana diya or usme apna sara data daal diya
# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no
#
#     def debit(self,amount): #debit(-)
#         self.balance -= amount
#         print(f"Rs.",amount, "was debited..")
#         print(f"Total balance = {self.get_balance()}")
#
#     def credit(self,amount): #credit(+)
#         self.balance += amount
#         print(f"Rs.", amount, "was credited..")
#         print(f"Total balance = {self.get_balance()}")
#
#     def get_balance(self):
#         return self.balance
#
# a1 = Account(10000,123455)
# a1.debit(1000)
# a1.credit(500)
# a1.credit(40000) # salary aai usko bhi add kr do

#del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# s1 = Student("Kanika")
# print(s1.name)# yaha per to print ho jae ga
# del s1.name
# print(s1.name) #per yaha pr error through karega kyuki jo hamne
# object me attribute likha tha vo delete ho chuka h..

#Private(like) attributes & methods
#take a Example of public and private
# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass
# a1 = Account(12345,1234456)
# print(a1.acc_no)
# print(a1.acc_pass) #this is ''public'' becoz we run the attrbutes  out of the class

# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)
# a1 = Account(12345,1234456)
# print(a1.acc_no)
# print(a1.reset_pass()) #private so we can't run out of class (__hello) double under scope ka mtlb private
# hota h jo ki hum attributes and method me use karte h

# class Person:
#     __name = "Kanika"
#
#     def __hello(self):
#         print("hello everyone!!")
#
#     def welcome(self):
#         self.__hello()
# p1 = Person()
# print(p1.welcome())

#Inheritance
# When the one class(child/derived) derives the properties & methods of another class(parant/base))
#types
#Single inheritance
# class Car:
#     color = "Blue"
#     @staticmethod #without using self
#     def start():
#         print("Car Started...")
#     @staticmethod
#     def stop():
#         print("Car Stoped...")
#
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name
#
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("prius")
# print(car1.name)
# print(car2.name)
# print(car1.color)
# print(car1.start())
# print(car1.stop())

#Multi-level inheritance
# class Car:
#     @staticmethod #without using self
#     def start():
#         print("Car Started...")
#     @staticmethod
#     def stop():
#         print("Car Stoped...")
#
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand
#
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type
# car1 = Fortuner("disel")
# car1.start()
# car1.stop()

#Multiple Inheritance
# class A:
#     varA = "Wlcome to class A"
# class B:
#     varB = "Welcome to class B"
# class C (A,B):
#     varC = "Welcomme to class C"
# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)

#Super Method
#super() method is used to access methods of parent class in child class
#
# class Car:
#     def __init__(self,type,brand):
#         self.type = type
#         self.brand = brand
#     @staticmethod #without using self
#     def start():
#         print("Car Started...")
#     @staticmethod
#     def stop():
#         print("Car Stoped...")
#
# class ToyotaCar(Car):
#     def __init__(self,name,type,brand):
#         super().__init__(type,brand)
#         self.name = name
#         super().start()
#
# car1 = ToyotaCar("prius","electric","BMW")
# print(car1.type,car1.brand)

#class Method
# class Person:
#     name = "Kanika"
#
#     # def changeName(self, name):
#     #        self.name = name  # isse sirf function ke liye naam print karga per hame class ka name change karna h
#     #       Person.name = name  # 1st tarika h class name change karne ka
#     #       self.__class__.name = "Kanu"  #2nd Tarika h class change karne ka
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name
#
# p1  = Person()
# p1.changeName("Kartik")
# print(p1.name)
# print(Person.name)
#
# #@property method
#
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy+self.chem+self.math)//3) + "%"
#
# stu1 = Student(98,87,80)
# print(stu1.percentage)
# stu1.chem = 70
# print(stu1.chem)
# print(stu1.percentage)

#in this class me humne jo chem k marks change kare h vo change hona chahiye tha pr vo change nhi hue
# to hum easy way me dekhe to hum property use arenge to change ho jaega

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#
#     # def calPercentage(self):
#     #     self.percentage = str((self.phy+self.chem+self.math)//3) + "%"
#
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)//3) + "%"
#
# stu1 = Student(98,87,80)
# print(stu1.percentage())
#
# stu1.math = 78
# print(stu1.percentage())


#decorator ==> staticmethod,classmethod,property,getter,setter

#Polymorphism
#Operator Overloading

# print(1+2)
# print("apna"+"college") #concatenate
# print([1,2,3,4]+[3,4,5,6]) #merge

#operator and Dunder Functions
# addition => __add__()
# subtraction => __sub__()
# multiplication => __mmul__()
# division => __truediv__()
#module => __mod__()

# Complex number => 2i + 3j (real + imaginary)
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#
#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")
#
#     # def add(self,num2):
#     def __add__(self, num2): #dunder function add karne k baad
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal,newImg)
#
#     def __sub__(self, num2): #dunder function sub karne k baad
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal,newImg)
#
# num1 = Complex(8,9)
# num1.showNumber()
#
# num2 =Complex(5,6)
# num2.showNumber()
#
# # num3 = num1.add(num2)
# num3 = num1 + num2 #add
# num3.showNumber()
#
# num3 = num1 - num2 #sub
# num3.showNumber()


# Practice Ques
#1st
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def Area(self):
#         area = (22//7)*self.r*self.r
#         print(f"The area of Circle is: {area} ")
#         # return 3.14*self.r**2
#     def Perimeter(self):
#         perimeter = 2*(22//7)*self.r
#         print(f"The perimeter of Circle is: {perimeter} ")
#
# a1 = Circle(6)
# a1.Area()
# a1.Perimeter()
#
# #2nd
#
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def showDetails(self):
#         print("Role = ",self.role)
#         print("Department = ",self.department)
#         print("Salary = ",self.salary)
#
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","45000")
#
# s1 = Employee("junior","main",40000)
# s1.showDetails()
#
# e1 = Engineer("Kanika",20)
# e1.showDetails()
#
# #3rd
# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price
#
#     def __gt__(self, ord2): # dunder function se hum apna logic create kr sakte h
#         return self.price > ord2.price
#
# odr1 = Order("Chips",30)
# odr2 = Order("Choclate",20)
#
# print(odr1 > odr2)











