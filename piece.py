class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y
        self.type = None

    def __repr__(self):
        if self.colour == "w":
            return f"{self.type}"
        else:
            return f" {str.lower(self.type)}"




class Pion(Piece):

    value = 1

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "P"

    def __repr__(self):
            return super.__repr__(self)







class Roi(Piece):

    value = 0

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "R"

    def __repr__(self):
        super.__repr__(self)




class Dame(Piece):
    value = 9

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type= "D"

    def __repr__(self):
        super.__repr__(self)



class Fou(Piece):

    value = 3

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "F"

    def __repr__(self):
        super.__repr__(self)



class Tour(Piece):

    value = 5

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "T"

    def __repr__(self):
        super().__repr__(self)

    def get_piece_colour(self):
        return f"{self.colour}"


class Cavalier(Piece):

    value = 3

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "C"

    def __repr__(self):
        super().__repr__(self)


class Vide(Piece):

    value = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "X"
        self.colour = None

    def __repr__(self):
        super().__repr__(self)