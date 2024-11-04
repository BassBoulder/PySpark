"""Functions to keep track and alter inventory."""
from collections import Counter

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    return Counter(items)


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    inventory = create_inventory(inventory)
    items = create_inventory(items)
    
    return items + inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    inventory = create_inventory(inventory)
    items = create_inventory(items)

    for key in inventory:
        if inventory[key] - items[key] <= 0:
            inventory[key] = 0
        else:
            inventory[key] = inventory[key] - items[key]
            
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory = create_inventory(inventory)

    if item in inventory: 
        inventory.pop(item)
    
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    
    return [(item, key) for item, key in inventory.items() if key > 0]
