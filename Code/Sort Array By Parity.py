class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if not x & 1] + [x for x in A if x & 1]        #Put even integers before odd integers.
