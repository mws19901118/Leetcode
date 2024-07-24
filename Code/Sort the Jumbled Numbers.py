class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(x: int) -> int:                                                        #Convert number to jumbled number.
            s = str(x)
            return sum(mapping[int(x)] * 10 ** (len(s) - 1 - i) for i, x in enumerate(s))
        return sorted(nums, key = lambda x: convert(x))                                    #Sort by jumbled number.
