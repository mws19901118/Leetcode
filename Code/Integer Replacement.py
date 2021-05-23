class Solution:
    @cache                                                                          #Cache result.
    def search(self, n: int) -> int:                                                #Find the number of replacements needed.
        if n == 1:                                                                  #If n is already 1, return 0.
            return 0
        result = 0
        if n % 2:                                                                   #If n is odd, result is the min value of number of replacements of n - 1 and n + 1 plus 1.
            result = min(self.search(n + 1), self.search(n - 1)) + 1
        else:                                                                       #If n is even, result is the number of replacements of n / 2 plus 1.
            result = self.search(n / 2) + 1
        return result                                                               #Return result.
        
    def integerReplacement(self, n: int) -> int:
        return self.search(n)                                                       #Find the result recursively.
