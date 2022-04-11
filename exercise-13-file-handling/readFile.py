# slurping a file
# prints as a string
# pelicanFile = open('pelican.txt').read()
# print(type(lines))
# print(lines)

# reading a file as a list
pelicanFile = open("pelican.txt", "r")
# print(len(pelicanFile.readlines()))
# pelicanFile.close()

# loop to iterate and print
# end="" avoids blank lines showing in terminal
for eachLine in pelicanFile:
    print(eachLine, end="")

