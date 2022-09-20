import pytest

from nqueenplay import NQueen

@pytest.mark.parametrize(
    'number_of_queen, number_lock, num_of_pairs', [
    [8, 1, 12],
    [8, 2, 4],
    [20, 1, 17],
    [20, 2, 21],
    ])
def test_get_attack_pairs(number_of_queen: int, number_lock:int, num_of_pairs:int):
    nqueens = NQueen(number_of_queen, number_lock)
    pairs = nqueens.get_attack_pairs()
    assert len(pairs) == num_of_pairs
