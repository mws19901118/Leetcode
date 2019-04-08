class Solution:
    def search(self, n, cache):                                                     #Find the number of replacements needed.
        if n == 1:                                                                  #If n is already 1, return 0.
            return 0
        if n in cache:                                                              #If n is in cache, return cache[n].
            return cache[n]
        result = 0
        if n % 2:                                                                   #If n is odd, result is the min value of number of replacements of n - 1 and n + 1 plus 1.
            result = min(self.search(n + 1, cache), self.search(n - 1, cache)) + 1
        else:                                                                       #If n is even, result is the number of replacements of n / 2 plus 1.
            result = self.search(n / 2, cache) + 1
        cache[n] = result                                                           #Add result to cache.
        return result                                                               #Return result.
        
    def integerReplacement(self, n: int) -> int:
        return self.search(n, {})                                                   #Find the result recursively with a dict to cachce intermediate result.
