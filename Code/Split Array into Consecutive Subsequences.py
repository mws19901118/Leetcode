from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)                                 #Count each number.
        endMap = Counter()                                    #Store the count of consecutive subsequence ending at a certain number.
        for x in nums:                                        #Traverse through nums.
            if not count[x]:                                  #If count is 0, the occurences of current number has all been distributed into subsequence, so skip to next number.
                continue
            if not endMap[x - 1]:                             #If no subsequence ends at x - 1, create a new subsequence starting from x.
                if not count[x + 1] or not count[x + 2]:      #If there is no x + 1 or no x + 2, cannot create a new subsequence, so x cannot be distributed into any subsequence, then return false.
                    return False
                count[x] -= 1                                 #Decrease the count of x, x + 1 and x + 2.
                count[x + 1] -=1
                count[x + 2] -= 1
                endMap[x + 2] += 1                            #Increase the count of subsequence ending at x + 2.
            else:                                             #Otherwise, distribute x to the subsequence ending at x - 1.
                count[x] -= 1                                 #Decrease for the count of x.
                endMap[x - 1] -= 1                            #Decrease the count of subsequence ending at x - 1.
                endMap[x] += 1                                #MIncrease the count of subsequence ending at x.
        return True                                           #After the traverse, return true as we found a way to split the list.
