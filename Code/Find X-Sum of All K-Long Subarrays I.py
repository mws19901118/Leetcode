class Solution:
    def find(self, nums: List[int], k: int, x: int) -> List[int]:
        count = Counter(nums[:k])                                               #Count numbers in nums[:k].
        sortedCount = SortedList((-j, -i) for i, j in count.items())            #Store the number and count pair in a sorted list in descending order.
        xSum = sum(i * j for i, j in sortedCount[:x])                           #Calculate the xSum for nums[:k].
        result = [xSum]                                                         #Initialize result with current xSum.

        def add(index: int) -> None:                                            #Add a number and count pair by index of original nums to sorted count then update xSum.
            nonlocal xSum
            pair = (-count[nums[index]], -nums[index])                          #Get the pair by index.
            pair_index = sortedCount.bisect_left(pair)                          #Search the pair in sorted count.
            if pair_index < x:                                                  #If the pair is top x, process.
                if len(sortedCount) >= x:                                       #If there are already x pairs in sorted count, we have to remove sortedCount[x - 1] from xSum.
                    xSum -= sortedCount[x - 1][0] * sortedCount[x - 1][1]
                xSum += pair[0] * pair[1]                                       #Add the current pair to xSum.
            sortedCount.add(pair)                                               #Also add it to sorted count.
        
        def remove(index: int) -> None:                                         #Remove a number and count pair by index of original nums from sorted count then update xSum.
            nonlocal xSum
            pair = (-count[nums[index]], -nums[index])                          #Get the pair by index.
            pair_index = sortedCount.bisect_left(pair)                          #Search the pair in sorted count.
            if pair_index < x:                                                  #If the pair is top x, process.
                if len(sortedCount) >= x + 1:                                   #If there are already x + 1 pairs in sorted count, we have to add sortedCount[x] to xSum.
                    xSum += sortedCount[x][0] * sortedCount[x][1]
                xSum -= pair[0] * pair[1]                                       #Remove the current pair from xSum.
            sortedCount.remove(pair)                                            #Also remove it from sorted count.

        for i in range(len(nums) - k):                                          #Traverse from 0 to len(nums) - k - 1.
            remove(i)                                                           #Remove index i.
            count[nums[i]] -= 1                                                 #Decrease count[nums[i]].
            if count[nums[i]] != 0:                                             #If count[nums[i]] is not zero, add index i.
                add(i)          
            if count[nums[i + k]] != 0:                                         #If count[nums[i + k]] is not zero, remove index i + k.
                remove(i + k)
            count[nums[i + k]] += 1                                             #Increase count[nums[i + k]].
            add(i + k)                                                          #Add index i + k.
            result.append(xSum)                                                 #Append xSum to result.
        return result
