from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None, items =[]):
        self.name = name
        self.description = description

        # As per instructions: 
        # The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
        # which point to the room in that respective direction.
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

        #Items in this room, list of Item objects, default value is []:
        self.items = items
    
    def __str__(self):
        return f"Room: {self.name} Description: {self.description}"
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    ## Methods Relating to Items in the Room:
    def get_items(self):
        return self.items
    
    # let's you set all the items in a room, useful for when you want to populate a room
    def set_items(self, new_items_list): 
        self.items = new_items_list

    #Shows you items in a room. 
    def show_items(self):
        if len(self.items) == 0:
            return "There's nothing here.\n"
        
        item_list=""
        if len(self.items) > 0:
            for item in self.items:
                item_list += f"{item} \n"
        return item_list
    
    # when you get a take or get request from player, e.g. "get matches"
    # 1) Check item exists in items in room. 
    # 2) If it exists pass it to the requester 
    # 3) Alter contents

    def on_take(self, requested_item_name):
        item_list = [item.get_name() for item in self.items]
        if requested_item_name in item_list:
            print(f"You pick up the following item: {requested_item_name}")
            item_taken = self.items[item_list.index(requested_item_name)]
            self.items.remove(item_taken)
            return item_taken
        else:
            print("You cannot have what doesn't exist")
