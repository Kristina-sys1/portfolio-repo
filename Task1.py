Menu = {
    "new_york_style_pizza": 1200,
    "brooklyn_style_pizza": 1150,
    "chicago_deep_dish_pizza": 1050,
    "tavern_style_pizza": 1200,
    "neapolitan_pizza": 950,
    "st_louis_style_pizza": 1100,
    "buffalo_style_pizza": 900
}

print("BECKETT PIZZA PLAZA 4-for-3 Offer")
print("=================================")

x = input("Do you want to place an order? (yes/no): ").lower()

if x != "yes":
    print("Hope you order soon!")
    exit()

print("\nOur Menu:")
for item, price in Menu.items():
    print(f"- {item.replace('_', ' ').title()} : Rs.{price}")

print("\nNote: You must order EXACTLY 4 pizzas to get the offer.")

# TAKE ORDER
while True:
    order = input(
        "\nEnter 4 pizzas (comma separated, use menu names):\n"
    ).lower().split(",")

    order = [item.strip() for item in order]

    if len(order) != 4:
        print("Please enter exactly FOUR pizzas!")
        continue

    prices = []
    valid = True

    for pizza in order:
        if pizza in Menu:
            prices.append(Menu[pizza])
        else:
            print(f"Invalid pizza name: {pizza}")
            valid = False
            break

    if valid:
        break

#CALCULATION
total_without_discount = sum(prices)
cheapest_pizza = min(prices)
final_total = total_without_discount - cheapest_pizza

discount_percentage = (cheapest_pizza / total_without_discount) * 100

# OUTPUT
print("\nCheckout Summary")
print("-----------------")
print(f"Prices: {prices}")
print(f"Cheapest Pizza (FREE): Rs.{cheapest_pizza}")
print(f"Order Total: Rs.{final_total:.2f}")
print(f"Fabulous Discount: {discount_percentage:.0f}%")
