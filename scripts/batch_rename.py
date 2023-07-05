import os

path = os.chdir("images/original/bricks")

i = 1
for file in os.listdir(path):

    new_file_name = "bricks_{}.JPEG".format(i)
    os.rename(file, new_file_name)

    i = i + 1