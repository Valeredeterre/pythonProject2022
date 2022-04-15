class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y

    def __str__(self):
        return f" Equipe : {self.colour} |  Position : ({self.x}, {self.y}) | Type : {self.type}"

class Pion(Piece):

    value = 1
    type = "P"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)


class Roi(Piece):

    value = 0
    type = "R"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)


class Dame(Piece):
    value = 9
    type = "D"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

class Fou(Piece):

    value = 3
    type = "F"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

class Tour(Piece):

    value = 5
    type = "T"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

class Cavalier(Piece):

    value = 3
    type = "C"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)


roi = Cavalier("B", 3, 2)
print(roi)