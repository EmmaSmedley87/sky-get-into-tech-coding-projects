pelicanFile = open("pelican.txt", "a")
# pelicanFile.write("\n A wonderful bird is the pelican")
pelicanFile.write("\n His bill hold more than is belican")

# \n is require so each string goes on a new line in the pelican.txt file
lines = ["He can take in his break, \n", " Enough food for a week,\n", " But damned if I see how the helican.\n"]
pelicanFile.writelines(lines)

pelicanFile.close()