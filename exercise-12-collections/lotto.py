
# randomNumber = (int(random.randint(0,50)))
# randomNumberLimit = 6
# print(random.randint(0,50))
# while randomNumberLimit <= 6:
#     print(randomNumber)

#while loop to generate 6 unique random numbers
import random

setOfGeneratorNumbers = set()
while len(setOfGeneratorNumbers) < 6:
    setOfGeneratorNumbers.add(random.randint(0, 50))
    print(setOfGeneratorNumbers)