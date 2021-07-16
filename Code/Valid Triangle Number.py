class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()                                             #Sort nums.
        count = 0                                               #Initialize count to be 0.
        for i in reversed(range(len(nums))):                    #Let's say 3 numbers are a, b and c and a <= b <= c. Traverse c backwards from the end of nums.Because of a + b > c, so c >= b > c - a.
            k = i - 1                                           #Initialize the upperbound of index of b.
            for j in range(i):                                  #Traverse a forwards from the start of nums.
                k = max(k, j)                                   #The index of b cannot be smaller than the indxe of a.
                while k > j and nums[k] > nums[i] - nums[j]:    #While k > j and b > c - a, decrease k.
                    k -= 1
                count += i - k - 1                              #So the lowerbound of idnex of b is k + 1. Total valid b for given a and c is (i - 1) - (k + 1) + 1 = i - k - 1. Add i - k - 1 to count.
        return count                                            #Return count.
