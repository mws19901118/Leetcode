class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    def rotate(self, nums, k):
        while k:
            nums.insert(0,nums.pop())           #Pop the end element and insert it at the front.
            k-=1
