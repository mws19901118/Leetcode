class FenwickTree:                                                                      #Fenwick Tree class.
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n, result = len(nums1), 0                                                      #Get the length and initialize result.
        index_2 = {x: i for i, x in enumerate(nums2)}                                  #Populate the index of each number in nums2.
        reverse_index_mapping = {index_2[x]: i for i, x in enumerate(nums1)}           #Build a index mapping for index in nums 2 to index in nums 1 for same number.
        tree = FenwickTree(n)                                                          #Initialize a Fenwick Tree for of size n.
        for i in range(n):                                                             #Traverse each index.
            j = reverse_index_mapping[i]                                               #I is index in nums2, find its corresponding index j in nums1.
            left = tree.query(j)                                                       #Query the sum before index j in Fenwick Tree, which is the count of numbers which are visited in nums2 and have indexes smaller than j in nums1.
            tree.update(j, 1)                                                          #Increase 1 to index j in Fenwick Tree to mark it as visited.
            right = (n - 1 - j) - (i - left)                                           #There are n - 1 - j numbers on the right of j and we have visited i - left numbers that have indexes larger than j; so in total, there are still (n - 1 - j) - (i - left) numbers which are unvisited in nums2 and have indexes larger than j in nums1
            result += left * right                                                     #For each number pair in left(x) and right(y), they can form a good triplet with nums1[j], i.e. (x, nums1[j], y).
        return result
