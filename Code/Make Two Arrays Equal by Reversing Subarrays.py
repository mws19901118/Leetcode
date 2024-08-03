class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)      #If target and arr have same elements, they can be made equal by reversing subarray in a selection sort fashion.
