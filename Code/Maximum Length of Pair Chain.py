class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])      #Sort by end value in asending order.
        curr = float('-inf')                  #Initialize current ending.
        result = 0

        for a, b in pairs:                    #Traverse pairs.
            if a > curr:                      #If starting is greater than current ending, we can add current pair to chain.
                result += 1                   #Increase result.
                curr = b                      #Update current ending.
        return result
