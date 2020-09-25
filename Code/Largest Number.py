class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a: str, b: str) -> int:                                             #Compare function: if the value of int(a + b)  is greater than that of int(b + a), a should be in front of b; vice versa.
            return int(b + a) - int(a + b)

        s = "".join(sorted([str(x) for x in nums], key=cmp_to_key(cmp)))            #Covert number to string, sort by compare function, then join together.
        return str(int(s))                                                          #Remove leading 0 and return.
