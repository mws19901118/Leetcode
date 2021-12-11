class Solution:
    def gcd(self, a: int, b: int) -> int:                             #Calculate gcd of 2 numbers.
        return a if not b % a else self.gcd(b % a, a)
    
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        division = 10 ** 9 + 7                                        #Division is 10 ** 9 + 7.
        lcm = a * b // self.gcd(a, b)                                 #Calculate lcm of a and b.
        start, end = 0, n * min(a, b)                                 #Binary search between 0 and n * min(a, b), because the nth magical number can't be greater than n * min(a, b).
        while start < end:
            mid = (start + end) // 2                                  #Calculate mid.
            if  mid // a + mid // b - mid // lcm < n:                 #There are (mid // a + mid // b - mid // lcm) magical numbers not greater than mid. If it's smaller than n, set start to mid + 1.
                start = mid + 1
            else:                                                     #Otherwise, set end to mid.
                end = mid
        return start % division                                       #Return start % division.
