"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    my_dict = {}

    for item in items:
        if item in my_dict:
            my_dict[item] = my_dict[item] + 1
        else:
            my_dict[item] = 1
    return my_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    expanded_items = []

    for key, value in inventory.items():
        print(key, value)
        expanded_items.extend([key] * value)
        
    expanded_items.extend(items)
    
    return create_inventory(expanded_items)


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for key in inventory:
        count = items.count(key)
        if inventory[key] <= count:
            inventory[key] = 0
        else:
            inventory[key] -= count
    return inventory

print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    
    new_dict = {}
    
    for item in inventory:
        if inventory[item] != 0:
            new_dict[item] = inventory[item]
    
    return list(new_dict.items())