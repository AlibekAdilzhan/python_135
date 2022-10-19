import shutil
import os

src = os.getcwd()

old_dst = src + "/Folder garden/cities.txt"
new_dst = src + "/lesson_22/Folder bridge/cities.txt"

shutil.copyfile(old_dst, new_dst)