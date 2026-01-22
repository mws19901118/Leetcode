class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        prev = [i - 1 for i in range(len(nums))]                  #Store the previous index of each index.
        next = [i + 1 for i in range(len(nums))]                  #Store the next index of each index.
        prev.append(len(nums) - 1)                                #Add a dummy end(-1) of list whose previous index is len(nums) - 1.
        next[-1] = -1
        next.append(0)                                            #Add a dummy end(-1) of list whose next index is 0.
        heap = []
        desend = 0
        for i in range(1, len(nums)):                             #Traverse each adjacent pair.
            desend += int(nums[i - 1] > nums[i])                  #Increase desend if in the pair the left is greater than the right.
            heappush(heap, (nums[i - 1] + nums[i], i))            #Push the sum of pair and index of the right to the min heap.
        result = 0
        while desend:                                             #Iterate while there are desending pairs.
            s, r = heappop(heap)                                  #Pop heap.
            l = prev[r]                                           #Get the index of the left in the pair.
            if l == -1 or nums[l] + nums[r] != s:                 #If it is the dummy end or the current sum of the pair doesn't equal what popped from the min heap, continue as current pair sum is invalidated.
                continue
            if nums[l] > nums[r]:                                 #If current pair is desending, we decrease desend because this pair is removed.
                desend -= 1
            ll, rr = prev[l], next[r]                             #Get the left of left and the right of right.
            if ll != -1:                                          #If ll is not the dummy end, it will form a new pair with current left 
                desend += (nums[ll] > s) - (nums[ll] > nums[l])   #If nums[ll] is either larger than or not larger than both s and nums[l], the operation(remove current pair and creat a new pair) won't change the amont of desending pair; if it is larger than s but not greater than nums[l], the operation will creat a new desending pair; otherwise, the operation will remove a desending pair.
                heappush(heap, (nums[ll] + s, l))                 #Push the sum of new pair and l to the min heap.
            if rr != -1:                                          #If rr is not the dummy end, it will form a new pair with current left.
                desend += (s > nums[rr]) - (nums[r] > nums[rr])   #If nums[rr] is either smaller than or not smaller than both s and nums[r], the operation(remove current pair and creat a new pair) won't change the amont of desending pair; if it is smaller than s but not smaller than nums[r], the operation will creat a new desending pair; otherwise, the operation will remove a desending pair.
                heappush(heap, (nums[rr] + s, rr))                #Push the sum of new pair and rr to the min heap.
            next[l] = next[r]                                     #Set the next index of left to the next index of right.
            prev[next[r]] = l                                     #Set the prev index of the inext index of the right to the left.
            nums[l], nums[r] = s, inf                             #Update nums[l] the sum of pair then invalidate nums[r].
            result += 1                                           #Increase result.
        return result
