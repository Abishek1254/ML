marks=[90,80,70,60,50,40]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])

# student=["karan",95.4,17,"Delhi"]
# print(student)

#list slicing - ending index is not included
# print(marks[1:4])
# print(marks[-5:-1])

# list methods
# marks.append(30) # adds 100 at the end of the list
# print(marks)

# marks.sort() # sorts the list in ascending order
# print(marks)

# marks.sort(reverse=True) # sorts the list in descending order
# print(marks)

# marks.reverse() # reverses the list
# print(marks)

# marks.insert(0,31) # inserts 31 at index 0 and shifts the rest of the elements to the right
# print(marks)

# tuples
# tup=(1,2,3,4,5)
# print(type(tup))
# print(tup[0])
#tup[0]=10 # tuples are immutable, we cannot change the value of a tuple

# tup1=("ram",10,90.5)
# print(type(tup1))
# print(tup1.index("ram")) # returns the index of the first occurrence of "ram" in the tuple
# print(tup1.count(10)) # returns the number of times 10 appears in the tuple

# tup2=(1)
# print(type(tup2)) # this is not a tuple, it is an integer

# tup3=(1,)
# print(type(tup3)) # this is a tuple with one element

# movie1=input("Enter the name of the movie: ")
# movie2=input("Enter the name of the movie: ")
# movie3=input("Enter the name of the movie: ")

# movies=[movie1,movie2,movie3]

# for movie in movies:
#     print(movie,end=" ")

# list1=[1,2,"abc",3.4,"abc",2,1]
# list2=list1.copy() # returns a shallow copy of the list

# i=0
# j=len(list1)-1

# while i<=j:
#     if (list1[i]!=list2[j]):
#         print("Not a palindrome")
#         break
#     i+=1
#     j-=1
# else:
#     print("Palindrome")


# grades=('C','D','A','A','B','B','A')
# list=[]

# for grade in grades:
#     list.append(grade)

# list.sort()
# print("Grade A count:", list.count('A')) # returns the number of times 'A' appears in the list

# for grade in list:
#     print(grade,end=" ")