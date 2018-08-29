from cs50 import get_int

height = get_int("Height: ")

while (height < 0 or height > 23):
    print("Usage: height between 1 and 23")
    height = get_int("Height: ")

rowP = height

while (height >= 1 and height < 24):

    # for every row in height
    # print spaces height - 1
    # print hashes remainder of spaces - height
    # print a new line

    # for height number of rows
    for rowP in range(1, (height + 1), 1):
        rowP = rowP
        print(" " * (height - rowP), end="")

        # for space in range(rowP, 1, -1):
        print("#" * (rowP), end="#\n"),

    break