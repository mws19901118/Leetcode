class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.length = len(nums)                             #Record current length of segment.
        if self.length == 0:
            self.sum = 0
        elif self.length == 1:
            self.sum = nums[0]
        else:                                               #If current length is larger than 2, build left segment and right segment recursively.
            mid = self.length / 2
            self.left = NumArray(nums[:mid])
            self.right = NumArray(nums[mid:])
            self.sum = self.left.sum + self.right.sum       #Update currrent sum.

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if self.length == 0:                                #If current length is 0, do nothing.
            return
        elif self.length == 1:
            self.sum = val
            return
        else:                                               #If current length is larger than 2, update left segment or right segment recursively.
            mid = self.length / 2
            if i < mid:
                self.left.update(i, val)
            else:
                self.right.update(i - mid, val)
            self.sum = self.left.sum + self.right.sum       #Update current sum.
            return

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:                                           #If i > j, range does not exist, return.
            return 0
        if self.length <= 1:                                #If current length is not larger than 1, directly return current sum.
            return self.sum
        elif self.length == j - i + 1:                      #If current length equals the length of range, directly return current sum.
            return self.sum
        else:
            mid = self.length / 2
            if mid >= i and mid <= j:                       #If mid is between i and j, divide range into 2 ranges and return the sum of sum of each range.
                return self.left.sumRange(i, mid - 1) + self.right.sumRange(0, j - mid)
            elif mid < i:                                   #Otherwise, find the sum in left segment or right segment.
                return self.right.sumRange(i - mid, j - mid)
            else:
                return self.left.sumRange(i, j)
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
