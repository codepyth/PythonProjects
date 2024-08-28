# name = "waseem"
# name1 = "Waseem"
# name == name1

# print(name == name1)

# num_string = '12'
# num_integer = 23


# print(num_string)
# print("Data type of num_string before Type Casting:",type(num_string))

# # explicit type conversion
# num_string = int(num_string)

# print("Data type of num_string after Type Casting:", num_string, type(num_string))

# num_sum = num_integer + num_string

# print("Sum:",num_sum)
# print("Data type of num_sum:",type(num_sum))

# mylist = [3, 10, 7, 6, 2]
# myset = set()
# ordered_unique_list = []
# for item in mylist:
#     if item not in myset:
#         ordered_unique_list.append(item)
#         myset.add(item)

# print(myset)
# print(ordered_unique_list)  # Output: [7, 5, 10, 2]


# create a dictionary named capital_city
# capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

# print(capital_city['Nepal'])  # prints Kathmandu

# print(capital_city['Italy'])  # throws error message 


# print("was", "hu", sep=".")

# x = 4
# t = 44

# print(t//x)

# a = 20
# a **= 4
# print(a)


# a = 5

# b = 2

# # equal to operator
# print('a == b =', a == b)

# # not equal to operator
# print('a != b =', a != b)

# # greater than operator
# print('a > b =', a > b)

# # less than operator
# print('a < b =', a < b)

# # greater than or equal to operator
# print('a >= b =', a >= b)

# # less than or equal to operator
# print('a <= b =', a <= b)


# ternary operator

# result = 3 if 3>5 else 5

# print(result)

# logical AND
# print(True and True)     # True
# print(True and False)    # False

# # logical OR
# print(True or False)     # True

# # logical NOT
# a = 3
# b= 4
# x = a != b

# print(x)

# print( not True)          # False


# number = int(input('Enter a number: '))

# # check if number is greater than 0
# if number > 0:
#     print(f'{number} is a positive number.')
# else:
#     print(f"{number} is a negative number")

# print('A statement outside the if statement.')

# x = 1
# total = 2

# # start of the if statement
# if x >= 0:
#     total += x
#     print(total)  
# # end of the if statement

# print("This is always executed.")

# languages = ['Swift', 'Python', 'Go']

# # access elements of the list one by one

# # print(len(languages))
# print(range(languages))


# for lang in range(languages):
#     print(lang)


# print(range(len(languages)))

# iterate from i = 0 to i = 3
# for i in range(4):
#     print(i)


# languages = ['Swift', 'Python', 'Go']

# languages.extend(["shaka"])
# print(languages)

# languages = ['Python', 'Swift', 'Python', 'Go']
# languages.remove('Python')
# print(languages)  # Output: ['Swift', 'Go']


# languages = ['Swift', 'Python', 'Go']
# index_of_python = languages.index('Python')
# print(index_of_python)  # Output: 1


# languages = ['Swift', 'Python', 'Go', 'Python']
# python_count = languages.count('Pyt')
# print(python_count)  # Output: 2



# Explaintations of shallow copy:
# import copy

# # Original list with a nested list
# original_list = [1, 2, [3, 4]]

# # Create a shallow copy of the original list
# shallow_copied_list = copy.copy(original_list)

# # Modify a top-level element in the shallow copy
# shallow_copied_list[0] = 'New'
# print("Original list:", original_list)   # Output: [1, 2, [3, 4]]
# print("Shallow copied list:", shallow_copied_list)  # Output: ['New', 2, [3, 4]]

# # Modify a nested element in the shallow copy
# shallow_copied_list[2][0] = 'Modified'
# print("Original list:", original_list)   # Output: [1, 2, ['Modified', 4]]
# print("Shallow copied list:", shallow_copied_list)  # Output: ['New', 2, ['Modified', 4]]



# import copy

# # Original list with a nested list
# original_list = [1, 2, [3, 4]]

