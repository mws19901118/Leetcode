class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sortedWithIndex = sorted((x, i) for i, x in enumerate(nums))                                            #Sort nums and keep original index.
        i = 0
        while i < len(sortedWithIndex):                                                                         #Traverse sortedWithIndex.
            indexes, values = [sortedWithIndex[i][1]], [sortedWithIndex[i][0]]                                  #Initialize indexes and values in current segment with index and value at i.
            j = i + 1
            while j < len(sortedWithIndex) and sortedWithIndex[j][0] - sortedWithIndex[j - 1][0] <= limit:      #Traverse while current value can be reached from previous one in one swap. They can be sorted but remain their own set of indxees.
                indexes.append(sortedWithIndex[j][1])                                                           #Append current index to indexes.
                values.append(sortedWithIndex[j][0])                                                            #Append current value to values.
                j += 1                                                                                          #Move forward.
            for index, value in zip(sorted(indexes), values):                                                   #Traverse soeted indexes and values simultaneously.
                nums[index] = value                                                                             #Set nums[index] to value.
            i = j                                                                                               #Now we have sorted current segment so move i to j.
        return nums                                                                                             #Return nums.
