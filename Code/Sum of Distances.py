class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexes = defaultdict(list)                                                                                #Store the indexes of each number.
        for i, x in enumerate(nums):
            indexes[x].append(i)
        result = [0] * len(nums)                                                                                   #Initialize result.
        for group in indexes.values():                                                                             #Traverse the group of inexes.
            result[group[0]] = sum(group[i] - group[0] for i in range(1, len(group)))                              #Calculate the sum of distance from rest of group to the first index and set it in result.
            for i in range(1, len(group)):                                                                         #Traverse the rest of indexes. Imagine all the indexes are on X-axis and then scan them from left to right. 
                result[group[i]] = result[group[i - 1]] + (group[i] - group[i - 1]) * (2 * i - len(group))         #Based on the previous distance, for current delta distance group[i] - group[i - 1], we will add it i - 1 times(i - 1 indexes before it) but minus it len(group) - 1 - i times(len(group) - 1 - i) indexes after it.
        return result
