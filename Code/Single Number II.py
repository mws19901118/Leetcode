class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0                                                               #ones ^ num performs the same XOR operation you see in the duplicate entries version of Single Number.
        for num in nums:                                                                #& ~twos removes the newly added number if it's been seen twice.
            ones, twos = (ones ^ num) & ~twos, (ones & num) | (twos & ~num)             #ones & num takes the number if it's in ones.
        return ones                                                                     #twos & ~num takes the number only if it's not in twos.
