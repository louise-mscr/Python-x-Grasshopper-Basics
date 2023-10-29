import rhinoscriptsyntax as rs

meals_list = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
		},
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
		},
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
		},
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
		},
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
		},
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
		},
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
		}
]

combos_list = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    }
]


#meals_dict
meals_dict = {
	meal["name"]: meal
	for meal in meals_list
}
#meals_id_dict
meals_id_dict = {
	meal["id"]: meal
	for meal in meals_list
}
#combos_dict
combos_dict = {
	combo["name"]: combo
	for combo in combos_list
}
#circles
cir = []
cir_2 = []




def calorie_counter(*args):
    totalcalories = 0
    totalprice = 0
    for item in args:
        for meal in item:
            if meal in meals_dict:
                a = meals_dict[meal]
                totalcalories += a['calories']
                totalprice += a['price']
            elif meal in combos_dict:
                b = combos_dict[meal]
                for meal_unique in b['meals']:
                    c = meals_id_dict[meal_unique]
                    totalcalories += c['calories']
                    totalprice += c['price']
            else:
                print(meal + ' is not in the menu')
                ghenv.Component.AddRuntimeMessage(ghenv.Component.RuntimeMessageLevel.Error,('This ' + meal + ' is not in the menu'))
    
    print(totalcalories)
    print(totalprice)
    circle1=rs.AddCircle([0,0,0], totalprice)
    circle=rs.AddCircle([0,0,0], totalcalories/100)
    cir.append(circle)
    cir_2.append(circle1)
    
calorie_counter(x)