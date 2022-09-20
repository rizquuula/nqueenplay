from nqueenplay import NQueen


N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
nqueens.move_to(2, 1)
nqueens.show()