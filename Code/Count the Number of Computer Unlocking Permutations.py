class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        return 0 if any(x <= complexity[0] for x in complexity[1:]) else factorial(len(complexity) - 1) % (10 ** 9 + 7)      #Any computer with a complexity not greater than the label 0 computer cannot by decyphered, thus return 0 if there are such cumputers; then fix the label 0 computer we can decipher the rest in any order, which is factorial(len(complexity) - 1) % (10 ** 9 + 7).
