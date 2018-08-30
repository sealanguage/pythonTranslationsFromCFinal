from cs50 import get_float

dollars = get_float("Dollars: ")
coins = 0
changeOwed = round(dollars)
# print("ROUND changeOwed: ", changeOwed)

# if(dollars >= 1):
#     changeOwed = round(dollars * 100)
#     print(changeOwed)
#     # print("ROUND changeOwed: ", changeOwed)

# #     dollars = get_float("Dollars: ")
# #     changeOwed = round(dollars * 100)
# #     print("THIS IS INPUT ", dollars)

# elif (dollars > 0 or dollars < 1):
#     changeOwed = int(dollars * 100)
#     round(changeOwed, 0)
#     # print("changeOwed < 1: ", changeOwed)

# elif (dollars <= 0):
#     dollars = get_float("Dollars: ")



# change dollars to cents
changeOwed = round(dollars * 100)
print(changeOwed)
print("ROUND changeOwed: ", changeOwed)

# change dollars to cents
# changeOwed = round(dollars)

while (changeOwed > 25):
    dollars = dollars % 25
    coins += 1
    changeOwed = changeOwed - 25
    # print(changeOwed)
    print(coins)
while (changeOwed > 10):
    dollars = dollars % 10
    coins += 1
    changeOwed = changeOwed - 10
    print(changeOwed)
    print(coins)
while (changeOwed > 5):
    dollars = dollars % 5
    coins += 1
    changeOwed = changeOwed - 5
    print(changeOwed)
    print(coins)
while (changeOwed > 1):
    dollars = dollars % 1
    coins += 1
    changeOwed = changeOwed - 1
    print(changeOwed)
    print(coins)
    print()
    break