# str1="This is a string using double quotes.\nLineSpace"
# str2='This is a string using single quotes.\tTabSpace'
# str3='''This is a string using triple quotes.'''

# print(str1)
# print(str2)

#concatenation of two strings
# s1="Hello"; s2="World"
# s3=s1+" "+s2
# print(s3)

# #length of a string
# print(len(s1))

#indexing in strings
# str1= "Abishek@123"
# print(str1[2])

# #not allowed to modify a string 
# str1[0]='a'

#slicing in strings
# str1= "Abishek@123"
# print(str1[0:7]) #Abishek
# print(str1[7:])  #@123
# print(str1[:len(str1)])  #Abishek
# print(str1[:])   #Abishek@123

# #negative indexing
# print(str1[-11:-4 ])

# string functions
# str="i am a coder"
# print(str.startswith("I am")) # returns true if the string starts with the specified value
# print(str.endswith("coder"))  # returns true if the string ends with the specified value
# str=str.capitalize() # capitalizes the first letter of the string 
# print(str) # now the original string is modified

# str.replace("o","0") # replaces all occurrences of a specified value with another value
# print(str) # the original string is not modified as strings are immutable

# print(str.find("coder")) # returns the lowest index of the substring in the string, otherwise returns -1
# print(str.count("a")) # returns the number of occurrences of a substring in the string

#Practice question 1 
#WAP to input users first name and print its length
# first_name=input("Enter your first name: ") 
# print("Length of your first name is: ", len(first_name))

#age=18
# if(age>=18):
#     print("You are eligible to vote.")
#     print("You can also apply for a driving license.")
#     print("You can also apply for a passport.")

# light="red"

# if(light=="green"):
#     print("Go") #indentation is important in python to define the scope of the code block

# elif(light=='yellow'):
#     print("Wait") # here in python we dont use curly braces to define the scope of the code block, instead we use indentation

# elif(light=='red'):
#     print("Stop")

# else:
#    print("Invalid traffic light color")


#grading system
# marks=int (input("Enter your marks: "))

# if(marks>=90):
#     print("Grade A")

# elif(marks>=80 and marks<90):
#     print("Grade B")

# elif(marks>=70 and marks<80):
#     print("Grade C") 

# elif(marks>=60 and marks<70): 
#     print("Grade D") 
    
# else: print("Grade F")
  

#Nesting of conditional statements
# age=int(input("Enter your age: "))

# if(age>=18):
#     if(age>=80):
#        print("You can't drive as u are too old")
#     else:
#       print("You can drive") 
# else:
#    print("You are not eligible to drive")


# even or odd number
# num=int(input("Enter a number: ")) 

# if(num%2==1):
#   print("number is odd")

# else:
#   print("number is even")


# greatest of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if(num1>num2 and num1>num3):
    print("Greatest number is: ", num1)

elif(num2>num1 and num2>num3):
    print("Greatest number is: ", num2)

else:
    print("Greatest number is: ", num3)
