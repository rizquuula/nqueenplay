from nqueenplay import NQueen

nqueens = NQueen(n=8, number_lock=1)
nqueens.show()
nqueens.show_attacking_pairs()

nqueens.move_down(2, 6)
nqueens.show()
nqueens.show_attacking_pairs()
