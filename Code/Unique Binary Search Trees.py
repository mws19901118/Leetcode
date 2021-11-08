class Solution:
    @cache                                                                                              #Cache result.
    def numTrees(self, n: int) -> int:
        return 1 if n <= 1 else sum(self.numTrees(i) * self.numTrees(n - 1 - i) for i in range(n))      #If n <= 1, return 1; otherwise, return the sum of number of trees of left child multiplied by that of right child when i(form 1 to n) is the root.
