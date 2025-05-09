class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        s = sum(int(x) for x in num)                                                                    #Calculate the sum of num.
        if s & 1:                                                                                       #Return 0 if sum is odd.
            return 0
        division = 10 ** 9 + 7                                                                          #Initialize division.
        target = s >> 1                                                                                 #Calculate target, which is half of sum.
        count = Counter([int(x) for x in num])                                                          #Count each digit.
        prefix = [0] * 11                                                                               #Build a prefix sum of number of digits left, from 0 to 9.
        for i in reversed(range(10)):
            prefix[i] = prefix[i + 1] + count[i]

        @cache                                                                                          #Cache result.
        def dfs(digit: int, odd_sum: int, odd_remain: int) -> int:                                      #DFS with current digit, sum and reamin of odd positions.
            if odd_remain < 0 or prefix[digit] < odd_remain or odd_sum > target:                        #If odd positions remain is smaller than 0 or not enough digits to fill odd positions or odd sum is greater than target, return 0.
                return 0
            if digit > 9:                                                                               #If digit reaches the end, return if odd positions sum is target and no more odd positions remain.
                return int(odd_sum == target and odd_remain == 0)
            even_remain = prefix[digit] - odd_remain                                                    #Calculate even positions remain.
            result = 0                                                                                  #Initialize result.
            for i in range(max(0, count[digit] - even_remain), min(count[digit], odd_remain) + 1):      #Try to distribute i of current digits to odd positions and rest to even positions.
                ways = comb(odd_remain, i) * comb(even_remain, count[digit] - i) % division             #The ways of assignment is comb(odd_remain, i) * comb(even_remain, count[digit] - i) % division.
                result += ways * dfs(digit + 1, odd_sum + i * digit, odd_remain - i)                    #So add ways of assignment multiplied by the next iteration of dfs(after taking modulo) to result.
            return result % division                                                                    #Return result after taking modulo.

        return dfs(0, 0, (len(num) + 1) >> 1)                                                           #Return the result of dfs from beginning.
