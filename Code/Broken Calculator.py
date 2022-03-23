class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        result = 0                                              #Work backward, using "divide by 2" and "add 1" to reach startValue from target. Take "divide by 2" as many as possible.
        while startValue < target:                              #While target is larger than startValue, add 1 if it is odd, else divide by 2. 
            while startValue < target and target % 2 == 0:
                target >>= 1
                result += 1
            if startValue < target:
                target += 1
                result += 1

        result += int(startValue - target)                      #Then, we need to do (startValue - target) additions to reach startValue.
        return result
