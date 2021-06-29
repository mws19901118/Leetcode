class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        indexes = deque()                             #Store the indexes of 0.
        count, start, result = 0, -1, 0               #Initialize count of 0, start of sliding window(not inclusive) and result.
        for i, x in enumerate(nums):                  #Traverse nums.
            if x == 0:                                #If x is 0, add its idnex to indexes and increase count by 1.
                indexes.append(i)
                count += 1
                if count > k:                         #If there are more than k 0, decrease count by 1 and set start to be the first index in indexes, thus we are maintain a sliding window with at most k 0.
                    count -= 1
                    start = indexes.popleft()
            result = max(result, i - start)           #Update result.
        return result
