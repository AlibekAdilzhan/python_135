import os

directory = os.getcwd()

os.chdir(directory + "/" + "folder")

# cities = ["Almaty", "Astana", "Uskaman", "Aktobe"]

# with open("cities_2.txt", "w") as fo:
#     for x in cities:
#         fo.write(x + "\n")

# os.chdir(directory)

# with open("cities.txt", "w") as fo:
#     for x in cities:
#         fo.write(x + "\n")

d = os.path.split(directory)
os.chdir(d[0])
open("aaabbb.txt", "w")
print(d[0])



