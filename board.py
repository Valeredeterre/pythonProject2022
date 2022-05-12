from piece import Piece
from piece import Pion
from piece import Roi
from piece import Dame
from piece import Fou
from piece import Tour
from piece import Cavalier
from piece import Vide


class Board:
    board = [["X" for i in range(8)] for j in range(8)]
    for i in range(8):
        board[i][2] = Vide(i, 2)
        board[i][3] = Vide(i, 3)
        board[i][4] = Vide(i, 4)
        board[i][5] = Vide(i, 5)

    for i in range(8):
        board[i][1] = Pion("B", i, 1)
        board[i][6] = Pion("W", i, 6)
    for i in range(0, 8, 7):  # i = 0 then i = 0 + 7
        if (i == 0):
            colour = "B"
            board[0][i] = Tour(colour, 0, i)
            board[1][i] = Cavalier(colour, 1, i)
            board[2][i] = Fou(colour, 2, i)
            board[3][i] = Roi(colour, 3, i)
            board[4][i] = Dame(colour, 4, i)
            board[5][i] = Fou(colour, 5, i)
            board[6][i] = Cavalier(colour, 6, i)
            board[7][i] = Tour(colour, 7, i)
        else:
            colour = "W"
            board[0][i] = Tour(colour, 0, i)
            board[1][i] = Cavalier(colour, 1, i)
            board[2][i] = Fou(colour, 2, i)
            board[3][i] = Roi(colour, 3, i)
            board[4][i] = Dame(colour, 4, i)
            board[5][i] = Fou(colour, 5, i)
            board[6][i] = Cavalier(colour, 6, i)
            board[7][i] = Tour(colour, 7, i)

    # def __init__(self):
    # self.board = self.initialize()
    board = [["X" for i in range(8)] for j in range(8)]
    for i in range(8):
        board[i][2] = Vide(i, 2)
        board[i][3] = Vide(i, 3)
        board[i][4] = Vide(i, 4)
        board[i][5] = Vide(i, 5)

    for i in range(8):
        board[i][1] = Pion("B", i, 1)
        board[i][6] = Pion("W", i, 6)
    for i in range(0, 8, 7):  # i = 0 then i = 0 + 7
        if (i == 0):
            colour = "B"
            board[0][i] = Tour(colour, 0, i)
            board[1][i] = Cavalier(colour, 1, i)
            board[2][i] = Fou(colour, 2, i)
            board[3][i] = Roi(colour, 3, i)
            board[4][i] = Dame(colour, 4, i)
            board[5][i] = Fou(colour, 5, i)
            board[6][i] = Cavalier(colour, 6, i)
            board[7][i] = Tour(colour, 7, i)
        else:
            colour = "W"
            board[0][i] = Tour(colour, 0, i)
            board[1][i] = Cavalier(colour, 1, i)
            board[2][i] = Fou(colour, 2, i)
            board[3][i] = Roi(colour, 3, i)
            board[4][i] = Dame(colour, 4, i)
            board[5][i] = Fou(colour, 5, i)
            board[6][i] = Cavalier(colour, 6, i)
            board[7][i] = Tour(colour, 7, i)

    def __repr__(self):
        str = ""
        for k in range(8):
            str += "\n"
            for j in range(8):
                str += self.board[j][k].type
        return str

    def deplacement_cavalier(self, x, y, new_x, new_y):
        check = (new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8)
        if ((new_x == x + 1 and new_y == y + 2) or (new_x == x - 1 and new_y == y + 2) or (
                new_x != x + 1 and new_y == y - 2) or (new_x != x - 1 and new_y == y - 2) or (
                new_x != x + 2 and new_y == y - 1) or (new_x != x + 2 and new_y == y + 1) or (
                new_x != x - 2 and new_y == y - 1) or (new_x != x - 2 and new_y == y + 1)) and check:
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Cavalier(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
            else:
                return print('La case est prise')
        else:
            return print("Deplacement non valide")

    def deplacement_roi(self, x, y, new_x, new_y):
        check = (new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8)
        if (abs(new_x - x) < 1 and abs(new_y - y) < 1) and check:
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Roi(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
            else:
                return print('La case est prise')
        else:
            return print("Deplacement non valide")

    def deplacement_pion(self, x, y, new_x, new_y):
        check = (new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8)
        if self.board[x][y].colour == "B":
            if (((new_x == x - 1  or (x==7 and new_x == 5)and new_y == y) or (self.board[new_x][new_y].colour == "W") and new_x == x - 1 and new_y == y + 1) or ((self.board[new_x][new_y].colour == "W") and new_x == x - 1 and new_y == y - 1)) and check:
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                else:
                    return print('La case est prise')
            else:
                return print("Deplacement non valide")
        if self.board[x][y].colour == "W":
            if ((((new_x  == x+1 or (x==1 and new_x == 3)) and new_y == y) or ((self.board[new_x][new_y].colour == "W") and new_x == x+1 and new_y == y+1)) or ((self.board[new_x][new_y].colour == "W") and new_x == x+1 and new_y == y-1))  and check:
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                else:
                    return print('La case est prise')
            else:
                return print("Deplacement non valide")

    def deplacement_tour(self, x, y, new_x, new_y):
        blocking = 0
        check = new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8

        if new_x == x and new_y > y:
            for i in range(1,abs(new_y - y)-1):
                if self.board[x][y + i].type != "X":
                    blocking = 1

        if new_x == x and new_y < y:
            for i in range(1,abs(new_y - y)-1):
                if self.board[x][y - i].type != "X":
                    blocking = 1

        if new_y == y and new_x > x:
            for i in range(1,abs(new_x - x)-1):
                if self.board[x + i][y].type != "X":
                    blocking = 1
    def deplacement_cavalier(self, x, y, new_x, new_y):
        if (new_x == x + 1 and new_y == y + 2) or (new_x == x - 1 and new_y == y + 2) or (
                new_x != x + 1 and new_y == y - 2) or (new_x != x - 1 and new_y == y - 2) or (
                new_x != x + 2 and new_y == y - 1) or (new_x != x + 2 and new_y == y + 1) or (
                new_x != x - 2 and new_y == y - 1) or (new_x != x - 2 and new_y == y + 1):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Cavalier(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
            else:
                return print('La case est prise')
        else:
            return print("Deplacement non valide")

    def deplacement_roi(self, x, y, new_x, new_y):
        if (abs(new_x - x) < 1 and abs(new_y - y) < 1) and (new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Roi(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
            else:
                return print('La case est prise')
        else:
            return print("Deplacement non valide")

    def deplacement_pion(self, x, y, new_x, new_y):
        if self.board[x][y].colour == "B":
            if (((new_x == x - 1 or (x == 7 and new_x == 5) and new_y == y) or (
                    self.board[new_x][new_y].colour == "W") and new_x == x - 1 and new_y == y + 1) or (
                        (self.board[new_x][new_y].colour == "W") and new_x == x - 1 and new_y == y - 1)) and (
                    new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8):
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                else:
                    return print('La case est prise')
            else:
                return print("Deplacement non valide")
        if self.board[x][y].colour == "W":
            if ((((new_x == x + 1 or (x == 1 and new_x == 3)) and new_y == y) or (
                    (self.board[new_x][new_y].colour == "W") and new_x == x + 1 and new_y == y + 1)) or (
                        (self.board[new_x][new_y].colour == "W") and new_x == x + 1 and new_y == y - 1)) and (
                    new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8):
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                else:
                    return print('La case est prise')
            else:
                return print("Deplacement non valide")

    def deplacement_tour(self, x, y, new_x, new_y):
        blocking = 0

        if new_x == x and new_y > y:
            for i in range(1, abs(new_y - y)):
                if self.board[x][y + i].type != "X":
                    blocking = 1

        if new_x == x and new_y < y:
            for i in range(1, abs(new_y - y)):
                if self.board[x][y - i].type != "X":
                    blocking = 1

        if new_y == y and new_x > x:
            for i in range(1, abs(new_x - x)):
                if self.board[x + i][y].type != "X":
                    blocking = 1

        if new_y == y and new_x < x:
            for i in range(1, abs(new_x - x)):
                if self.board[x - i][y].type != "X":
                    blocking = 1

        if ((new_x == x and new_y > y) or (new_x == x and new_y < y) or (new_y == y and new_x > x) or (
                new_y == y and new_x < x)) and blocking == 0 and (
                new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Tour(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
            else:
                return print('La case est prise')
        else:
            return print("Deplacement non valide")

    def deplacement_fou(self, x, y, new_x, new_y):
        old_x = x
        old_y = y
        a = abs(new_x - x) == abs(new_y - y)
        print(a)
        if 0 <= new_x < 8 and 0 <= new_y < 8 and (new_y - (new_y - y) == y) and abs(new_x - x) == abs(new_y - y) and (new_x - (new_x - x) == x) and \
                self.board[x][y].type == "F":
            while x != new_x and y != new_y:
                if new_x > old_x and new_y > old_y:
                    x = x + 1
                    y = y + 1
                    k1 = -1
                    k2 = -1
                elif new_x < old_x and new_y > old_y:
                    x = x - 1
                    y = y + 1
                    k1 = 1
                    k2 = -1
                elif new_x > old_x and new_y < old_y:
                    x = x + 1
                    y = y - 1
                    k1 = -1
                    k2 = 1
                elif new_x < old_x and new_y < old_y:
                    x = x - 1
                    y = y - 1
                    k1 = 1
                    k2 = 1
                if self.board[x][y].type != 'X' and self.board[x][y].colour != \
                        self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                            y + k2 * (int((new_y - old_y) / (new_y - old_y)))].colour:
                    print(f"{self.board[x][y].type} a été mangé(e)")
                    self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                        y + k2 * (int((new_y - old_y) / (new_y - old_y)))] = Vide(x - 1, y - 1)
                    self.board[x][y] = Fou(self.board[old_x][old_y].colour, new_x, new_y)
                    return 1
                elif self.board[x][y].type != 'X' and self.board[x][y].colour == \
                        self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                            y + k2 * (int((new_y - old_y) / (new_y - old_y)))].colour:
                    return print('Cette case est déjà prise')
                else:
                    self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                        y + k2 * (int((new_y - old_y) / (new_y - old_y)))] = Vide(x, y)
                    self.board[x][y] = Fou(self.board[old_x][old_y].colour, new_x, new_y)
        elif (new_y - (new_y - y) != y) or (new_x - (new_x - x) != x) or abs(new_x - x) != abs(new_y - y):
            return print('Deplacement invalide')
        elif self.board[x][y].type != "F":
            return print('Ce deplacement est unique au Fou')
        elif new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
            return print('La case destination est inappropriee')

        if new_y == y and new_x < x:
            for i in range(1,abs(new_x - x)-1):
                if self.board[x - i][y].type != "X":
                    blocking = 1

        if ((new_x == x and new_y != y) or (new_y == y and new_x != x))  and blocking == 0 and check:
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Tour(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                else:
                    return print('La case est prise')
        else:
            return print("Deplacement non valide")

    def deplacement_Dame(self, x, y, new_x, new_y):
        blocking = 0
        check = new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8

        if new_x == x and new_y > y:
            for i in range(1,abs(new_y - y)):
                if self.board[x][y + i].type != "X":
                    blocking = 1

        if new_x == x and new_y < y:
            for i in range(1,abs(new_y - y)):
                if self.board[x][y - i].type != "X":
                    blocking = 1

        if new_y == y and new_x > x:
            for i in range(1,abs(new_x - x)):
                if self.board[x + i][y].type != "X":
                    blocking = 1

        if new_y == y and new_x < x:
            for i in range(1,abs(new_x - x)):
                if self.board[x - i][y].type != "X":
                    blocking = 1

        if (new_x - x) == (new_y - y) and (new_y - y) >= 0:
            for i in range(1,abs(new_y - y)):
                if self.board[x + i ][y + i].type != "X":
                    blocking = 1

        if (new_x - x) == (new_y - y) and (new_y - y) <= 0:
            for i in range(1,abs(new_y - y)):
                if self.board[x - i][y - i].type != "X":
                    blocking = 1

        if (new_x - x) == -(new_y - y) and (new_y - y) >= 0:
            for i in range(1,abs(new_y - y)):
                if self.board[x+i][y-i].type != "X":
                    blocking = 1

        if (new_x - x) == -(new_y - y) and (new_y - y) <= 0:
            for i in range(1,abs(new_y - y)):
                if self.board[x-i][y+i].type != "X":
                    blocking = 1

        if (((new_x == x and new_y != y) or (new_y == y and new_x != x)) or (new_y - (new_y - y) == y) and (new_x - (new_x - x) == x)) and blocking == 0 and check:
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Dame(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                else:
                    return print('La case est prise')
        else:
            return print("Deplacement non valide")


