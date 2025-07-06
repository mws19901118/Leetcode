class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1                                                #Store nums1.
        self.nums2 = nums2                                                #Store nums2.
        self.nums2_count = Counter(nums2)                                 #Count each number in nums2.

    def add(self, index: int, val: int) -> None:
        self.nums2_count[self.nums2[index]] -= 1                          #Maintain the count of nums2.
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.nums2_count[tot - x] for x in self.nums1)         #Traverse nums1 and sum up the corresponding count in nums2 count that can make a pair equals to tot with each number in nums1.


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
