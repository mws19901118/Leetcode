class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modulo = [0] * 60
        for t in time:                                                                      #Count songs by their length % 60 remainder.
            modulo[t % 60] += 1
        count = modulo[0] * (modulo[0] - 1) // 2 + modulo[30] * (modulo[30] - 1) // 2       #Handle the case where remainder = 0 or 30, they can only pair with songs having same remainder。
        for i in range(1, 30):                                                              #Add each other pair to count.
            count += modulo[i] * modulo[60 - i]
        return count
