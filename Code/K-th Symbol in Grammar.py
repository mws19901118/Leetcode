class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:                                                                                  #If n == 1, return 0 because first row only has 0.
            return 0                                                                                #Found the following pattern after observation.
        half = 1 << (n - 2)                                                                         #Get the legnth of half row.
        return self.kthGrammar(n - 1, k) if k <= half else 1 - self.kthGrammar(n - 1, k - half)     #If k <= half, return self.kthGrammar(n -1, k) because first half is the duplicate of last row; otherwise, return 1 - self.kthGrammar(n - 1, k - half), because second half is the inverse of last row.
