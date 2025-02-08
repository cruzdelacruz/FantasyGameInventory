def add_to_inventory(inventory, added_items):
    """inventory is a dictionary, added_items is a list.
    """
    if not isinstance(inventory, dict):
        raise TypeError("Inventory muust be a dictionary")
        
    for item in added_items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
