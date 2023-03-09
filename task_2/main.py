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

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list, bufer = {}, []
    for dish_name in dishes:
        for b in cook_book[dish_name]:                # b - состав ингредиента
            ingr_name, s = b['ingredient_name'], 1    # s - количество
            if ingr_name in bufer:
                s = ingr_list[ingr_name]['quantity'] + \
                    person_count * b['quantity']
            else:
                bufer.append(b['ingredient_name'])
                s = person_count * b['quantity']
            ingr_list[ingr_name] = {'measure': b['measure'], 'quantity': s}
    pprint(ingr_list)

#test
get_shop_list_by_dishes(['Омлет', 'Фахитос', ], 2)