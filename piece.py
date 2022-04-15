<<<<<<< HEAD
class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.colour} {self.x} {self.y}"

class Pion(Piece):
    pion = "P"
    value = 1

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)


class Roi(Piece):
    roi = "R"
    value = 0

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)


class Dame(Piece):
    value = 9
    dame = "D"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

class Fou(Piece):

    value = 3
    fou = "F"
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

class Tour(Piece):

    value = 5
    tour = "T"
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

class Cavalier(Piece):

    value = 3
    cavalier = "C"
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)


roi = Roi("B", 3, 2)
print(roi)
=======

>>>>>>> 01cc218 (Create piece.py)
