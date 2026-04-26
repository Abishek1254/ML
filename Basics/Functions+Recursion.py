# sum of 2 numbers
# def sum(a,b):
#     mysum=a+b
#     return mysum
# print(sum(14,35))


# average of 3 numbers
# def calc_average(a,b,c):
#     avg= (a+b+c)/3 
#     return avg
# print("Average :",calc_average(10,12,14))

# default parameters - all the default parameters must follow the non-default ones
# def product(a,b=2):
#     return a*b
# print(product(5))

# function to print the length of a list
# def length(list):
#     return len(list)

# print items in a list
# def printList(list) :
#     for item in list:
#         print(item,end=" ")

# cities=["delhi","mumbai","hyderabad","noida"]
# printList(cities)
# print("Length= ",length(cities))

# factorial of n
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print('Factorial :',fact)

# factorial(5)

# prints n to 1 backwards
# def f(n):
#     if(n==0):
#      return 
    
#     print(n)
#     f(n-1)

# f(5)

# n!
# def factorial(n):
#     if(n==0):
#      return 1
    
#     return n*factorial(n-1)


# sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    
    return n+sum(n-1)

print(sum(10))