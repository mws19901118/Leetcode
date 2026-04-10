class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indexes = defaultdict(list)                                      #Store the indexes of numbers by number value.
        for i, x in enumerate(nums):
            indexes[x].append(i)
        result = inf                                                     #Initialize result.
        for index in indexes.values():                                   #Traverse each index list.
            for i in range(2, len(index)):                               #Calculate the distance of each adjacent triplet.
                result = min(result, 2 * (index[i] - index[i - 2]))      #Update result if necessary.
        return result if result < inf else -1                            #Return result if it is not infinity; otherwise, return -1.
