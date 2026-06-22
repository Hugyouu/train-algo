# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1


# Astuce : l'operateur XOR (^) possede 3 proprietes clefs
#   1. x ^ x = 0   -> deux valeurs identiques s'annulent
#   2. x ^ 0 = x   -> XOR avec 0 ne change rien
#   3. commutatif et associatif -> l'ordre des operations n'a aucune importance
# En faisant le XOR de TOUS les nombres, chaque paire s'annule (-> 0)
# et il ne reste que le nombre unique.
# Exemple [4,1,2,1,2] : 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1^1) ^ (2^2) = 4 ^ 0 ^ 0 = 4
def singleNumber(nums: list[int]) -> int:
    result = 0  # 0 est l'element neutre du XOR (propriete 2)
    for n in nums:
        result ^= n  # equivalent a : result = result ^ n
    return result  # toutes les paires se sont annulees, il reste l'unique