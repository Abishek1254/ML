# both sentences are printed in different lines
# print("My name is Abishek")
# print("My age is 21")

# # both sentences are printed in same line
# print("My name is Abishek.","My age is 21")

# print("Sum :" ,23+25) 
# name='''Abishek'''; age=21; salary=75000.0
# # print("My name is :",name, "and my age is :",age,"and my salary is",salary)
# print(type(name))
# print(type(age))
# print(type(salary))

# True and False T and F capital always in boolean datatype
# b=False
# print(type(b))

# arithmetic operators
# a=4; b=2
# sum=a+b
# difference=a-b
# product=a*b
# quotient=a/b
# print("Sum of",a,"and",b,"is:",sum)
# print("Difference of",a,"and",b,"is:",difference)
# print("Product of",a,"and",b,"is:",product)
# print("Quotient of",a,"and",b,"is:",quotient)
# print("Remainder of",a,"and",b,"is:",a%b)
# print("Exponentiation of",a,"and",b,"is:",a**b)


# relational operators
# a=50; b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# assignment operators
#num=10
# num+=5
# print(num)
# num-=5
# print(num)
# num*=2
# print(num)
# num/=2
# print(num)
# num%=4
# print(num)
# num**=2
# print(num)

#logical operators
# a=2; b=4
# # print(not (a>b))
# # print(not (True))
# # print(not (False))

# print(True and False)
# print(False or True)
# print((a==b) or (a<b))

#type conversion- done automatically by python (eg from int to float)
# a=2
# b=2.5
# sum=a+b # 2.0 + 2.5
# print(sum)

# #error
# a='2'
# b=4
# print(a+b)

#typecasting - manual conversion
# a="2"
# b=4
# print(int(a)+b)

# #error
# a="abi"
# b=4
# print(int(a)+b)

#taking input in python
# name=input("Enter your name :")
# print(name)

# #result of input() is always str
# something= input("Enter anything :")
# print(type(something))

# age= int ( input("Enter your age :") )
# print("Age is ",age)




# Practice question 1- WAP to input 2 numbers and print their sum
# num1= int ( input("Enter first number :"))
# num2= int ( input("Enter first number :"))
# sum=num1+num2
# print("Sum is :",sum)

#Practice question 2- WAP to input side of a square and print its area
# side= float ( input("Enter the side of square :"))
# area=side*side
# print("Area is :",area)


#Practice question 3- WAP to input 2 floating point numbers and print their average
# float1= float(input("Enter first number :"))
# float2= float(input("Enter second number :"))
# avg= (float1+float2)/2 
# print("Average is :",avg)

#Practice question 4- WAP to input 2 numbers a and b.
# Print true if a is greater than or equal to b else print false
a=input("Enter number 1 :")
b=input("Enter number 2 :")

print(a>=b)