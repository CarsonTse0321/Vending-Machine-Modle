print("Menu")

print("----------------------------------------------------------")

menu = {
    "espresso": 50,
    "latte": 50,
    "cappuccino": 50,
    "coffee": 50,
    "tea": 15,
    "milk": 20,
    "water": 10,
    "potato chips": 30,
    "chocolate": 30}

for items, price in menu.items():
    print(f"{items}, ${price}")

shopping_cart = []
money = []

print("----------------------------------------------------------")

print("Order (input q to stop ordering)")
print("----------------------------------------------------------")

while True:
    food = input("What would you like to order? ").lower()
    if food == "q":
        break
    elif food not in menu:
        print("Sorry, we don't have that.")
        continue
    else:
        shopping_cart.append(food)
        money.append(menu.get(food))

print("----------------------------------------------------------")

print("Your order is:")
print("----------------------------------------------------------")

for index, food in enumerate (shopping_cart):
    print(f"{index + 1}. {food}")

print("----------------------------------------------------------")

print("Your total:")
for index, price in enumerate (money):
    print(f"{index + 1}. ${price}")

print(f"Total: ${sum(money)}")
print("----------------------------------------------------------")