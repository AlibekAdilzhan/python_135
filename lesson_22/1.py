# planets = ["The Earth", "The Sun", "Jupyter", "Mars", "Saturn", "Uranus"]
cities = ["Taraz", "Oral", "Tulkibas", "Taldykorgan"]

# with open("cities_2.txt", "a") as fo:
#     for x in cities:
#         fo.write(x + "\n")

fo = open("cities_2.txt", "a")

for x in cities:
    fo.write(x + "\n")

fo.close()