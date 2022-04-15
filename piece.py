class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y

    def __str__(self):
        return f" Equipe : {self.colour} \n Position : ({self.x}, {self.y})"

class Pion(Piece):
    pion = "P"
    value = 1

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)


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

    def __repr__(self):
        super.__repr__(self)

class Fou(Piece):

    value = 3
    fou = "F"
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

class Tour(Piece):

    value = 5
    tour = "T"
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

class Cavalier(Piece):

    value = 3
    cavalier = "C"
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)


roi = Roi("B", 3, 2)
print(roi)