import pygame


class Piece:
    def __init__(self, colour, x, y): #colour is either "B" or "W", case is x,y coordinates
        self.colour = colour
        self.x = x
        self.y = y
        self.type = None
        self.image = None

    def __repr__(self):
        return f"{self.type}"


class Pion(Piece):

    value = 1

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "P"
        if self.colour == "W":
            self.image = pygame.image.load("ImagesPieces/pionBlanc.png")
        else:
            self.image = pygame.image.load("ImagesPieces/pionNoir.png")


    def __repr__(self):
        return super.__repr__(self)


class Roi(Piece):

    value = 0

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "R"
        if self.colour == "W":
            self.image = pygame.image.load("ImagesPieces/roiBlanc.png")
        else:
            self.image = pygame.image.load("ImagesPieces/roiNoir.png")

    def __repr__(self):
        super.__repr__(self)



class Dame(Piece):
    value = 9

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type= "D"
        if self.colour == "W":
            self.image = pygame.image.load("ImagesPieces/reineBlanche.png")
        else:
            self.image = pygame.image.load("ImagesPieces/reineNoire.png")

    def __repr__(self):
        super.__repr__(self)


class Fou(Piece):

    value = 3

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "F"
        if self.colour == "W":
            self.image = pygame.image.load("ImagesPieces/fouBlanc.png")
        else:
            self.image = pygame.image.load("ImagesPieces/fouNoir.png")

    def __repr__(self):
        super.__repr__(self)



class Tour(Piece):

    value = 5

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "T"
        if self.colour == "W":
            self.image = pygame.image.load("ImagesPieces/tourBlanche.png")
        else:
            self.image = pygame.image.load("ImagesPieces/tourNoire.png")

    def __repr__(self):
        super().__repr__(self)



class Cavalier(Piece):

    value = 3

    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.type = "C"
        if self.colour == "W":
            self.image = pygame.image.load("ImagesPieces/cavaBlanc.png")
        else:
            self.image = pygame.image.load("ImagesPieces/CavaNoir.png")

    def __repr__(self):
        super().__repr__(self)

class Vide(Piece):

    value = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "X"
        self.colour = None
        self.image = pygame.image.load("ImagesPieces/PieceVide.png")

    def __repr__(self):
        super().__repr__(self)