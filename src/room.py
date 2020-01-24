# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description

        # As per instructions: 
        # The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
        # which point to the room in that respective direction.
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    
    
    def __str__(self):
        return f"Room: {self.name} Description: {self.description}"
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description