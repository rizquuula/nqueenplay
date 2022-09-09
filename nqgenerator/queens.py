from random import randint


class Queens:
    def __init__(self, n: int):
        self.number_of_queens = n
        self.chessboard = []
        
        self._queen_symbol = 'Q'
        self._queens_position = []
        self._attack_pairs = 0
        
        self._create_queens(n)
        self._create_chessboard(n)
        self._place_queens()
        self._count_attack_pairs()
    
    def show(self):
        # -----------------
        # |   | Q |   |   |
        # -----------------
        # |   | Q |   |   |
        # -----------------
        # |   |   |   |   |
        # -----------------
        # |   | Q | Q |   |
        # -----------------
        
        mult = (len(self.chessboard))
        
        print('  ' + ''.join([f'  {i+1} ' for i in range(self.number_of_queens)]))
        for i in range(self.number_of_queens):
            row = self.chessboard[i]
            print('  ' + '----'*mult + '-')
            print(f"{self.number_of_queens - i} | {' | '.join(row)} | {self.number_of_queens - i}")
        
        print('  ' + '----'*mult + '-')
        print('  ' + ''.join([f'  {i+1} ' for i in range(self.number_of_queens)]))
        print(f'Number of attacking pair(s): {self._attack_pairs}')
    
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
            pos_x = randint(1, n)
            pos_y = randint(1, n)
            if (pos_x, pos_y) not in x_y_positions:
                x_y_positions.append((pos_x, pos_y))
        
        # assign
        self._queens_position = x_y_positions
    
    def _place_queens(self):
        for pos in self._queens_position:
            x = pos[0] #self.number_of_queens - coord[0] - 1
            y = pos[1] #self.number_of_queens - coord[1] - 1
            if x >= 1 and y >= 1:
                x-=1
                y = self.number_of_queens - y
                self.chessboard[y][x] = self._queen_symbol
            else:
                raise ValueError('Only accept integer >= 1')
            
    def _count_gradient(self, pos_1: tuple, pos_2: tuple):
        x1, y1 = pos_1
        x2, y2 = pos_2
        m = (y2-y1)/(x2-x1) if x2-x1 != 0 else 0
        return m
        
    def _count_attack_pairs(self):
        pairs = []
        gradients = []
        for pos_1 in self._queens_position:
            for pos_2 in self._queens_position:
                pair = [pos_1, pos_2]
                pair.sort()
                if pos_1 != pos_2 and pair not in pairs:
                    gradient = self._count_gradient(pos_1, pos_2)
                    
                    pairs.append(pair)
                    gradients.append(gradient)
        
        attack_pairs = 0
        for gra in gradients:
            if abs(gra) == 0 or abs(gra) == 1:
                attack_pairs+=1 

        self._attack_pairs = attack_pairs