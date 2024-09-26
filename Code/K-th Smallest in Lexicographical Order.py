class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(start, end):                         #Count numbers exist lexicographically in [start, end).
            numbers = 0                                #Initialize numbers.
            while start <= n:                          #Iterate while start <= n.
                numbers += min(n + 1, end) - start     #There are min(n + 1, end) - start numbers in current [start, end).
                start *= 10                            #Extend start to next digit by adding 0.
                end *= 10                              #Extend end to next digit by adding 0.
            return numbers
            
        curr = 1                                       #Start from 1.
        k -= 1                                         #Decrease k as we already uses 1.
        while k > 0:                                   #Traverse while k is greater than 0.
            step = count(curr, curr + 1)               #Calculate the numbers lexicographically in [curr, curr + 1).
            if step <= k:                              #If steps are less than or equal to k, skip this subtree of curr and decrease k by the steps.
                curr += 1
                k -= step
            else:                                      #Otherwise, move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1
        return curr
