budget = 0
checkout = 0
available = 0
amount = 0
count = 0
subtotal = 0
total = 0
options = ["(1) Roses for $75 per half dozen, with a 25% discount.", "(2) Hair Extensions $100 per pack, with a 10% discount.", "(3) Male Denims each for $150.", "(4) Female Denims each for $175, with a 5% discount.", "(5) Jordans for $200 each."]
print(" Welcome to Crystal's Boutique! ")
print("What is your budget?")
budget = float(input())
print("You have a total of $" + str(budget) + " to spend")
while True:    #This simulates a Do Loop
    print("Here is list of items available at my store.   Select the items you wish to purchase by choosing the number that correspond with each item. When you are finished, Press 0 to checkout.")
    for list in options:
        print(list)
    itemnumber = float(input())
    if itemnumber == 0:
        print("You have successfully checked out. ")
        if available >= 0:
            grandtotal = total + total * 0.07
            print("You have " + str(count) + " items in your shopping cart.  Your Grand total is $" + str(grandtotal) + "    Thank you for shopping at Crystal's Boutique.")
        else:
            print("Your total before exceeding your budget is $" + str(checkouttotal))
    else:
        if itemnumber == 1:
            print("How many of this item would you like?")
            many = int(input())
            price = 75 * many
            subtotal = price - price * 0.25
            print("The price of the item is $ " + str(price) + " with a discount of 25%.    Your new price is $ " + str(subtotal) + ".")
        if itemnumber == 2:
            print("How many of this item would you like?")
            many = int(input())
            price = 100 * many
            subtotal = price - price * 0.10
            print("The price of the item is $ " + str(price) + " with a discount of 10%.    Your new price is $" + str(subtotal))
        if itemnumber == 3:
            print("How many of this item would you like?")
            many = int(input())
            price = 150 * many
            subtotal = price
            print("The price of the item is $ " + str(price) + " .    Your new price is $" + str(subtotal))
        if itemnumber == 4:
            print("How many of this item would you like?")
            many = int(input())
            price = 175 * many
            subtotal = price - price * 0.05
            print("The price of the item is $ " + str(price) + " with a discount of 5%.    Your new price is $" + str(subtotal))
        if itemnumber == 5:
            print("How many of this item would you like?")
            many = int(input())
            price = 200 * many
            subtotal = price
            print("The price of the item is $ " + str(price) + "     Your new price is $" + str(subtotal))
        count = count + many
        amount = budget
        available = amount - subtotal
        budget = available
        checkouttotal = total
        total = total + subtotal
        if available <= 0:
            print("Your have insufficient funds to complete this transaction. Make another selection OR press 0 to checkout.")
        else:
            print("Your remaining balance is $ " + str(available))
    if not(itemnumber != 0): break   #Exit loop
