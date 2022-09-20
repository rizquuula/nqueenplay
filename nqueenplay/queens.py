from random import choice, randint, uniform, seed
from typing import List, Tuple

from .exceptions import MovementIndexException, OverlappingQueenException, MovementDirectionException
from .move_direction import MovementDirection


class NQueen:
    '''N-Queens Puzzle'''

    def __init__(self, n: int, number_lock: int = 0):
        self._queens_position = []
        self._number_of_queens = n
        self._chessboard = []
        self._queen_symbol = 'Q'

        self._create_random_queens(n, number_lock)
        self._place_queens()

    def get_number_of_queens(self) -> int:
        """Get number of Queens

        Returns:
            int: Number of Queens
        """
        return self._number_of_queens

    def get_queen_positions(self) -> List[Tuple[int, int]]:
        """Get Queen positions

        Returns:
            List[Tuple[int, int]]: Queen positions
        """
        return self._queens_position

    def move_up(self, queen_pos: int, movement_length: int = 1) -> None:
        """Move the selected Queen up side

        Args:
            queen_pos (int): index of selected Queen
            movement_length (int, optional): movement length. Defaults to 1.
        """
        self._move(queen_pos, MovementDirection.UP, movement_length)

    def move_down(self, queen_pos: int, movement_length: int = 1) -> None:
        """Move the selected Queen down side

        Args:
            queen_pos (int): index of selected Queen
            movement_length (int, optional): movement length. Defaults to 1.
        """
        self._move(queen_pos, MovementDirection.DOWN, movement_length)

    def move_to(self, queen_pos: int, target_pos: int) -> None:
        """Move the selected Queen to specific row or neighbor

        Args:
            queen_pos (int): index of selected Queen
            next_pos (int): target position.
        """
        queen_index = queen_pos-1 # Note: queen_index != queen_pos
        _, current_queen_row = self.get_queen_positions()[queen_index]
        movement_length = target_pos-current_queen_row
        self._move(queen_pos, MovementDirection.UP, movement_length)

    def move_random(self, queen_pos: int) -> None:
        """Randomly move the selected Queen

        Args:
            queen_pos (int): index of selected Queen
        """
        try:
            direction = choice([MovementDirection.DOWN, MovementDirection.UP])
            movement_length = randint(1, self._number_of_queens)
            self._move(queen_pos, direction, movement_length)
        except MovementIndexException:
            self.move_random(queen_pos)

    def get_attack_pairs(self) -> List[Tuple[int, int]]:
        """Get attack pairs, each pair consist from two Queen index

        Returns:
            List[Tuple[int, int]]: attack pairs
        """
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

        attack_pairs = []
        for i, gra in enumerate(gradients):
            pair = pairs[i]
            if abs(gra) == 0 or abs(gra) == 1:
                attack_pairs.append(pair)

        return attack_pairs

    def show_attacking_pairs(self) -> None:
        """Print attack pairs to console
        """
        # attack pairs
        attack_pairs = self.get_attack_pairs()
        print('attack_pairs', [(p[0][0], p[1][0]) for p in attack_pairs])
        print(f'Number of attacking pair(s): {len(attack_pairs)}')

    def show(self) -> None:
        """Print current chessboard to console
        """
        # chessboard
        mult = self._number_of_queens
        print(
            '  ' + ''.join([f'  {i+1} ' for i in range(self._number_of_queens)]))
        for i in range(self._number_of_queens):
            row = self._chessboard[i]
            print('  ' + '----'*mult + '-')
            print(
                f"{self._number_of_queens - i} | {' | '.join(row)} | {self._number_of_queens - i}")

        print('  ' + '----'*mult + '-')
        print(
            '  ' + ''.join([f'  {i+1} ' for i in range(self._number_of_queens)]))

    def _get_next_pos(self, pos: tuple, direction: str, movement_length: int) -> Tuple[int, int]:
        '''Get next position using movement'''
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
            raise MovementDirectionException('Invalid movement direction')
        return next_position

    def _check_movement_pos_index(self, pos: tuple) -> bool:
        '''Check, is the movement position is valid or not based on index'''
        return pos[0] < 1 or pos[1] < 1 \
            or pos[0] > self._number_of_queens or pos[1] > self._number_of_queens

    def _move(self, queen_pos: int, direction: str, movement_length: int) -> None:
        '''Move queen with direction and length'''
        queen_pos -= 1
        next_position = self._get_next_pos(
            pos=self._queens_position[queen_pos],
            direction=direction,
            movement_length=movement_length,
        )

        if next_position in self._queens_position:
            raise OverlappingQueenException(
                'There are other Queen in this place')
        elif self._check_movement_pos_index(next_position):
            raise MovementIndexException('Movement index out of range')
        else:
            self._queens_position[queen_pos] = next_position
            self._place_queens()

    def _create_initial_chessboard(self, n: int) -> None:
        '''Initial blank chessboard, use this to refresh chessboard'''
        chessboard = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(' ')
            chessboard.append(row)

        # assign
        self._chessboard = chessboard

    def _create_random_queens(self, n: int, number_lock: int = 0) -> None:
        '''Create random queen position'''
        if number_lock != 0:
            seed(number_lock)

        x_y_positions = []
        pos_x = 1
        while len(x_y_positions) < n:
            # pos_x = round(uniform(1, n))
            pos_y = round(uniform(1, n))
            if (pos_x, pos_y) not in x_y_positions:
                x_y_positions.append((pos_x, pos_y))
                pos_x += 1

        # assign
        self._queens_position = x_y_positions

    def _place_queens(self) -> None:
        '''Place queen position to board'''
        self._create_initial_chessboard(self._number_of_queens)

        for pos in self._queens_position:
            # check position validation
            if not self._check_movement_pos_index(pos):
                x = pos[0] - 1
                y = self._number_of_queens - pos[1]
                self._chessboard[y][x] = self._queen_symbol
            else:
                raise ValueError('Only accept integer >= 1')

    def _count_gradient(self, pos_1: tuple, pos_2: tuple) -> float:
        '''Count the gradient between two point'''
        x1, y1 = pos_1
        x2, y2 = pos_2
        m = (y2-y1)/(x2-x1) if x2-x1 != 0 else 0
        return m
