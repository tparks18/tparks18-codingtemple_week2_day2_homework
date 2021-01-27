# 1) Build a Shopping Cart
#   Should have the following capabilities:
#    1) Takes in input
#    2) Stores user input into a list
#    3) User can add or delete items
#    4) User can see current shopping list
#    5) Loops until user 'quits'
#    6) Upon quiting the program, print out all items in the user's list

# start with an empty dictionary to represent the shopping cart
shopping_cart = {}

# commands

print("Shopping Cart Actions")
print("1: Add item")
print("2: Remove item")
print("3: View basket ")
print("0: Stop shopping")


# ask what they're doing
action = int(input("Enter an action: "))
# start the while loop
while action != 0:
    # what will it do for each option?
    if action == 1:
        # inputs
        item = input("What are you getting? ")
        quantity = int(input("How many items? "))
        # line to add the items to the cart
        shopping_cart[item] = quantity
    elif action == 2:
        item = input("What are you deleting? ")
        del(shopping_cart[item])
    elif action == 3:
        print(shopping_cart)
    elif action != 0:
        print("Please select a valid action!")
        # go back to the beginning
    action = int(input("Enter an action: "))
    # terminate program
else:
    print("You are ready for checkout.")