# # Create a deep copy of the original list
# deep_copied_list = copy.deepcopy(original_list)

# # Modify a top-level element in the deep copy
# deep_copied_list[0] = 'New'
# print("Original list:", original_list)   # Output: [1, 2, [3, 4]]
# print("Deep copied list:", deep_copied_list)  # Output: ['New', 2, [3, 4]]

# # Modify a nested element in the deep copy
# deep_copied_list[2][0] = 'Modified'
# print("Original list:", original_list)   # Output: [1, 2, [3, 4]]
# print("Deep copied list:", deep_copied_list)  # Output: ['New', 2, ['Modified', 4]]

# Inshort:

# Shallow copy:
# it creates a new object but any changes in nested elements of new copy from shallow list, will also effect the original list.
# Deep copy:
# it creates a totally new object and any changes to the new copy will not effect the main or original list.


# mylist = [1, 3, 4, 5, 7]

# newlist = [x/2 for x in mylist]

# print(newlist)

# t = (1, "hello", 3.14)
# print(t[1][1])  # prints "hello"
# for element in t:
#     print(element)  # prints each element in the tuple

# t = (1, "hello", 3.14)
# print(t[1][4])



# print("Twinkle, twinkle, little star,")
# print("\t How I wonder what you are! ")
# print("\t \t Up above the world so high,  ") 		
# print("\t \t \t Like a diamond in the sky.") 
# print("Twinkle, twinkle, little star,") 
# print("\t How I wonder what you are")

# import sys

# print(sys)
# print('python version: ', sys.version)
# print('system version: ', sys.version_info)


# date and time module

# from datetime import datetime, date
# import time

# print(date.today())

# print(time.strftime("%H:%M:%S"))

# print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))



# A = pi r square


# r = 1.1
# pi = 3.141592653589793


# a = pi*r**2
# print(a)


# from math import pi

# print(pi)

# # radius = float(input("Enter radius: "))
# radius = 1.1

# area = pi*r**2

# print(area)


# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# fname = 'Waseem'
# lname = 'Nawaz'
# fulname = fname +' '+ lname

# # print(fulname)

# word = ''
# result = ''


# for char in fulname:
#     if char != ' ':
#         word += char
#     else:
#         for i in range(len(word)-1, -1, -1):
#             result += word[i]
#         result += ' '
#         word = ''

# for i in range(len(word)-1, -1, -1):
#     result += word[i]


# print(result)


# mynumber = input("Enter Numbers to generate a list and tuple: ")

# mylist = []
# mytuple = ()
# print(len(mynumber))
# while mynumber:
#     if mynumber == ",":
#         pass
#     else:
#         mylist += mynumber
#         mytuple += mynumber


# print(mylist)
# print(mytuple)


# from wifi_qrcode_generator import wifi_qrcode

# qr_code = wifi_qrcode('Khuda Ka Khouf Kro', hidden=False, authentication_type='WPA', password='ijazdon1')

# qr_code_image = qr_code.make_image()

# qr_code_image.save('my_qr_code.jpg')


# mylist = input("Enter numbers: ")
# newlist = mylist.split(',')

# newtuple = tuple(newlist)


# print("List: ", newlist)
# print("Tuple: ", newtuple)


# var = ["code.java", "serew.ve", "wjerlje.jsd", "pisc.jpeg"]

# extenlist = []

# for data in var:
#     newvar = data.split('.')
#     print(newvar)
#     extenlist.append(newvar[-1])

# print(extenlist)


# color_list = ["Red","Green","White" ,"Black"]

# last_color = len(color_list)

# print(color_list[0]+ " "+ color_list[-1])


# Define a tuple called 'exam_st_date' containing the exam start date in the format (day, month, year)
# exam_st_date = (11, 12, 2014)

# result =''

# for i in exam_st_date:
#     result += str(i)+'/'

# result = result.rstrip('/')
# print(result)


# from datetime import date


