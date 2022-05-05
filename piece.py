class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.type}"

    def deplacement(self):
        pass

class Pion(Piece):

    value = 1
    type = "P"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

    def deplacement(self):
        pass


class Roi(Piece):

    value = 0
    type = "R"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

    def deplacement(self):
        pass


class Dame(Piece):
    value = 9
    type = "D"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

    def deplacement(self):
        pass

class Fou(Piece):

    value = 3
    type = "F"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

    def deplacement(self):
        pass

class Tour(Piece):

    value = 5
    type = "T"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

    def deplacement(self):
        pass

class Cavalier(Piece):

    value = 3
    type = "C"

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def __repr__(self):
        super.__repr__(self)

    def deplacement(self):
        pass
