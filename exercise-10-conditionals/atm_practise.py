import getpass, sys

pin = "3241"
tries = 0
max_tries = 3

while tries < 3:
    supplied_pin = getpass.getpass('Enter your PIN')
    print(supplied_pin)
    if supplied_pin == pin:
        print("PIN entry is successful")
        break
    else:
        print("PIN incorrect")
        print("You have had", tries + 1, "attempt of 3")
    tries = tries + 1
    if max_tries == tries:
        print("You have reached your max number of tries")

    # print("You have had", tries, "of", max_tries)
    # print("You have", tries, "attempts remaining")

# don't use while number = True
# while number != 5:
#     number = input("Give me a number: ")