# date1 = date(2014, 7, 11)
# date2 = date(2014, 7, 2)


# delta = date1 - date2

# print(delta.days)

# from math import pi


# rad = 6

# data = pi*rad**3

# result = data*(4/3)

# print(result)


# number1 = 23

# number2 = 17

# if number1>number2:
#     result = number1-number2
#     result *= 2
#     print(result)
# else:
#     result = number1-number2
#     print(abs(result))


# var = [2, 5, 4, 8]

# newlee = [x*2 for x in var]
# print(newlee)

# num = 5
# result = 1
# for i in range(1, num+1):
#     for x in range(i):
#         x = x*x
#         result += x

    

# print(result)


# finding factors of a number

# number = 8

# number_divided = number//2

# all_factors = []

# for i in range(1, number_divided+1):
#     if number_divided%i == 0:
#         all_factors.append(i)


# all_factors.append(number)
# print(all_factors)


import time

# # Start the timer
# start_time = time.time()

# # Your code here
# number = 8
# all_factors = []

# for i in range(1, number//2 + 1):
#     if number % i == 0:
#         all_factors.append(i)

# all_factors.append(number)

# print(all_factors)

# # End the timer
# end_time = time.time()

# # Calculate the time taken
# total_time = end_time - start_time

# print(f"Time taken: {total_time} seconds")
# Write a Python program to calculate the difference between a given number and 17.
#  If the number is greater than 17, return twice the absolute difference.


# mynum = int(input("Enter a number: "))


# print(f"Number {mynum} is in between 100 and 1000" if
#       mynum >=100 and mynum <=1000 else 
#       f"Given Number {mynum} is in between 1000 and 2000" 
#       if mynum >= 1000 and mynum < 2000 else "Wrong Input"
#       )

# Ternary operator in python
# print("I am Pro Programmer" if 2==2 else "I am Just Noob")

# Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.


# numlist = []
# x = 1
# while x<4:
#     numlist.append(int(input("Enter a Number: ")))
#     x += 1
    
# sum = 0

# for i in range(len(numlist)):
#     sum += numlist[i]

# all_same = True
# for i in range(1, len(numlist)):
#     if numlist[i] != numlist[0]:
#         all_same = False
#         break

# if all_same:
#     sum *= 3
# else:
#     print("\nAll entered Numbers aren't same")
    

# print("Sum is: ", sum)
# print("Entered Numers: ", numlist)



# mystr = input("Enter string: ")


# if mystr.startswith('is'):
#     print(mystr)
# else:
#     mystr = 'is ' + mystr
#     print(mystr)


# Write a  Python program that returns a string that is n (non-negative integer) copies of a given string.
# import time

# startf = time.time()

# print("InshaALlah, i will successfully start Python Django development role job from next(September) month.")
# print("InshaALlah, i will successfully start Python Django development role job from next(September) month.")
# print("InshaALlah, i will successfully start Python Django development role job from next(September) month.")
# print("InshaALlah, i will successfully start Python Django development role job from next(September) month.")

# endf = time.time()

# print("Total time taken: ", endf-startf)


# mystri = input("Enter string sentence: ")

# howmany = int(input("Enter a number: "))
# starts = time.time()
# for i in range(howmany):
#     print(mystri)
    
# ends = time.time()


# print("Total time taken: ", ends-starts)


# Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.


# number = int(input("Enter a number: "))

# print('Given number is Even' if number%2==0 else "Number is Odd bro")

#  Write a  Python program to count the number 4 in a given list.

# mylist = [3, 8, 4, 9, 4, 7, 4]


# number_count = 0
# number = 4


# for i in range(len(mylist)):
#     if mylist[i]==number:
#         number_count += 1
        

# print(number_count)


# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2.


# my_data = [1, 4, 2, 5, 4, 7, 4]

# numb = 4
# times = 0

# for i in my_data:
#     if numb == i:
#         times += 1
    

# print(times)

