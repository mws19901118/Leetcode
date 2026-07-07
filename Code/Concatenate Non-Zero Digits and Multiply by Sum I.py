class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [x for x in str(n) if x != '0']                                        #Get the non zero digits.
        return int("".join(digits)) * sum(int(x) for x in digits) if digits else 0      #Calculate result and return.
