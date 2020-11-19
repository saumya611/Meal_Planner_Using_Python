from contents import pantry, recipes

# print(pantry)
# print(recipes)

display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
print(display_dict)

while True:
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_items, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_items, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_items} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} for {food_items}")
