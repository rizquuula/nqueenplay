from nqueenplay import NQueen

# N = 4
# nqueens = NQueen(n=N, number_lock=1)
# nqueens.get_attack_pairs()

# for i in range(N):
#     nqueens.move_random(i)
    
# nqueens.show()
# nqueens.show_attacking_pairs()

N = 8
nqueens = NQueen(n=N, number_lock=1)
nqueens.show()
nqueens.show_attacking_pairs()
