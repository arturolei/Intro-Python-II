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

    def pick_up(self,new_item):
        self.items.append(new_item)
