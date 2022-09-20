from nqueenplay import NQueen


N = 4
nqueens = NQueen(n=N, number_lock=1)
positions = nqueens.get_queen_position()
print(positions)