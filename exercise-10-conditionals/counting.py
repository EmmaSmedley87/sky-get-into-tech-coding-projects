# counter = 0
# while counter <5:
#     print("Hello!")
#     counter += 1
#
# my_list = [0, 1, 2, 3, 4]
# for elem in my_list:
#     print("Hello from list")
#
# for i in range(0, 5, 2):
#     print("hello from range")
#
# # conditional expressions
#
# a = 4
# b = 5
# if a > b:
#     c = a
# else:
#     c = b
#
# #shortened to conditional expression
# c = a if a>b else b
#
# # unicode
# print("\N{winking face}")
#
# # print function
# name = "Emma"
# surname = "Smedley"
# num = 5
# print(name + " " + surname, end="; ")
# print(name, surname, num, sep="\U0001F600")
#
# # id name with comma,
# surname = "O'Donnell"
# surname2 = 'o\'Donnell'

#overloaded


#
# str = "Hello World"
# print(str[3.9])
# print(str[-1])
# print(str[-5:-1])
# print(str[:])

# split string

split_str = "Oranges, apples, bananas, milk"
print()

list_str = split_str.split(',')
print(list_str[1])

new_str = ":" .join(list_str)
new_str(new_str)