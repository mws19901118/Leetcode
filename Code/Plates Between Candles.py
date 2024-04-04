class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        neariestLeftCandle = [-1] * len(s)                                                                    #For each index, find the index of nearest candle on its left.
        left = -1
        for i in range(len(s)):
            if s[i] == '|':
                left = i
            neariestLeftCandle[i] = left
        neariestRightCandle = [-1] * len(s)                                                                   #For each index, find the index of nearest candle on its right.
        right = -1
        for i in reversed(range(len(s))):
            if s[i] == '|':
                right = i
            neariestRightCandle[i] = right
        platesFromLeft = {}                                                                                   #For each candle, count all the plates on its left.
        count = 0
        for i, x in enumerate(s):
            if s[i] == "*":
                count += 1
            else:
                platesFromLeft[i] = count
        result = [0] * len(queries)                                                                           #Initialize result.
        for i, (l, r) in enumerate(queries):                                                                  #Traverse queries.
            leftCandle, rightCandle = neariestRightCandle[l], neariestLeftCandle[r]                           #Find the leftCandle and rightCandle in query, which is the nearest candle on l's right and nearest candle on r's left.
            if rightCandle != -1 and leftCandle != -1 and leftCandle <= rightCandle:                          #If both is not -1 and leftCandle <= rightCandle, calculate number of plates in between, which is platesFromLeft[rightCandle] - platesFromLeft[leftCandle].
                result[i] = platesFromLeft[rightCandle] - platesFromLeft[leftCandle]
        return result
