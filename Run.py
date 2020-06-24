FIRST_PLAYER = 0
SECOND_PLAYER = 1
EMPTY_CELL = 2


class Map:
    def __init__(self):
        self.m = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]

    def is_empty(self, x: int, y: int) -> bool:
        return self.m[y][x] == EMPTY_CELL

    def place(self, player: int, x: int, y: int) -> bool:
        success = False

        if self.is_empty(x, y) and (player == FIRST_PLAYER or player == SECOND_PLAYER):
            self.m[y][x] = player
            success = True

        return success

    def get(self, x: int, y: int) -> int:
        return self.m[y][x]

    def __str__(self) -> str:
        ans = "  1 2 3\n"

        for index, c in enumerate(self.m):
            ans += str(index + 1) + " "
            for cell in c:
                if cell == FIRST_PLAYER:
                    ans += "x "
                elif cell == SECOND_PLAYER:
                    ans += "o "
                elif cell == EMPTY_CELL:
                    ans += "_ "
            ans += "\n"

        return ans

    def __getitem__(self, item: tuple):
        return self.get(*item)


class Game:
    def __init__(self):
        self.map = Map()

        self.current_player = FIRST_PLAYER
        self.winner = -1

    def is_over(self) -> bool:
        if self.map[0, 0] == self.map[1, 0] == self.map[2, 0] != EMPTY_CELL:
            over = True
            self.winner = self.map[0, 0]
        elif self.map[0, 1] == self.map[1, 1] == self.map[2, 1] != EMPTY_CELL:
            over = True
            self.winner = self.map[0, 1]
        elif self.map[0, 2] == self.map[1, 2] == self.map[2, 2] != EMPTY_CELL:
            over = True
            self.winner = self.map[0, 2]
        elif self.map[0, 0] == self.map[0, 1] == self.map[0, 2] != EMPTY_CELL:
            over = True
            self.winner = self.map[0, 0]
        elif self.map[1, 0] == self.map[1, 1] == self.map[1, 2] != EMPTY_CELL:
            over = True
            self.winner = self.map[1, 0]
        elif self.map[2, 0] == self.map[2, 1] == self.map[2, 2] != EMPTY_CELL:
            over = True
            self.winner = self.map[2, 0]
        elif self.map[0, 0] == self.map[1, 1] == self.map[2, 2] != EMPTY_CELL:
            over = True
            self.winner = self.map[0, 0]
        elif self.map[2, 0] == self.map[1, 1] == self.map[0, 2] != EMPTY_CELL:
            over = True
            self.winner = self.map[2, 0]
        else:
            over = not self.map.is_empty(0, 0) and not self.map.is_empty(0, 1) and not self.map.is_empty(0, 2) \
                   and not self.map.is_empty(1, 0) and not self.map.is_empty(1, 1) and not self.map.is_empty(1, 2)\
                   and not self.map.is_empty(2, 0) and not self.map.is_empty(2, 1) and not self.map.is_empty(2, 2)

        return over

    def change_player(self) -> None:
        self.current_player = (self.current_player + 1) % 2

    def turn(self, x: int, y: int) -> bool:
        return self.map.place(self.current_player, x, y)

    def __str__(self) -> str:
        return str(self.map) + "\n\n" + "player " + str(self.current_player + 1)


if __name__ == "__main__":

    game = Game()

    while not game.is_over():
        successful_turn = False
        while not successful_turn:
            print(game)

            col = 0
            correct_val = False
            while not correct_val:
                correct_val = True
                try:
                    col = int(input("Enter column: "))
                except ValueError:
                    print("Column has to be a number")
                    correct_val = False
                if correct_val and (1 > col or col > 3):
                    print("Column has to be between 1 and 3")
                    correct_val = False

            row = 0
            correct_val = False
            while not correct_val:
                correct_val = True
                try:
                    row = int(input("Enter row: "))
                except ValueError:
                    print("Row has to be a number")
                    correct_val = False
                if correct_val and (1 > row or row > 3):
                    print("Row has to be between 1 and 3")
                    correct_val = False

            print()

            successful_turn = game.turn(col - 1, row - 1)

            if successful_turn:
                game.change_player()
            else:
                print("This cell is occupied")
                print()

    print(game.map)
    if game.winner == -1:
        print("Draw")
    else:
        print("Player " + str(game.winner + 1) + " won!")
