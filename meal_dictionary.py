meal = {
    "Drink":"Coke",
    "Appetizer":"Chips",
    "Entree":"Tacos",
    "Dessert":"Churros"
}

print('This Thursday I will have %s and %s for dinner' % (meal['Drink'],meal["Entree"]))

if "Dessert" in meal:
    print('Of Course I will have Dessert')
    meal["Dessert"]="ice-cream"
    print(meal)
    del meal["Dessert"]
    print(meal)
else:
    print('Need to find some dessert')
    # meal['Dessert'] = "Churros"
    # print(meal)