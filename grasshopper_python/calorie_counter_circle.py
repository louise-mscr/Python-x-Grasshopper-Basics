#RADIUS OF CIRCLE DEPENDING ON NUMBER OF CALORIES
#The more calories, the bigger the circle

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghc 


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

a = []

def calorie_counter(*args):
    totalcalories = 0
    for item in args:
        for meal in item:
            if meal in calories:
                totalcalories += calories[meal]
            else:
                combo_meals = combos[meal]
                for combo_item in combo_meals:
                    totalcalories += calories[combo_item]
    print(totalcalories)
    circle=rs.AddCircle([0,0,0], totalcalories/100)
    a.append(circle)
            

calorie_counter(x)