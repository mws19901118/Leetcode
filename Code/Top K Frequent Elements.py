class Solution:
    def findK(self, nums: List[int], count: dict, k: int) -> int:           #Find the k-th frequent element.
        smaller, larger = [], []
        for x in nums[1:]:
            if count[x] > count[nums[0]]:
                larger.append(x)
            else:
                smaller.append(x)
        if len(larger) == k - 1:
            return nums[0]
        elif len(larger) > k - 1:
            return self.findK(larger, count, k)
        else:
            return self.findK(smaller, count, k - 1 - len(larger))
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)                                               #Count each element.
        kth = self.findK(list(count.keys()), count, k)
        return [x for x in count.keys() if count[x] >= count[kth]]          #Return elements whose count is larger than or equal to the count of k-th frequent element.
