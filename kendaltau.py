from __future__ import print_function
import numpy as np
from itertools import combinations, permutations

def kendalltau_dist(rank_a, rank_b):
  tau = 0
  n_candidates = len(rank_a)
  for i, j in combinations(range(n_candidates), 2):
    tau += (np.sign(rank_a[i] - rank_a[j]) ==
            -np.sign(rank_b[i] - rank_b[j]))
    return tau
#
cols = "SBI BOB PNB Canara UBI IB BOI CBI PSB UCO IDBI ICICI HDFC Axis Kotak Yes".split()
ranks = np.array([[1, 12, 14, 6, 4, 9, 2, 16, 15, 3, 5, 7, 10, 8, 11, 13],
                  [1, 10, 5, 8, 6, 7, 12, 15, 16, 13, 14, 3, 2, 4, 9, 11],
                  [1, 6, 4, 6, 6, 6, 12, 14, 16, 13, 14, 1, 1, 4, 6, 6]])
kendalltau_dist(ranks[0], ranks[0])
print('d(NCIIPC, Volume) = {}'.format(kendalltau_dist(ranks[0], ranks[1])))
print('d(NCIIPC, Value) = {}'.format(kendalltau_dist(ranks[0], ranks[2])))
print('d(NCIIPC, X-Sector) = {}'.format(kendalltau_dist(ranks[1], ranks[2])))
