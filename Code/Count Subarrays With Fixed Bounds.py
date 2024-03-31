class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0                                                                       #Initialize count.
        i = 0                                                                           #Initialize the left boundary of sliding window.
        while i < len(nums):                                                            #Traverse nums.
            if nums[i] < minK or nums[i] > maxK:                                        #If nums[i] is not within bound, move to next.
                i += 1
                continue
            j = i                                                                       #Initialize the right boundary.
            minK_q, maxK_q = deque(), deque()                                           #Initialize the indexes of minK and maxK within current window.
            while j < len(nums) and minK <= nums[j] <= maxK:                            #Move the right boundary as far as possible.
                if nums[j] == minK:                                                     #Push j to minK_q if nums[j] == minK.
                    minK_q.append(j)
                if nums[j] == maxK:                                                     #Push j to maxK_q if nums[j] == maxK.
                    maxK_q.append(j)
                j += 1
            while i < j and minK_q and maxK_q:                                          #Move left boundary while nums[i:j] is valid subarray with fixed bound.
                count += j - max(minK_q[0], maxK_q[0])                                  #For each k in max(minK_q[0], maxK_q[0] to j - 1. nums[i:k + 1] is valid subarray with fixed bound.
                if i == minK_q[0]:                                                      #If i == minK_q[0], pop left minK_q[0].
                    minK_q.popleft()
                if i == maxK_q[0]:                                                      #If i == maxK_q[0], pop left maxK_q[0].
                    maxK_q.popleft()
                i += 1
            i = j                                                                       #Set i to j.
        return count                                                                    #Return count.
