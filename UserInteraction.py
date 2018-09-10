from boardFunctions import BoardFunctions
from square import Square


class UserInteraction():
    ##variable to check when the game ends
    game_over = False

    def reveal(self, x, y):
        if BoardFunctions.grid[x][y].num_adj_mines != 0:
            BoardFunctions.grid[x][y].is_revealed = True
        else:
            if BoardFunctions.grid[x + 1][y].is_flagged != False and BoardFunctions.grid[x + 1][y].num_adj_mines != 0:
                BoardFunctions.grid[x + 1][y].is_revealed = True
            else:
                self.reveal(x+1, y)
            if BoardFunctions.grid[x - 1][y].is_flagged != False and BoardFunctions.grid[x - 1][y].num_adj_mines != 0:
                BoardFunctions.grid[x - 1][y].is_revealed = True
            else:
                self.reveal(x-1, y)
            if BoardFunctions.grid[x][y + 1].is_flagged != False and BoardFunctions.grid[x][y + 1].num_adj_mines != 0:
                BoardFunctions.grid[x][y + 1].is_revealed = True
            else:
                self.reveal(x, y + 1)
            if BoardFunctions.grid[x][y - 1].is_flagged != False and BoardFunctions.grid[x][y - 1].num_adj_mines != 0:
                BoardFunctions.grid[x][y - 1].is_revealed = True
            else:
                self.reveal(x, y - 1)
            if BoardFunctions.grid[x + 1][y- 1 ].is_flagged != False and BoardFunctions.grid[x + 1][y - 1].num_adj_mines != 0:
                BoardFunctions.grid[x + 1][y - 1].is_revealed = True
            else:
                self.reveal(x+1, y - 1)
            if BoardFunctions.grid[x + 1][y + 1].is_flagged != False and BoardFunctions.grid[x + 1][y + 1].num_adj_mines != 0:
                BoardFunctions.grid[x + 1][y + 1].is_revealed = True
            else:
                self.reveal(x+1, y + 1)
            if BoardFunctions.grid[x - 1][y + 1].is_flagged != False and BoardFunctions.grid[x - 1][y + 1].num_adj_mines != 0:
                BoardFunctions.grid[x - 1][y + 1].is_revealed = True
            else:
                self.reveal(x-1, y + 1)
            if BoardFunctions.grid[x - 1][y - 1].is_flagged != False and BoardFunctions.grid[x - 1][y - 1].num_adj_mines != 0:
                BoardFunctions.grid[x - 1][y - 1].is_revealed = True
            else:
                self.reveal(x - 1, y - 1)

    def check_win(self):
        flag_on_mine = 0
        for i in range(0, BoardFunctions.boardSize):
            for x in range(0, BoardFunctions.boardSize):
                if BoardFunctions.grid[i][x].is_mine == True and BoardFunctions.grid[i][x].is_flagged == True:
                    flag_on_mine += 1
        if flag_on_mine == BoardFunctions.mines_num:
            print("You Win!")
            self.game_over = True
        else:
            return 0

    def play(self,mines,size):

        myBoard = BoardFunctions()

        myBoard.mines_num = mines

        grid = myBoard.make_grid(size)
        myBoard.generate_mines(size,grid)

        while(self.game_over != True):
            numFlags = mines
            myBoard.print_board(size, grid)
            print("Number of flags: %s" % numFlags)
            userX = int(input("Enter an X coordinate: "))
            userY = int(input("Enter a Y coordinate: "))
            userChoice = input("Enter an action flag [f], reveal [r], unflag [n]: ")
            if userX > size or userY > size:
                print("Invalid Try again")
            elif grid[userX][userY].is_flagged == False and userChoice == "n":
                print("Invalid try again")
            elif grid[userX][userY].is_flagged == False and userChoice == "f":
                grid[userX][userY].is_flagged = True
                numFlags -= 1
                check_win()
            elif grid[userX][userY].is_flagged == True and userChoice == "n":
                grid[userX][userY].is_flagged = False
                numFlags += 1
            elif grid[userX][userY].is_mine == True and userChoice == r:
                print("Game Over")
                self.game_over = True
            else:
                reveal(userX, userY)
