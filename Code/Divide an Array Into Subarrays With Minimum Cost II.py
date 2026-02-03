class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:        
        sl = SortedList()                                                            #Use a sorted list to store the numbers in sliding window.
        for i in range(1, min(len(nums), dist + 2)):                                 #Initialize the sliding window of length dist + 1, put dist + 1 numbers(all rest numbers if not enought) starting at 1 in the sorted list.
            sl.add(nums[i])
        s = sum(sl[i] for i in range(k - 1))                                         #Sum up the smallest k - 1 numbers in the sorted list as the initial sum in sliding window.
        result = nums[0] + s                                                         #Initialize result as nums[0] plus s.
        for i in range(1, len(nums) - dist - 1):                                     #Traverse from 1 to the last possible index of the start of sliding window.
            right = i + dist + 1                                                     #Calculate the index of number to be added to the sliding window.
            index = sl.index(nums[i])                                                #Find the index of nums[i] in the sorted list.
            sl.remove(nums[i])                                                       #Remove nums[i] from the sorted list to move it out of the sliding window.
            sl.add(nums[right])                                                      #Add nums[right] to the sorted list.
            rightIndexInSortedList = sl.index(nums[right])                           #Find its index in the sorted list.
            if index < k - 1:                                                        #If the index is smaller than k - 1, meaning the number moved out of the sliding window is in top k - 1 smallest.
                s -= nums[i]                                                         #Deduct it from s.
                s += nums[right] if rightIndexInSortedList < k - 1 else sl[k - 2]    #If added number is in top k - 1, add it to s; otherwise, we need to add the number at position k - 2, currently (k - 1)-th smallest in the sliding window, in sorted list to s.
            elif rightIndexInSortedList < k - 1:                                     #If the index is not smaller than k - 1 but the added number is in top k - 1, we need to add it to s then decrease the  number at k - 1, currently k-th smallest in the sliding window, from s.
                  s += nums[right] - sl[k - 1]
            result = min(result, nums[0] + s)                                        #Update result if nums[0] + s is smaller.
        return result
