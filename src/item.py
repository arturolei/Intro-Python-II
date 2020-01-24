class Item:
    def __init__(self,name, description = "Not worth describing"):
        self.name = name #should be one word for parsing's sake
        self.description = description
    
    def get_name(self):
        return self.name 
    
    def get_description(self):
        return self.description

    def __str__(self):
        return f"Item name: {self.name},  Item Description: {self.description}"

    # I do not think we will need setters here (players can't change items
    # but it might be good to have this--maybe wizards can change items' attributes

    def set_name(self, new_name):
        self.name = new_name
    
    def set_description(self, new_description):
        self.description = new_description
    

        