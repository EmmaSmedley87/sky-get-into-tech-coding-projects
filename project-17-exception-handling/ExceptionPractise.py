# exception practise
# dividing by zero exception alert
#
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by 0!")
# except ValueError:
#     print("Enter only number please!")
# except Exception:
#     print("Something went wrong :(")

# exception as e
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")