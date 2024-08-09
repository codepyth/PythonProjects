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

from datetime import datetime, date
import time

print(date.today())

print(time.strftime("%H:%M:%S"))

print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
