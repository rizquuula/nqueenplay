from nqueenplay import NQueen

N = 4
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
nqueens.show_attacking_pairs()