stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print("Inventory:")

    #This is to re order to match desired output.
    #for key in ['apple','gold coin','rope','torch','ring']:
   #     stuff[key] = stuff.pop(key)

    #Print the inventory
    for item in inventory:
        print(inventory[item], item)

    #Print total
    print("Total number of items:", sum(inventory.values()))

##displayInventory(stuff)