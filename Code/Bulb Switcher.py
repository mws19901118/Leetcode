class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))                   #For each position x, each of its divisors will toggle once. Only square number will be toggled odd times, so return int(sqrt(n)).
