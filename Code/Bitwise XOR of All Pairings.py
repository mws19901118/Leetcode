class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums1XOR, nums2XOR = reduce(lambda x, y: x ^ y, nums1), reduce(lambda x, y: x ^ y, nums2)      #Calculate the XOR results of nums1 and nums2 respectively.
        return (nums1XOR if len(nums2) & 1 else 0) ^ (nums2XOR if len(nums1) & 1 else 0)               #Let's say numbers in nums1 are a1, a2, ..., am and numbers in nums2 are b1, b2, ..., bn.
                                                                                                       #So, final result is (a1 ^ b1) ^ (a2 ^ b1) ^ ... ^ (am ^ b1) ^ (a1 ^ b2) ^ ... ^ (am ^ bn).
                                                                                                       #For each number ai in nums1, it has impact ai ^ (b1 ^ b2 ^ ... ^ bn) = a1 ^ nums2XOR to the final result.
                                                                                                       #So, nums2XOR repeats m times and it will have impact if m is odd while no impact if m is even.
                                                                                                       #Same applies for nums1XOR.
                                                                                                       #Thus, final result is (nums1XOR if len(nums2) & 1 else 0) ^ (nums2XOR if len(nums1) & 1 else 0).
