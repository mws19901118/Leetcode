class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = set([1, 2, 3, 4, 5, 6, 7, 8, 9])            #Initialize possible first digits.
        for i in range(n - 1):                          #Iterate n - 1 times.
            newq = set()                                #Initialize possible numbers of with i + 2 digits.
            for x in q:                                 #Traverse result from last iteration.
                d = x % 10                              #Get the last digit.
                if d + k < 10:                          #If d + k is a digit, add x * 10 + d + k to newq.
                    newq.add(x * 10 + d + k)
                if d - k >= 0:                          #If d - k is a digit, add x * 10 + d - k to newq.
                    newq.add(x * 10 + d - k)
            q = newq                                    #Replace q with newq.
        return q                                        #Return q.
