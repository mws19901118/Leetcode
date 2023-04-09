class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = defaultdict(list)                     #Group the indexes of each value in nums2 in a list.
        for i, x in enumerate(nums2):
            indexes[x].append(i)
        result = []
        for x in nums1:                                 #Traverse nums1.
            result.append(indexes[x][-1])               #Add the last index of x in nums2 to result.
            indexes[x].pop()                            #Pop the last index of x from indexes[x].
        return result
