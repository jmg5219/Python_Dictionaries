#Lookup function for Brunch key in the provided dictionary
def brunch_lookup(table_order):
    for i in table_order:
        if i == "Steak and Eggs":
            brunch.append("Steak and Eggs")
        elif i == "Three Egg Breakfast" :
            brunch.append("Three Egg Breakfast")
        elif i == "Egg Benedict" :
            brunch.append("Egg Benedict")
        elif i == "Biscuit and Gravy":
            brunch.append("Biscuit and Gravy")
        elif i== "Chicken Fingers":
            brunch.append("Chicken Fingers")
        elif i == "Chicken Wrap":
            brunch.append("Chicken Wrap")
        elif i == "Steak Salad":
            brunch.append("Steak Salad")
    return(brunch)

#lookup function for Drinks key in the provided dictionary
def drink_lookup(table_order):
    for i in table_order:
        if i == "Soft Drink":
            drink.append("Soft Drink")
        elif i== "Coffee":
            drink.append("Coffee")
        elif i== "Orange Juice":
            drink.append("Orange Juice")
        elif i == "Milk":
            drink.append("Milk")
        elif i == "Water":
            drink.append("Water")
    return(drink)

#Lookup function for Special key in the provided dictionary
def special_lookup(table_order):
    for i in table_order:
        if i == "Soup of the Day":
            special.append("Soup of the Day")
        elif i == "Catch of the Day":
            special.append("Catch of the Day")
        elif i == "Chef Special":
            special.append("Chef Special")
    return(special)

#Given a list of prices, this function calculates the total price
def total_price(price):
    total_price = 0
    for i in range(0,len(price)):
        total_price = total_price + price[i]
    return total_price

#Asks user which table to checkout
table_select = int(input("Which table (1 or 2) do you want to checkout?"))
if table_select == 1:
    guests_orders = [["Egg Benedict", "Coffee"], [
"Biscuit and Gravy", "Coffee"], ["Steak and Eggs", "Soft Drink"]]
elif table_select == 2 :
    guests_orders = [["Steak Salad", "Soft Drink"], ["Soup of the Day","Chicken Wrap","Water"],["Chicken Fingers","Soft Drink"],["Chef Special"]]
#Provided dictionary
menu = {
    "Brunch" : {
        "Steak and Eggs": 16.99,
        "Three Egg Breakfast": 8.99,
        "Egg Benedict": 11.99,
        "Biscuit and Gravy": 7.99,
        "Chicken Fingers": 10.99,
        "Chicken Wrap": 8.99,
        "Steak Salad" : 1.99
    },
    "Drinks": {
        "Soft Drink": 1.99,
        "Coffee": 1.99,
        "Orange Juice": 0.99,
        "Milk": 0.55,
        "Water": 0.00
    }
}
#These are the tasks the excercise has prompted us for:
#Fix the price of the steak salad. It should be 15.99
menu["Brunch"]["Steak Salad"] = 15.99
#Add a specials menu that includes: Soup of the Day (8.99), Catch of the Day (14.99), Chef Special (15.99)
menu["Specials"] = {"Soup of the Day":8.99,"Catch of the Day":14.99,"Chef Special":15.99}
#Change "Three Egg Breakfast" to have the options of: Without Bacon (8.99) and With Bacon (9.99)
menu["Brunch"]["Three Egg Breakfast"] = {"Without Bacon":8.99, "With Bacon":9.99}

#Initializing empty lists for lookup
brunch = []
drink = []
special = []
price = []
#table = table_selector()

#loops through the different guest orders
for i in range(0,len(guests_orders)):
    table = guests_orders[i]
    #print(table)
    # Lets take the order and classify brunch, drink or special items
    brunch = brunch_lookup(table) # returns brunch items as strings
    drink = drink_lookup(table)# returns drink items as strings
    special = special_lookup(table)#returns special as strings

    #Going through the returned lists and finding the price via the menu dictionary
    print('{:<20s}{:>15s}{:>5s}'.format("--Guest %d--" % (i+1)," "," "))
    for i in brunch:
        print('{:<20s}{:>15s}{:>5s}'.format(i,"$ ",str(menu["Brunch"][i])))#Printing Brunch Items
        price.append(menu["Brunch"][i])#Appending brunch items to the price list
    for i in special:
        print('{:<20s}{:>15s}{:>5s}'.format(i,"$ ",str(menu["Specials"][i])))#Printing Special items
        price.append(menu["Specials"][i])#Appending Special items to the price list
    for i in drink:
        print('{:<20s}{:>15s}{:>5s}'.format(i,"$ ",str("{:.2f}".format(menu["Drinks"][i]))))#Printing Drinks
        price.append(menu["Drinks"][i])#Appending drink items to the price list
    print()

    brunch = []
    drink = []
    special = []


#Calculation and storing of price, tax and total price
tot_price = ("Price $ %.2f" % total_price(price))#Calling the price function to calculate total price 
taxes = ("Taxes $ %.2f" % (total_price(price)*0.07))#Calculating the tax 
tot = total_price(price)+(total_price(price)*0.07)#calculating the total price inclusive of tax
total = ("Total $ %.2f" % tot)
total25 = str("{:.2f}".format(tot * 0.25))#calculating suggested tip amounts
total15 = str("{:.2f}".format(tot * 0.15))
total20 = str("{:.2f}".format(tot* 0.20))
#Printing total price, tax and total price inclusive of tax
print('{:<20s}{:>7s}{:>3s}'.format(" "," ",tot_price))
print('{:<20s}{:>7s}{:>3s}'.format(" "," ",taxes))
print('{:<20s}{:>7s}{:>3s}'.format(" "," ",total))
print()
#Printing suggested tip amounts
print("** Suggested Tip **")
print('{:<12s}{:>1s}{:>1s}'.format("Tip 25%:","$ ",total25))
print('{:<12s}{:>1s}{:>1s}'.format("Tip 20%:","$ ",total20))
print('{:<12s}{:>1s}{:>1s}'.format("Tip 15%:","$ ",total15))