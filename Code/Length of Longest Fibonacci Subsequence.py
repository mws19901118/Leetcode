class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length = defaultdict(dict)                                                   #Initialize a dict for each number to store the Fibonacci subsequence length ending at current number by the expected next number. 
        result = 2                                                                   #Initialize result to be 2 as it the Fibonacci subsequence should at least have 3 numbers.
        for i, x in enumerate(arr):                                                  #Traverse arr.
            for y in arr[:i]:                                                        #Traverse arr[:i].
                length[x][x + y] = (length[y][x] if x in length[y] else 1) + 1       #If x the next number of a Fibonacci subsequence ending at y, then length[x][x + y] is length[y][x] + 1 to extend the Fibonacci subsequence; otherwise length[x][x + y] is 2 to start a new potential Fibonacci subsequence.
                result = max(result, length[x][x + y])                               #Update result if necessary.
        return result if result > 2 else 0                                           #Return result if it's greater than 2; otherwise return 0.
