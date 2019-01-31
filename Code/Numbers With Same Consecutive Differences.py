class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        def dp(n, valid):      
            if n == N:                                    #If current digit length is N, we have found all numbers. Add them to result. 
                result.extend(valid)
            else:                                         #Otherwise, we need to enumerate all possible number in next digit.
                nextD = []                                #Initialize a list for valid numbers in next digit.
                for t in valid:                           #For each number passed in valid number list.
                    d = t % 10                            #Calculate the last digit d.
                    if d + K <= 9:                        #Judge if d + K is valid and append it to nextD.
                        nextD.append(t * 10 + d + K)
                    if K != 0 and d - K >= 0:             #Judge if d - K is valid and append it to nextD. Don't need to do this if K is 0 to avoid duplicate.
                        nextD.append(t * 10 + d - K)
                dp(n + 1, nextD)                          #DP next digit.
        
        if N == 1:                                        #If N is 1, directly return 0 to 9.
            return [0,1,2,3,4,5,6,7,8,9]
        result = []                                       #Initialize result list.
        for i in range(1, 10):                            #DP from the first digit, 1 to 9.
            dp(1, [i])
        return result
