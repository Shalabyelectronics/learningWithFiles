# open is a built-in method that open the file.
# read is a method that reading the contents inside the file.
# close is a method will close the file after done modification.
# file = open("file.txt")
# content = file.read()
# print(content)
# file.close()
# ----------------------
# There is another way to close the file and it's by using with....as keywords and it's not required adding close method

# with open("file.txt") as file:
#     content = file.read()
#     print(content)

# This about Open and reading file so How could we write and creates them?
# There are 3 modes inside open argument called mode="r" for read only mode="w" for creating and writing a new text
# by deleting the previous one and add new one.
# Last mode we learn today was mode="a" append and it will add text without effecting the previous one.
# Finally write("Anystr") will write on the file.

with open("new_file.txt", mode="w") as file:
    file.write("Hi my name is Mr:X, and I like to be hacker")

# I noticed when I open and read file I can't write with the same with...as keywords.







