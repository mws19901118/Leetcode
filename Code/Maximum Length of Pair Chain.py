class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])      #Sort by end value in asending order.
        curr = float('-inf')                  #Initialize current max ending.
        result = 0

        for a, b in pairs:                    #Traverse pairs.
            if a > curr:                      #If starting is greater than current ending, because current ending is smaller than any ending after it, adding current pair to chain is optimal.
                result += 1                   #Increase result.
                curr = b                      #Update current max ending.
        return result
