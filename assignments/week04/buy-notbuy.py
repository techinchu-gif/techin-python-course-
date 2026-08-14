prices = []

print("Enter prices of 6 items:")

for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

print()

budget = int(input("Enter total budget: "))

print()

total_spent = 0
bought_items = []

for i in range(len(prices)):
    item_no = i + 1
    price = prices[i]

    if total_spent + price <= budget:
        total_spent += price
        bought_items.append(price)
        print(f"Item {item_no} = {price} -> buy")
        print(f"Current total = {total_spent}")
    else:
        print(f"Item {item_no} = {price} -> cannot buy")
        print(f"Current total = {total_spent}")

    print()

print(f"Bought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {budget - total_spent}")