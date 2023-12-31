# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customer_order = {}

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
selection_count = 0
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected '{menu_category_name}'\n")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Input menu item number to order: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():

                # Convert the menu selection to an integer
                menu_selection_int = int(menu_selection)


                # 4. Check if the menu selection is in the menu items
                if menu_selection_int in menu_items.keys():
                    # Store the item name as a variable
                    menu_selection_name = menu_items[menu_selection_int]["Item name"]
                    menu_selection_price = menu_items[menu_selection_int]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"You chose '{menu_selection_name}', what quantity would you like of this item? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        menu_selection_quantity_int = int(quantity)
                    else:
                        menu_selection_quantity_int = 1
   
                    # Add the item name, price, and quantity to the order list
                    selection_count += 1
                    customer_order[selection_count] = {"Item name" : menu_selection_name,
                                                    "Price" : menu_selection_price,
                                                    "Quantity" : menu_selection_quantity_int
                                                        }
                else:
                   
                    # Tell the customer that their input isn't valid
                    print(f"'{menu_selection}' is not a menu option.")

            else:
                # Tell the customer they didn't select a menu option
                print(f"'{menu_selection}' is not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number, please try again.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering
        match keep_ordering.lower():
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                if selection_count > 0:
                    print("\nThank You for your order.")
                else:
                    print("\nSorry we could not serve you today.  Please visit us again.\n")
                break

            case _:

                print("invalid input.  Please try again and enter (Y)es or (N)o\n")

                # Exit the keep ordering question loop
                

                # Complete the order
                #if keep_ordering = n 
                #break
                # Since the customer decided to stop ordering, thank them for
                # their order
                #print("Thank you for your order.")


                # Exit the keep ordering question loop
               #break 

                # Tell the customer to try again
                #print("Please try again.")
if selection_count > 0:
    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Uncomment the following line to check the structure of the order
    #print(order)

    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")

    # 6. Loop through the items in the customer's order
    order_items = []
    order_item_prices = []
    order_item_quantities = []
                                                               
    for key in customer_order.keys():


        # 7. Store the dictionary items as variables
        order_items.append(customer_order[key]["Item name"])
        order_item_prices.append(customer_order[key]["Price"])                    
        order_item_quantities.append(customer_order[key]["Quantity"])
                                      
        # 8. Calculate the number of spaces for formatted printing
        num_item_spaces = 25 - len(customer_order[key]["Item name"])

        # 9. Create space strings
        item_spaces = " " * num_item_spaces
                                   
        # 10. Print the item name, price, and quantity
        print(f"{customer_order[key]['Item name']}{item_spaces} | ${customer_order[key]['Price']:5.2f} | {customer_order[key] ['Quantity']:2}")


    # 11. Calculate the cost of the order using list comprehension
    # newOrder = [item_names, menu_items, quantity, price]
    order_item_total_prices = [order_item_prices[x] * order_item_quantities[x] for x in range(len(order_items))]

                                   
    print("\n\nYour order is ready for pickup.\n")
    print("Variety Food Truck - Customer Order Receipt\n")
    print("Item name                 |  Price  | Quantity |  Item Total  ")
    print("--------------------------|---------|----------|--------------")
                                   
    for x in range(len(order_items)):
        print("{:25}  | ${:6.2f} |    {:3}    | ${:7.2f}".format(order_items[x], order_item_prices[x], order_item_quantities[x], order_item_total_prices[x]))
                                   
    order_total_price = sum(order_item_total_prices)
                                   
    dashed_line = "-" * 60
    print(f"{dashed_line}\n")
    item_spaces = " " * 34
    print(f"{item_spaces} Total Price  ${order_total_price:7.2f}\n")

    dashed_line = "-" * 60
    print(f"{dashed_line}\n")
    print("Thank You from Variety Food Truck.  Have a Great Day!\n")

# Multiply the price by quantity for each item in the order list, then sum()
  #  for newOrder:
   #     quantity.price *=
    #    save()
# and print the prices.
   # print(newOrder)
