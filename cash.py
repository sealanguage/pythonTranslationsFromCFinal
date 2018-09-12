from cs50 import get_float

dollars = get_float("Dollars: ")
coins = 0


while(dollars < 0.00):
    dollars = get_float("Dollars: ")
    break

# change dollars to cents
changeOwed = dollars * 100

while (changeOwed >= 25):
    dollars = dollars % 25
    coins += 1
    changeOwed = changeOwed - 25
    print(coins)
while (changeOwed >= 10):
    dollars = dollars % 10
    coins += 1
    changeOwed = changeOwed - 10
    print(coins)
while (changeOwed >= 5):
    dollars = dollars % 5
    coins += 1
    changeOwed = changeOwed - 5
    print(coins)
while (changeOwed >= 1):
    dollars = dollars % 1
    coins += 1
    changeOwed = changeOwed - 1
    print("Coins: ", coins)
    # print()
    break