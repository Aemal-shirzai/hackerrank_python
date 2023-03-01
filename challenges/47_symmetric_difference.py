m_count = int(input())
M = set(map(int, input().split()))
n_count = int(input())
N = set(map(int, input().split()))

M_DiFFERENCE = M.difference(N)
N_DIFFERENCE = N.difference(M)

symettric_difference = list(M_DiFFERENCE.union(N_DIFFERENCE))
symettric_difference.sort()
for item in symettric_difference:
    print(item)