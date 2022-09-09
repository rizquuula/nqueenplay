from random import randint


class Queens:
    def __init__(self, n: int):
        self.chessboard = []
        
        self._queen_symbol = 'Q'
        self._queens_position = []
        
        
        self._create_queens(n)
        self._create_chessboard(n)
        self._place_queens()
    
    def show(self):
        mult = (len(self.chessboard)*4+1)
        for row in self.chessboard:
            print('-'*mult)
            print(f"| {' | '.join(row)} |")
        
        print('-'*mult)
    
    def _create_chessboard(self, n: int):
        chessboard = []
        for x in range(n):
            row = []
            for y in range(n):
                row.append(' ')
            chessboard.append(row)
        
        # assign
        self.chessboard = chessboard
    
    def _create_queens(self, n:int):
        x_y_positions = []
        while len(x_y_positions) < n:
            pos_x = randint(0, n-1)
            pos_y = randint(0, n-1)
            if (pos_x, pos_y) not in x_y_positions:
                x_y_positions.append((pos_x, pos_y))
        
        # assign
        self._queens_position = x_y_positions
    
    def _place_queens(self):
        for coord in self._queens_position:
            self.chessboard[coord[0]][coord[1]] = self._queen_symbol