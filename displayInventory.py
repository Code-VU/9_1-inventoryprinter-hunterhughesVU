stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print("Inventory: ")

    for itemType, item in stuff.items():
        print(item, itemType)


    print("Total number of items:", sum(stuff.values()))

##displayInventory(stuff)