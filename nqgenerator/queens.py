from random import randint, uniform
import random

class MovementException(Exception):
    ...
    
class MovementDirection:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'

class Queens:
    def __init__(self, n: int, number_lock: int=0):
        self.number_of_queens = n
        self.queens_position = []
        
        self._chessboard = []
        self._queen_symbol = 'Q'
        self._attack_pairs = 0
        
        self._create_queens(n, number_lock)
        self._place_queens()
        self._count_attack_pairs()
    
    # def move_left(self, queens_index: int):
    #     self._move(queens_index, MovementDirection.LEFT)
    
    def move_up(self, queens_index: int, movement_length: int=1):
        self._move(queens_index, MovementDirection.UP, movement_length)
    
    # def move_right(self, queens_index: int):
    #     self._move(queens_index, MovementDirection.RIGHT)
    
    def move_down(self, queens_index: int, movement_length: int=1):
        self._move(queens_index, MovementDirection.DOWN, movement_length)
    
    def _get_next_pos(self, pos: tuple, direction: str, movement_length:int):
        next_position = ()
        x, y = pos
        if direction == MovementDirection.LEFT:
            next_position = (x-movement_length, y)
        elif direction == MovementDirection.RIGHT:
            next_position = (x+movement_length, y)
        elif direction == MovementDirection.UP:
            next_position = (x, y+movement_length)
        elif direction == MovementDirection.DOWN:
            next_position = (x, y-movement_length)
        else:
            raise MovementException('Invalid movement direction')
        return next_position
    
    def _check_movement_pos_index(self, pos: tuple):
        return pos[0] < 1 or pos[1] < 1 or pos[0] > self.number_of_queens or pos[1] > self.number_of_queens
        
    
    def _move(self, queens_index: int, direction: str, movement_length: int):
        queens_index-=1
        next_position = self._get_next_pos(
            pos=self.queens_position[queens_index],
            direction=direction,
            movement_length=movement_length,
            )
        
        if next_position in self.queens_position:
            raise MovementException('There are other Queen in this place')
        elif self._check_movement_pos_index(next_position):
            raise MovementException('Movement index out of range')
        else:
            self.queens_position[queens_index] = next_position
            self._place_queens()
            
    
    def show(self):
        mult = self.number_of_queens
        
        print('  ' + ''.join([f'  {i+1} ' for i in range(self.number_of_queens)]))
        for i in range(self.number_of_queens):
            row = self._chessboard[i]
            print('  ' + '----'*mult + '-')
            print(f"{self.number_of_queens - i} | {' | '.join(row)} | {self.number_of_queens - i}")
        
        print('  ' + '----'*mult + '-')
        print('  ' + ''.join([f'  {i+1} ' for i in range(self.number_of_queens)]))
        print(f'Number of attacking pair(s): {self._attack_pairs}')
        
        queens_pos = [f"Q{i+1}={self.queens_position[i]}" for i in range(self.number_of_queens)]
        print(f'Queen positions: {", ".join(queens_pos)}')
    
    def _create_chessboard(self, n: int):
        chessboard = []
        for x in range(n):
            row = []
            for y in range(n):
                row.append(' ')
            chessboard.append(row)
        
        # assign
        self._chessboard = chessboard
    
    def _create_queens(self, n:int, number_lock: int=0):
        if number_lock != 0:
            random.seed(number_lock)
            
        x_y_positions = []
        pos_x = 1
        while len(x_y_positions) < n:
            # pos_x = round(uniform(1, n))
            pos_y = round(uniform(1, n))
            if (pos_x, pos_y) not in x_y_positions:
                x_y_positions.append((pos_x, pos_y))
                pos_x+=1
        
        # assign
        self.queens_position = x_y_positions
    
    def _place_queens(self):
        self._create_chessboard(self.number_of_queens)
        
        for pos in self.queens_position:
            x = pos[0] #self.number_of_queens - coord[0] - 1
            y = pos[1] #self.number_of_queens - coord[1] - 1
            if x >= 1 and y >= 1:
                x-=1
                y = self.number_of_queens - y
                self._chessboard[y][x] = self._queen_symbol
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
        for pos_1 in self.queens_position:
            for pos_2 in self.queens_position:
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