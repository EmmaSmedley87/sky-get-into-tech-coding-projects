#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(Belgium)
print(len(Belgium))
for lineofhyphens in Belgium:
    linesofhyphens = "-"
    print(linesofhyphens, end="")

list_Belgium = Belgium.split(',')
print(list_Belgium)
print(list_Belgium[1])
print(list_Belgium[3])

new_str = ":".join(list_Belgium)
print(new_str)

new_str = ":".Belgium.replace(",",":")
print(new_str)

totalPopulationNumber = int(list_Belgium[1]) + int(list_Belgium[3])
print(totalPopulationNumber)




