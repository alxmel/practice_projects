"""
A.M.

Inventory system for fantasy games.
Created to practice Python dictionaries, lists, for, if & while loops.
"""
import pprint

inventory = {}

new_loot = []

print()
print('Hello! Welcome to the interactive inventory tracker!')


# Defining function that will be used to print out the inventory.
def display_inventory(inv_items):
    print('CURRENT INVENTORY'.center(20 + 20, '-'))
    print()
    for k, v in inv_items.items():
        print(k.ljust(30, '.') + str(v).rjust(1))
    print()
    print('-'.center(20 + 20, '-'))


while True:
    print()
    print('Type "1" to print out your inventory, "2" for updating your inventory, "3" for adding new boss loot (once defeated), or "exit" to quit:')
    choice = input()
    if choice.lower() == 'exit':
        print()
        print('Thanks for using the Fantasy Inventory System!')
        break
    elif choice == '1':
        print()    # Blank print statements added for output readability
#        pprint.pprint(inventory, width=1) ### Commented out in favor for using string justification to print inventory
        display_inventory(inventory)
        print()
    elif choice == '2':
        print()
        while True:
            print('Please enter the item name to add or deduce from the inventory ("return" to return to main menu):')
            key = input().lower()
            print()
            if key == 'return':
                break
            print('Now enter the quantity (negative subtracts from current inventory quantity):')
            value = input()
            inventory.setdefault(key, 0)
            if value == '-*':
                inventory[key] -= int(value)
                print()
            else:
                inventory[key] += int(value)
                print()
    elif choice == '3':
        print()
        new_loot = []
        while True:
            print('Please enter the name of item #' + str(len(new_loot) + 1) + ' (enter blank to complete list):')
            new_item = input()
            if new_item == '':
                break
            new_loot = new_loot + [new_item]
            print()
        for item_to_inventory in new_loot: 
            inventory.setdefault(item_to_inventory, 0)
            inventory[item_to_inventory] += 1 
        print()
    else:
        print()
        print('incorrect option, returning to main menu')
        continue


