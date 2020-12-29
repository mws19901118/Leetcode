#https://leetcode.com/problems/reach-a-number/discuss/990399/Python-Math-O(1)-solution-explained
class Solution:
    def reachNumber(self, target: int) -> int:
        bound = ceil(sqrt(2 * abs(target) + 0.25) - 0.5)
        if target % 2 == 0:
            if bound % 4 == 1: bound += 2
            if bound % 4 == 2: bound += 1
        else:
            if bound % 4 == 3: bound += 2
            if bound % 4 == 0: bound += 1
                
        return bound
        
#https://leetcode.com/problems/reach-a-number/discuss/112986/Concise-Python-with-explanation-and-example
class Solution:
    def reachNumber(self, target: int) -> int:
        t = abs(target)
        n = math.floor(math.sqrt(2 * t))
        while True:
            to_minus = ((n + 1) * n) // 2 - t 
            if to_minus >= 0:  
                if to_minus % 2 == 0:
                    return int(n)
            n += 1
