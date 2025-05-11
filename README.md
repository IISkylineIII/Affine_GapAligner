# Affine_GapAligner

# Description
AffineGapAligner is a Python implementation of the global sequence alignment algorithm with affine gap penalties. This method improves upon linear gap models by differentiating between gap opening and gap extension costs, providing biologically realistic alignments for DNA and protein sequences.

The function uses dynamic programming with three matrices (lower, middle, upper) to handle alignment states and performs traceback to construct the optimal alignment path between two sequences.

# Features
* Affine gap penalty model:
* Separate penalties for gap opening and gap extension.
* Dynamic programming:
* Uses three matrices: match/mismatch, gap-open, and gap-extend.
* Traceback support:
* Reconstructs aligned sequences after scoring.
* Returns both alignment score and aligned sequences.

# Function

```
affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w)
```

# Purpose
* Computes the optimal global alignment between two sequences using affine gap penalties and returns both the alignment score and the aligned sequences.

# Parameters
* match_reward (int): Score for matching characters (e.g., 1)
* mismatch_penalty (int): Penalty for mismatched characters (e.g., 5)
* gap_opening_penalty (int): Penalty to open a gap (e.g., 3)
* gap_extension_penalty (int): Penalty to extend a gap (e.g., 1)
* v (str): First sequence (e.g., DNA string)
* w (str): Second sequence (e.g., DNA string)

# Returns
* int: Optimal alignment score
* str: Aligned version of sequence v (including gaps)
* str: Aligned version of sequence w (including gaps)

# Example
```
match_reward = 1
mismatch_penalty = 5
gap_opening_penalty = 3
gap_extension_penalty = 1

v = "AGGTGGATCCTGTTGACGGTGCACCTGGTATTGCATGTGGATTGCACTTAAGCTCGTATCCGCCACAAGCACAACCCTCGTTGTCACGTG"
w = "AGGTGGATCCGATTGGCCTGGCAATCCTCATGTGGAGAACATTGCGCGCCTTATGCTTGTATCCGCACCCCAGATGTCACGTG"

score, aligned_v, aligned_w = affine_gap_alignment(
    match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w
)

print(score)
print(aligned_v)
print(aligned_w)
```
# Output
-15
AGGTGGATCCTG-TTGACGGTGCACCTGG--TAT--TGCATGT-G-G---ATT----GCACTTAAGCTCGTATCCGCCACAAGCACAACCCTC-GTTGTCACGTG
AGGTGGATCC-GATT----G-G--CCTGGCA-ATCCT-CATGTGGAGAACATTGCGCGC-CTTATGCTTGTAT----C-C--G--C-ACCC-CAGATGTCACGTG
