import os

src = os.getcwd()
# dst = src + "/" + "Folder bridge"
dst = os.path.join(src, "Folder bridge")
os.chdir(dst)
open("cities_3.txt", "w")