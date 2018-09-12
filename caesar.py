from cs50 import get_string
from cs50 import sys


if len (sys.argv) != 2:
    print ("Usage: python caesar.py key")
    # sys.exit (1)

if sys.argv[1].isalpha():
    print ("Usage: key should be a number")

filename = sys.argv[0]
key = int(sys.argv[1])
# cyphertext = []

plaintext = get_string("Enter a string: ")
print("ciphertext: ", end="")

for c in plaintext:
    if c.isalpha():
        if c.isupper():
            c = ((ord(c) - 65) + key) % 26
            c = c + 65
            c = chr(c)
            # print("chr c: ", c)
        elif c.islower():
            c = ((ord(c) - 97) + key) % 26
            c = c + 97
            c = chr(c)
            # print("chr c", c)
        else:
            print(c)
        ciphertext = c
        sys.stdout.write(c)

# for c in plaintext:
#     # See if the char is punctuation.
#     if c in string.punctuation:


print("\n")



# else:
#             print(c, end="")
#             # print(c)
#             # ciphertext = c
#             sys.stdout.write(c)




# --get the key
#   --get the plain text
#       encrypt cypher text
#           print cyper text

# encypher
#   for each character in plaintext string
#       if alphabetic
#           shift character by key
#           preserving case
