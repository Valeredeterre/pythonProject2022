class Player:
    def __init__(self, pseudo, colour):
        self.pseudo = pseudo
        self.colour = colour
    
    def __repr__(self):
        return self.pseudo