# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name 
        self.current_room = current_room

    def __str__(self):
        return f"Player: {self.name} Current Room: {self.current_room}"
    
    # Fix later; add move method

    # Get room info. 
    def get_room(self):
        return self.current_room

    # Set current room. 
    def set_room(self, new_room):
        self.current_room = new_room 



    def move(self):

        pass

