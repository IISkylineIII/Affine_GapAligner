def affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w):
    n = len(v)
    m = len(w)

    lower = [[0] * (m + 1) for _ in range(n + 1)]
    middle = [[0] * (m + 1) for _ in range(n + 1)]
    upper = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        lower[i][0] = -gap_opening_penalty - (i - 1) * gap_extension_penalty
        middle[i][0] = -gap_opening_penalty - (i - 1) * gap_extension_penalty
        upper[i][0] = float('-inf')

    for j in range(1, m + 1):
        upper[0][j] = -gap_opening_penalty - (j - 1) * gap_extension_penalty
        middle[0][j] = -gap_opening_penalty - (j - 1) * gap_extension_penalty
        lower[0][j] = float('-inf')

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            lower[i][j] = max(lower[i - 1][j] - gap_extension_penalty, middle[i - 1][j] - gap_opening_penalty)
            upper[i][j] = max(upper[i][j - 1] - gap_extension_penalty, middle[i][j - 1] - gap_opening_penalty)
            match = match_reward if v[i - 1] == w[j - 1] else -mismatch_penalty
            middle[i][j] = max(lower[i][j], middle[i - 1][j - 1] + match, upper[i][j])

    alignment_score = middle[n][m]

    # Backtrack to find the alignment
    i, j = n, m
    align_v, align_w = '', ''

    while i > 0 and j > 0:
        current_score = middle[i][j]
        if current_score == middle[i - 1][j - 1] + (match_reward if v[i - 1] == w[j - 1] else -mismatch_penalty):
            align_v = v[i - 1] + align_v
            align_w = w[j - 1] + align_w
            i -= 1
            j -= 1
        elif current_score == lower[i][j]:
            align_v = v[i - 1] + align_v
            align_w = '-' + align_w
            i -= 1
        else:
            align_v = '-' + align_v
            align_w = w[j - 1] + align_w
            j -= 1

    while i > 0:
        align_v = v[i - 1] + align_v
        align_w = '-' + align_w
        i -= 1

    while j > 0:
        align_v = '-' + align_v
        align_w = w[j - 1] + align_w
        j -= 1

    return alignment_score, align_v, align_w

# Sample Input
match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty = 1, 5, 3, 1
v = "AGGTGGATCCTGTTGACGGTGCACCTGGTATTGCATGTGGATTGCACTTAAGCTCGTATCCGCCACAAGCACAACCCTCGTTGTCACGTG"
w = "AGGTGGATCCGATTGGCCTGGCAATCCTCATGTGGAGAACATTGCGCGCCTTATGCTTGTATCCGCACCCCAGATGTCACGTG"

alignment_score, aligned_v, aligned_w = affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w)
print(alignment_score)
print(aligned_v)
print(aligned_w)
