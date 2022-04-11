# def calculate():
#     operation = input('''
# Please type in the maths operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
# # use float to get on whole numbers instead of int
#     number_1 = int(input('Enter your first number: '))
#     number_2 = int(input('Enter your second number: '))
#
#
# #addition
#     if operation == '+':
#         print('{} + {} = '.format(number_1, number_2))
#         print(number_1 + number_2)
#
# #subtraction
#     elif operation == '-':
#         print('{} - {} = ' .format(number_1, number_2))
#         print(number_1 - number_2)
#
# #multiply
#     elif operation == '*':
#         print('{} * {} = ' .format(number_1, number_2))
#         print(number_1 * number_2)
#
# #divide
#     elif operation == '/':
#         print('{} / {} = ' .format(number_1, number_2))
#         print(number_1 / number_2)
#
#     else:
#         print('You have not typed a valid operator, please run the program again.')
#
# # Define a function to ask user if they want to use the calculator again
# def again():
#
# # Take user input
#     calculate_again = input('''Would you like to do another calculation? Please type Y for Yes and N for no.''')
#
# # If user types Y or y calculate again, .upper allows lower case input to be accepted
#     if calculate_again.upper() == 'Y':
#         calculate()
#
# # If user types N, say goodbye to user and end program, again .upper allows lower case input to be accepted
#     elif calculate_again.upper() == 'N':
#         print("Goodbye.")
#
# # If user types another key, run function again
#     else:
#         again()
#
# # Call calculate function
# calculate()

calculate = [int(calculation) for calculation in input("Enter multiple values: ").split()]
print("Number of list is: ", calculate)

if calculation == "+":
    print(' {} + {} = '.add(input(calculate)))




