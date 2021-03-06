from piece import *
import pygame


class Board:

    index_range = [k for k in range(8)]  # used to know if an index is out of range

    def __init__(self):
        self.board = [["" for i in range(8)] for j in range(8)]  # initialisation of a list of string list
        for i in range(8):
            self.board[i][2] = Vide(i, 2)
            self.board[i][3] = Vide(i, 3)
            self.board[i][4] = Vide(i, 4)
            self.board[i][5] = Vide(i, 5)
        for i in range(8):
            self.board[i][1] = Pion("B", i, 1)
            self.board[i][6] = Pion("W", i, 6)
        for i in range(0, 8, 7):  # i = 0 then i = 0 + 7
            if i == 0:
                colour = "B"
                self.board[0][i] = Tour(colour, 0, i)
                self.board[1][i] = Cavalier(colour, 1, i)
                self.board[2][i] = Fou(colour,0,0)
                self.board[3][i] = Dame(colour,2, i)
                self.board[4][i] = Roi(colour, 4, i)
                self.board[5][i] = Fou(colour,0,0)
                self.board[6][i] = Cavalier(colour, 6, i)
                self.board[7][i] = Tour(colour, 7, i)
            else:
                colour = "W"
                self.board[0][i] = Tour(colour, 0, i)
                self.board[1][i] = Cavalier(colour, 1, i)
                self.board[2][i] = Fou(colour,0,0)
                self.board[3][i] = Dame(colour,2, i)
                self.board[4][i] = Roi(colour, 4, i)
                self.board[5][i] = Fou(colour,0,0)
                self.board[6][i] = Cavalier(colour, 6, i)
                self.board[7][i] = Tour(colour, 7, i)

    def __repr__(self):
        """Allow print command to print a representation of the Board class.

        :return: A string representing the board
        :rtype: str
        """
        str = ""
        for k in range(8):
            str += "\n"
            for j in range(8):
                str += self.board[j][k].type
        return str

    def copy_board(self, chess: object):
        """Make a piece move
        This method will copy on board into an other

        :param x: Array positional argument used to locate the piece.
        :rtype : None
        """
        for j in range(8):
            for k in range(8):
                self.board[j][k] = chess.board[j][k]
        return None


    def deplacement(self,x ,y ,new_x ,new_y):
        """Make a piece move
        This method will take two starting and two ending  positional arguments and make the move if it is legitimate for its type.
        The starting position piece type is predetermined and only the appropriate move method will be applied.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        match self.board[x][y].type:
            case 'P':
                move = bool(self.deplacement_pion(x, y, new_x, new_y))
            case 'T':
                move = bool(self.deplacement_tour(x, y, new_x, new_y))
            case 'C':
                move = bool(self.deplacement_cavalier(x, y, new_x, new_y))
            case 'D':
                move = bool(self.deplacement_dame(x, y, new_x, new_y))
            case 'R':
                move = bool(self.deplacement_roi(x, y, new_x, new_y))
            case 'F':
                move = bool(self.deplacement_fou(x, y, new_x, new_y))
            case 'X':
                move = False
        return move

    def isdeplacement(self,x ,y ,new_x ,new_y):
        """Verify if a move is legitimate
        This method will take two starting and two ending  positional arguments and verify if the move is legitimate for its type.
        The starting position piece type is predetermined and only the appropriate move verification method will be applied.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
        :rtype: bool
        """
        is_move = bool()
        match self.board[x][y].type:
            case 'P':
                is_move = bool(self.isdeplacement_pion(x, y, new_x, new_y))
            case 'T':
                is_move = bool(self.isdeplacement_tour(x, y, new_x, new_y))
            case 'C':
                is_move = bool(self.isdeplacement_cavalier(x, y, new_x, new_y))
            case 'D':
                is_move = bool(self.isdeplacement_dame(x, y, new_x, new_y))
            case 'R':
                is_move = bool(self.isdeplacement_roi(x, y, new_x, new_y))
            case 'F':
                is_move = bool(self.isdeplacement_fou(x, y, new_x, new_y))
        return is_move

    def isinrange(self, x, y, new_x, new_y):
        """Verify if the selected position is on the bord
            This method will take two starting and two ending  positional arguments and verify if the move finish on the board.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is on the board, a boolean value of 0 otherwise.
            :rtype: bool
        """
        for k in [x, y, new_x, new_y]:  # k take each value of the list from first to last
            if k not in self.index_range:  # only raise an error when k is not in the interval [0,7]
                raise IndexError
                return False
        return True

    def isdeplacement_fou(self, x, y, new_x, new_y):
        """Verify if a move is legitimate for a Bishop
            This method will take two starting and two ending  positional arguments and verify if the move is a legitimate bishop move.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
            :rtype: bool
        """

        blocking = 0 #blocking is equal to 1 if a piece block the way to new_x,new_y
        self.isinrange(x, y, new_x, new_y)
        if (new_x - x) == (new_y - y) and (new_y - y) >= 0:
            for i in range(1, abs(new_y - y)):
                if self.board[x + i][y + i].type != "X":
                    blocking = 1

        elif (new_x - x) == (new_y - y) and (new_y - y) <= 0:
            for i in range(1, abs(new_y - y)):
                if self.board[x - i][y - i].type != "X":
                    blocking = 1

        elif (new_x - x) == -(new_y - y) and (new_y - y) >= 0:
            for i in range(1, abs(new_y - y)):
                if self.board[x - i][y + i].type != "X":
                    blocking = 1

        elif (new_x - x) == -(new_y - y) and (new_y - y) <= 0:
            for i in range(1, abs(new_y - y)):
                if self.board[x + i][y - i].type != "X":
                    blocking = 1

        if ((new_y - y == new_x - x) or (-(new_y - y) == new_x - x)) and blocking == 0 and self.board[x][y].type == "F":
            return 1
        elif ((new_y - y == new_x - x) or (-(new_y - y) == new_x - x)) and blocking == 0 and self.board[x][y].type == "D":
            return 2
        else:
            return 0



    def isdeplacement_roi(self, x, y, new_x, new_y):
        """Verify if a move is legitimate for a king
            This method will take two starting and two ending  positional arguments and verify if the move is legitimate.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
            :rtype: bool
        """
        self.isinrange(x, y, new_x, new_y)
        if (abs(new_x - x) <= 1 and abs(new_y - y) <= 1) and self.board[x][y].type == 'R':
            return 1
        else : return 0

    def isdeplacement_cavalier(self, x, y, new_x, new_y):
        """Verify if a move is legitimate for a bishop
            This method will take two starting and two ending  positional arguments and verify if the move is legitimate.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
            :rtype: bool
        """
        self.isinrange(x, y, new_x, new_y)  # c.f the method in question
        if ((new_x == x + 1 and new_y == y + 2) or (new_x == x - 1 and new_y == y + 2) or (
                new_x == x + 1 and new_y == y - 2) or (new_x == x - 1 and new_y == y - 2) or (
                    new_x == x + 2 and new_y == y - 1) or (new_x == x + 2 and new_y == y + 1) or (
                    new_x == x - 2 and new_y == y - 1) or (new_x == x - 2 and new_y == y + 1)) and (
                (abs(x - new_x) == 2 and abs(y - new_y) == 1) or (abs(x - new_x) == 1 and abs(y - new_y) == 2)) \
                and (x != new_x and y != new_y) and self.board[x][y].type == 'C':
            return 1
        else:
            return 0

    def isdeplacement_pion(self, x, y, new_x, new_y):
        """Verify if a move is legitimate for a pawn
            This method will take two starting and two ending  positional arguments and verify if the move is legitimate.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
            :rtype: bool
        """
        if self.board[x][y].type == 'P':
            if self.board[x][y].colour == 'W':
                if (x == new_x and y-1 == new_y and self.board[new_x][new_y].type == 'X')or(x == new_x and y == 6 and new_y == 4 and self.board[new_x][new_y].type == 'X')or(self.board[new_x][new_y].colour == 'B' and (x == new_x-1 or x == new_x+1) and y-1 == new_y):
                    return 1
            elif self.board[x][y].colour == 'B':
                if (x == new_x and y+1 == new_y and self.board[new_x][new_y].type == 'X')or(x == new_x and y == 1 and new_y == 3 and self.board[new_x][new_y].type == 'X')or(self.board[new_x][new_y].colour == 'W'and (x == new_x-1 or x == new_x+1) and y+1 == new_y):
                    return 1
            else: return 0

        else:
            return 0

    def isdeplacement_dame(self,x,y,new_x,new_y):
        """Verify if a move is legitimate for a Queen
            This method checks if the move is either a Bishop or a tower one.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
            :rtype: bool
        """
        self.isinrange(x,y,new_x,new_y)
        if self.isdeplacement_fou(x,y,new_x,new_y) == 2 or self.isdeplacement_tour(x,y,new_x,new_y) == 2:
            return 1

    def isdeplacement_tour(self, x,y,new_x,new_y):
        """Verify if a move is legitimate for a tower
            This method will take two starting and two ending  positional arguments
             and verify if the move is legitimate for a tower.

            :param x: Array positional argument used to locate the piece.
            :param y: Array positional argument used to locate the piece.
            :param new_x: Array positional argument used to locate the piece ending position.
            :param new_y: Array positional argument used to locate the piece ending position.
            :return: A boolean value of 1 when a movement is legitimate, a boolean value of 0 otherwise.
            :rtype: bool
        """
        self.isinrange(x, y, new_x, new_y)

        blocking = 0 #blocking is equal to 1 if a piece block the way to new_x,new_y

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
            return 1
        elif ((new_x == x and new_y > y) or (new_x == x and new_y < y) or (new_y == y and new_x > x) or (
                new_y == y and new_x < x)) and blocking == 0 and (
                new_x >= 0 and new_y >= 0 and new_x < 8 and new_y < 8) and self.board[x][y].type == 'D':
            return 2
        else : return 0

    def deplacement_cavalier(self, x, y, new_x, new_y):
        """Make a piece move
        This method will take two starting and two ending  positional arguments
         and make the move if it is legitimate for a knight.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        try:
            if self.isdeplacement_cavalier(x, y, new_x, new_y) == 1:  # used to know if the move is legitimate
                if self.board[new_x][new_y].colour != self.board[x][y].colour:  # in this case our piece would "eat" the enemy piece
                    # if self.board[new_x][new_y].type != 'X': # Void case has no color, so we make sure to don't let the player know if he ate nothing
                    # print(f"{self.board[new_x][new_y].type} a ??t?? mang??(e)") # let the player know what he has just eaten
                    self.board[new_x][new_y] = Cavalier(self.board[x][y].colour, new_x, new_y)  # place the appropriate piece on the destination positional values
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
        """Make a piece move
        This method will take two starting and two ending  positional arguments
         and make the move if it is legitimate for a king.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        if self.isdeplacement_roi(x, y, new_x, new_y):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a ??t?? mang??(e)")
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
        """Make a piece move
        This method will take two starting and two ending  positional arguments
        and make the move if it is legitimate for a pawn.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        if self.isdeplacement_pion(x, y, new_x, new_y):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a ??t?? mang??(e)")
                self.board[new_x][new_y] = Pion(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                if self.board[new_x][new_y].colour == "W" and new_y == 0:
                    self.board[new_x][new_y] = Dame("W",0,0)

                if self.board[new_x][new_y].colour == "B" and new_y == 7:
                    self.board[new_x][new_y] = Dame("B", 0, 0)

                return 1
            else:
                # print('La case est prise')
                return 0
        else:
            # print('La case est prise')
            return 0

    def deplacement_tour(self, x, y, new_x, new_y):
        """Make a piece move
        This method will take two starting and two ending  positional arguments and make the move if it is legitimate for a tower.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        if self.isdeplacement_tour(x, y, new_x, new_y):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a ??t?? mang??(e)")
                self.board[new_x][new_y] = Tour(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                return 1
            else:
                return 0
        else:
            return 0

    def deplacement_dame(self, x, y, new_x, new_y):
        """Make a piece move
        This method will take two starting and two ending  positional arguments and make the move if it is legitimate for a queen.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        if self.isdeplacement_dame(x, y, new_x, new_y):
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a ??t?? mang??(e)")
                self.board[new_x][new_y] = Dame(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                return 1
            else:
                # print('La case est prise')
                return 0
        else:
            # print("Deplacement non valide")
            return 0


    def deplacement_fou(self,x , y, new_x, new_y):
        """Make a piece move
        This method will take two starting and two ending  positional arguments and make the move if it is legitimate for a bishop.

        :param x: Array positional argument used to locate the piece.
        :param y: Array positional argument used to locate the piece.
        :param new_x: Array positional argument used to locate the piece ending position.
        :param new_y: Array positional argument used to locate the piece ending position.
        :return: A boolean value of 1 when a movement is done, a boolean value of 0 otherwise.
        :rtype: bool
        """
        if self.isdeplacement_fou(x, y, new_x, new_y) == 1:
            if self.board[new_x][new_y].colour != self.board[x][y].colour:
                if self.board[new_x][new_y].type != 'X':
                    print(f"{self.board[new_x][new_y].type} a ??t?? mang??(e)")
                self.board[new_x][new_y] = Fou(self.board[x][y].colour, new_x, new_y)
                self.board[x][y] = Vide(x, y)
                return 1
            else:
                # print('La case est prise')
                return 0
        else:
            # print("Deplacement non valide")
            return 0


    def board_display(self,screen,colour):
        """Display the board using the pygame library
        This method will read through the whole chessboard line by line displaying the right image on the right position

        :param colour: String value used to display an overlay showing whose turn it is
        :param screen: Pygame display on witch we want to display the board
        :rtype: None
        """
        screen.blit(pygame.image.load("ImagesPieces/chess.jpg"), (0, 0))
        for i in range(8):
            for j in range(8):
                if self.board[i][j].colour == colour:
                    screen.blit(pygame.image.load("ImagesPieces/colour.png"), (50 * i, 50 * j))
                screen.blit(self.board[i][j].image, (50 * i, 50 * j))
        pygame.display.update()


    def get_king_positional_arguments(self, colour: str):
        """Get either a B or W king positional arguments
        This method will read through the whole chessboard line by line until the element met is a King of the
        requested colour.

        :param colour: String value used to check if the piece colour attribute matches it.
        :return: A tuple containing both positional arguments of the requested king.
        :rtype: tuple
        """
        king_x = int()
        king_y = int()
        for j in range(8):
            for k in range(8):
                if self.board[k][j].type == 'R' and self.board[k][j].colour == colour:
                    king_x = k
                    king_y = j
        return king_x, king_y

    def ischeck(self, colour: str):
        """Return either True or False depending on the check status
        This method will try to move all the piece on the king position to see if the kink is check

        :param colour: String to choose the color who need to be check if it's check
        :return: True when the team of the argument color is in check, false otherwise
        :rtype: bool
        """
        check = False
        enemy_colour = str()
        king_x, king_y = self.get_king_positional_arguments(colour)
        if self.board[king_x][king_y].colour == 'W':
            enemy_colour = 'B'
        if self.board[king_x][king_y].colour == 'B':
            enemy_colour = 'W'
        for x in range(8):
            for y in range(8):
                if self.board[x][y].colour == enemy_colour:
                    try:
                        check = self.isdeplacement(x, y, king_x, king_y)
                        self.board[king_x][king_y] = Roi(colour, king_x, king_y)

                    except Exception as e:
                        print(e)
                if check:
                    return check
        return check

    def ischeck_mate(self, colour, start_turn_board: object):
        """Return either True or False depending on the checkmate status
            This method will try to move all the piece and test is the king is still check

            :param colour: String to choose the color who need to be check if it's checkmate
            :return: True of False depending on the state of the board
            :rtype: bool
        """
        checkMate = True
        start_turn_board.copy_board(self)
        for x in range(8):
            for y in range(8):
                if checkMate is True and self.board[x][y].colour == colour:
                    for new_x in range(8):
                        for new_y in range(8):
                            self.deplacement(x, y, new_x, new_y)

                            if self.ischeck(colour) is not True:
                                checkMate = False

                            self.copy_board(start_turn_board)
        return checkMate






