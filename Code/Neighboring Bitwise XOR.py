class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not reduce(lambda x, y: x ^ y, derived)    #Each number has 2 occurrences towards the XOR result of derived list; which means the XOR result of drived list should be 0. 
