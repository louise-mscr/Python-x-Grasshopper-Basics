calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}


def calorie_counter(*args):
    a = []
    totalcalories = 0
    for item in args:
        if item in calories:
            totalcalories += calories[item]
        else:
            combo_meals = combos[item]
            for combo_item in combo_meals:
                totalcalories += calories[combo_item]
    print(totalcalories)
    return(totalcalories)
            
calorie_counter('Salad')