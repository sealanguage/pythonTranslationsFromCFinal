from cs50 import get_float

dollars = get_float("Dollars: ")
coins = 0


while(dollars <= 0):
    dollars = get_float("Dollars: ")
    print(dollars)
    break

# change dollars to cents
changeOwed = round(dollars * 100)
print(changeOwed)

while (changeOwed > 25):
    dollars = dollars % 25
    coins += 1
    changeOwed = changeOwed - 25
    print("change owed = ", changeOwed)
    print("coins = ", coins)
while (changeOwed > 10):
    dollars = dollars % 10
    coins += 1
    changeOwed = changeOwed - 10
    print("change owed = ", changeOwed)
    print("coins = ", coins)
while (changeOwed > 5):
    dollars = dollars % 5
    coins += 1
    changeOwed = changeOwed - 5
    print("change owed = ", changeOwed)
    print("coins = ", coins)
while (changeOwed > 1):
    dollars = dollars % 1
    coins += 1
    changeOwed = changeOwed - 1
    print("change owed = ", changeOwed)
    print("coins = ", coins)




# # prints Hello Geek 3 Times
# count = 0
# while (count < 3):
#     count = count+1
#     print("Hello Geek")



# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
