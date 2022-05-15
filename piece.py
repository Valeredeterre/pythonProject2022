class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y
        self.type = None
        self.png = None

    def __repr__(self):
        return f"{self.type}"


class Pion(Piece):

    value = 1

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "P"
        self.png = None

    def __repr__(self):
        return super.__repr__(self)


class Roi(Piece):

    value = 0

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "R"
        self.png = None

    def __repr__(self):
        super.__repr__(self)



class Dame(Piece):
    value = 9

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type= "D"
        self.png = None

    def __repr__(self):
        super.__repr__(self)


class Fou(Piece):

    value = 3

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "F"
        self.png = None

    def __repr__(self):
        super.__repr__(self)



class Tour(Piece):

    value = 5

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "T"
        self.png = None

    def __repr__(self):
        super().__repr__(self)



class Cavalier(Piece):

    value = 3

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "C"
        self.png = None

    def __repr__(self):
        super().__repr__(self)

class Vide(Piece):

    value = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "X"
        self.colour = "V"
        self.png = None

    def __repr__(self):
        super().__repr__(self)