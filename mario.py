from cs50 import get_int

height = get_int("Height: ")
heightN = height
rowP = height
space = rowP

while (height < 1 or height > 23):
    print("Usage: height between 1 and 23")
    break

while (height > 1 and height < 23):
    print("value of height = ", height)

# for every row in height
# print spaces height - 1
# print hashes remainder of spaces - height
# print a new line

    # for height number of rows
    for rowP in range(1, (height + 1), 1):
        rowP = rowP
        print("^ " * (height - rowP), end = "")

        # for space in range(rowP, 1, -1):
        print("# " * (rowP)),

    break






