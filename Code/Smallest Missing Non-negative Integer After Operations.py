class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(x % value for x in nums)      #Count the remain of each number divided by value.
        min_count, offset = inf, -1                   #Initialize the min count and offset.
        for i in range(value):                        #Traverse from 0 to value - 1.
            if count[i] < min_count:                  #If count[i] is smaller than min count, update min count and offset.
                min_count = count[i]
                offset = i
        return count[offset] * value + offset         #We can only transform count[offset] numbers whose remain is offset. Thus MEX is count[offset] * value + offset.
