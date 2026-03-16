def add_ingredient(inventory, ingredient, amount):
    if ingredient not in inventory:
        i={}
        i[ingredient]=amount
        inventory.update(i)
    else:
        inventory[ingredient]+=amount
    return inventory
def brew_potion(inventory, recipes, potion_name):
    if potion_name in recipes:
        c=0
        for i in recipes[potion_name]:
            for j in inventory:
                if i==j:
                    if recipes[potion_name].get(i)<=inventory.get(j):
                        c+=1
                        inventory[j]-=recipes[potion_name][i]
                    else:
                        return False
        if c==len(recipes[potion_name]):
            return True
    else:
        return False
inventory={
    "herb": 3,
    "water": 5,
    "mushroom": 2,
    "crystal": 0
}
recipes={
    "health_potion": {"herb": 2, "water": 1},
    "mana_potion": {"crystal": 1, "water": 2},
    "invisibility_potion": {"mushroom": 3, "water": 2, "herb": 1}
}
