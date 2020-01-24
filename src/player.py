# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name 
        self.current_room = current_room
        self.items = items # player now has items/inventory

    def __str__(self):
        return f"Player: {self.name}, Current Room: {self.current_room}"
    
    def get_name(self):
        return self.name

    # Get room info. 
    def get_room(self):
        return self.current_room

    # Set current room. 
    def set_room(self, new_room):
        self.current_room = new_room 

    # Get pick up item
    def pickup_item(self,new_item):
        if new_item != None:
            self.items.append(new_item)
        else:
            print("You cannot take what is not there.")

    # Drop item 
    def drop_item(self,dropped_item_name):
        item_list = [item.name for item in self.items]
        if dropped_item_name not in item_list:
            return None
        else:
            dropped_item = self.items[item_list.index(dropped_item_name)]
            self.items.remove(dropped_item)
            print(f"Dropping {dropped_item.get_name()}")
            return dropped_item

    # Get list of items a player has
    def get_items(self):
        if len(self.items) == 0:
            return f"You got nothing, {self.name}!"
        items_list = f"\nHere is what you have, {self.name}: \n"
        for item in self.items:
            items_list += f"{item} \n"

        return items_list
