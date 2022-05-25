from piece import Pion
from piece import Roi
from piece import Dame
from piece import Fou
from piece import Tour
from piece import Cavalier
from piece import Vide


class Board:
    board = [["" for i in range(8)] for j in range(8)]  # initialisation of a list of string list
    index_range = [k for k in range(8)]     # used to know if an index is out of range
    for i in range(8):
        board[i][2] = Vide(i, 2)
        board[i][3] = Vide(i, 3)
        board[i][4] = Vide(i, 4)
        board[i][5] = Vide(i, 5)
    for i in range(8):
        board[i][1] = Pion("B", i, 1)
        board[i][6] = Pion("W", i, 6)
    for i in range(0, 8, 7):  # i = 0 then i = 0 + 7
        if i == 0:
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

    def isinrange(self, x, y, new_x, new_y):  # return value is boolean, raise an index error if one of the
        # positional values is out of range
        for k in [x, y, new_x, new_y]:  # k take each value of the list from first to last
            if k not in self.index_range:  # only raise an error when k is not in the interval [0,7]
                raise IndexError
                return 0
        return 1

    def isdeplacement_cavalier(self, x, y, new_x,
                               new_y):  # return value is boolean, verify if the positional values match a knight move
        self.isinrange(x, y, new_x, new_y)  # c.f the method in question
        if (new_x == x + 1 and new_y == y + 2) or (new_x == x - 1 and new_y == y + 2) or (
                new_x == x + 1 and new_y == y - 2) or (new_x == x - 1 and new_y == y - 2) or (
                new_x == x + 2 and new_y == y - 1) or (new_x == x + 2 and new_y == y + 1) or (
                new_x == x - 2 and new_y == y - 1) or (new_x == x - 2 and new_y == y + 1) and (
                (abs(x - new_x) == 2 and abs(y - new_y) == 1) or (abs(x - new_x) == 1 and abs(y - new_y) == 2))\
                and (x != new_x and y != new_y):
            return 1
        else:
            return 0

    def isdeplacement_fou(self, x, y, new_x, new_y):  # return value is boolean, verify if the positional values
        # match a bishop move
        self.isinrange(x, y, new_x, new_y)
        if (new_y - (new_y - y) == y) and abs(new_x - x) == abs(new_y - y) and (
                new_x - (new_x - x) == x) and self.board[x][y].type == "F" and (x != new_x and y != new_y):
            # conditions that are unique to the bishop
            return 1
        else:
            return 0

    def deplacement_cavalier(self, x, y, new_x, new_y):  # move the piece to the appropriate positional values
        try:
            if self.isdeplacement_cavalier(x, y, new_x, new_y) == 1:  # used to know if the move is legitimate
                if self.board[new_x][new_y].colour != self.board[x][
                    y].colour:  # in this case our piece would "eat" the enemy piece
                    # if self.board[new_x][new_y].type != 'X': # Void case has no color, so we make sure to don't let the player know if he ate nothing
                    # print(f"{self.board[new_x][new_y].type} a été mangé(e)") # let the player know what he has just eaten
                    self.board[new_x][new_y] = Cavalier(self.board[x][y].colour, new_x,
                                                        new_y)  # place the appropriate piece on the destination positional values
                    self.board[x][y] = Vide(x, y)  # empty the previous piece location
                    return 1  # return 1 when a move has been played
                else:
                    # print('La case est prise')
                    return 0  # return 0 and print the reason the move didn't happen
            else:
                # print("Deplacement non valide")
                return 0  # return 0 and print the reason the move didn't happen
        except Exception as e:
            # print(e)
            return 0  # return 0 and print the raised errors

    def deplacement_roi(self, x, y, new_x, new_y):
        check = (new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8)
        if (abs(new_x - x) <= 1 and abs(new_y - y) <= 1) and self.board[x][y].type == 'R' and check:
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Roi(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                return 1
            else:
                # print('La case est prise')
                return 0
        else:
            # print("Deplacement non valide")
            return 0

    def deplacement_pion(self, x, y, new_x, new_y):
        check = (8 > new_x >= 0 and 0 <= new_y < 8)
        if self.board[x][y].colour == "W":
            if ((new_x == x and new_y == y - 1 and self.board[new_x][new_y].type == 'X') or (
                    new_x == x and new_y == 4 and y == 6 and self.board[new_x][new_y].type == 'X') or (
                        self.board[new_x][new_y].colour == "B" and (
                        new_x == x + 1 or new_x == x - 1) and new_y == y - 1)) and self.board[x][
                y].type == 'P' and check:
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                    return 1
                else:
                    # print('La case est prise')
                    return 0
            else:
                # print('La case est prise')
                return 0

        if self.board[x][y].colour == "B":
            if ((new_x == x and new_y == y + 1 and self.board[new_x][new_y].type == 'X') or (
                    new_x == x and new_y == 3 and y == 1 and self.board[new_x][new_y].type == 'X') or (
                        self.board[new_x][new_y].colour == "W" and (
                        new_x == x + 1 or new_x == x - 1) and new_y == y + 1)) and self.board[x][
                y].type == 'P' and check:
                if self.board[new_x][new_y].colour != self.board[x][y].colour:
                    if self.board[new_x][new_y].type != 'X':
                        print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                    self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                    self.board[x][y] = Vide(x, y)
                    return 1
                else:
                    # print('La case est prise')
                    return 0
            else:
                # print('La case est prise')
                return 0

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
                new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8) and self.board[x][y].type == 'T':
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Tour(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                return 1
            else:
                # print('La case est prise')
                return 0
        else:
            # print("Deplacement non valide")
            return 0

    def deplacement_fou(self, x, y, new_x, new_y):
        old_x = x  # store initial x value
        old_y = y  # store initial y value
        old_colour = self.board[x][y].colour
        if self.isdeplacement_fou(self, x, y, new_x, new_y) == 1:
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
                if self.board[x][y].type != 'X' and self.board[x][y].colour != old_colour:
                    # print(f"{self.board[x][y].type} a été mangé(e)")
                    self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                        y + k2 * (int((new_y - old_y) / (new_y - old_y)))] = Vide(x - 1, y - 1)
                    self.board[x][y] = Fou(old_colour, new_x, new_y)
                    if x == new_x or y == new_y:
                        return 1
                elif self.board[x][y].type != 'X' and self.board[x][y].colour == old_colour:
                    self.board[old_x][old_y] = Fou(old_colour, old_x, old_y)
                    self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                        y + k2 * (int((new_y - old_y) / (new_y - old_y)))] = Vide(x - 1, y - 1)
                    # print('Cette case est déjà prise')
                    return 0
                else:
                    self.board[x + k1 * (int((new_x - old_x) / (new_x - old_x)))][
                        y + k2 * (int((new_y - old_y) / (new_y - old_y)))] = Vide(x, y)
                    self.board[x][y] = Fou(old_colour, new_x, new_y)

    def deplacement_dame(self, x, y, new_x, new_y):
        blocking = 0
        try:
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

            if (new_x - x) == (new_y - y) and (new_y - y) >= 0:
                for i in range(1, abs(new_y - y)):
                    if self.board[x + i][y + i].type != "X":
                        blocking = 1

            if (new_x - x) == (new_y - y) and (new_y - y) <= 0:
                for i in range(1, abs(new_y - y)):
                    if self.board[x - i][y - i].type != "X":
                        blocking = 1

            if (new_x - x) == -(new_y - y) and (new_y - y) >= 0:
                for i in range(1, abs(new_y - y)):
                    if self.board[x + i][y - i].type != "X":
                        blocking = 1

            if (new_x - x) == -(new_y - y) and (new_y - y) <= 0:
                for i in range(1, abs(new_y - y)):
                    if self.board[x - i][y + i].type != "X":
                        blocking = 1
        except Exception as e:
            # print(e)
            return 0

        if (((new_x == x and new_y != y) or (new_y == y and new_x != x)) or (new_y - (new_y - y) == y) and (
                new_x - (new_x - x) == x)) and blocking == 0 and self.board[x][y].type == 'D':
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a été mangé(e)")
                self.board[new_x][new_y] = Dame(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                return 1
            else:
                # print('La case est prise')
                return 0
        else:
            # print("Deplacement non valide")
            return 0

    def ischeck(self, colour):
        check = 0
        for j in range(8):
            for k in range(8):
                if self.board[k][j].type == 'R' and self.board[k][j].colour == colour:
                    king_x = k
                    king_y = j

        if self.board[king_x][king_y].colour == 'W':
            enemy_colour = 'B'
        if self.board[king_x][king_y].colour == 'B':
            enemy_colour = 'W'
        print(king_x, king_y)
        for x in range(8):
            for y in range(8):
                if self.board[x][y].colour == enemy_colour:
                    check += self.deplacement_pion(x, y, king_x, king_y)
                    check += self.deplacement_tour(x, y, king_x, king_y)
                    check += self.deplacement_cavalier(x, y, king_x, king_y)
                    check += self.deplacement_dame(x, y, king_x, king_y)
                    check += self.deplacement_roi(x, y, king_x, king_y)
                    check += self.deplacement_fou(x, y, king_x, king_y)
                    match self.board[king_x][king_y].type:
                        case 'P':
                            self.board[x][y] = Pion(enemy_colour, x, y)
                            print("P")
                        case 'T':
                            self.board[x][y] = Tour(enemy_colour, x, y)
                            print('T')
                        case 'C':
                            self.board[x][y] = Cavalier(enemy_colour, x, y)
                        case 'D':
                            self.board[x][y] = Dame(enemy_colour, x, y)
                            print("D")
                        case 'R':
                            if self.board[king_x][king_y].colour == enemy_colour:
                                self.board[x][y] = Roi(enemy_colour, x, y)
                        case 'F':
                            self.board[x][y] = Fou(enemy_colour, x, y)
                    self.board[king_x][king_y] = Roi(colour, king_x, king_y)
                if check == 1:
                    return print(check)
        return print(check)

