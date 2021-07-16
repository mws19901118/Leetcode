class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sum2 = {}                                                                                   #Store the list of index tuple of each pair whose sum is the key.                
        result = set()                                                                              #Intitalize a result set.
        for i in range(len(nums)):                                                                  #Traverse nums.
            for j in range(i + 1, len(nums)):                                                       #Traverse nums[i + 1:].
                if nums[i] + nums[j] not in sum2:                                                   #If nums[i] + nums[j] not already in sum2, initialize the list in sum2.
                    sum2[nums[i] + nums[j]] = []
                sum2[nums[i] + nums[j]].append((i, j))                                              #Append (i, j) to sum2[nums[i] + nums[j]].
        for x in sum2:                                                                              #Traverse the key in sum2.
            if target - x not in sum2:                                                              #If target - x is not in sum2, continue.
                continue
            for a, b in sum2[target - x]:                                                           #Traverse each pair in sum2[target - x].
                for c, d in sum2[x]:                                                                #Traverse each pair in sum2[x].
                    if a not in [c, d] and b not in [c, d]:                                         #If no duplicates exist in a, b, c, d, we found a quadruplet.
                        result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))             #Sort the quadruplet and comvert it to tuple then add it to result.
        return [list(q) for q in result]                                                            #Covert result to a list of quadruplet list and return.
