class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {i: x for i, x in enumerate(nums) if x != 0}                       #Store the non zero value by its index.

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(x * vec.map[i] for i, x in self.map.items() if i in vec.map)       #Calculate dot product.

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
