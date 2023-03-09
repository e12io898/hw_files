from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingr_count = int(f.readline())
        ingridients = []
        for i in range(ingr_count):
            ingr, quantity, unit = f.readline().strip().split(' | ')
            ingridients.append({
                'ingredient_name': ingr,
                'quantity': int(quantity),
                'measure': unit.strip()
            })
        cook_book[dish_name] = ingridients
        f.readline()

pprint(cook_book, sort_dicts=False)