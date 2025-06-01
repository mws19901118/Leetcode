class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = comb(n + 2, 2)                                  #Initialize result to be the number of ways to distribute without limit. Suppose there are x candies, to distribute them to 3 children, the number of ways is (x + 1) * (x + 2) // 2. Because there are x - 1 gaps initially(including 2 edges), we can place a board in any gap, now there are x + 2 gaps. Place another board in any gap now, but divide by 2 because 2 boards are equal.
        if n - (limit + 1) + 2 >= 0:                             #Deduct the number of ways to distribute with at least one child over limit.
            result -= 3 * comb(n - (limit + 1) + 2, 2)           #To calculate that, assign limit + 1 to one child, then distribute the rest then multiply by 3(3 choices to choose over limit children).
        if n - (limit + 1) * 2 + 2 >= 0:                         #Add back the number of ways to distribute with at least two children over limit, because they are deducted twice.
            result += 3 * comb(n - (limit + 1) * 2 + 2, 2)       #To calculate that, assign limit + 1 to 2 children respectively, then distribute the rest then multiply by 3(3 choices to choose over limit children).
        if n - 3 * (limit + 1) + 2 >= 0:                         #Deduct the number of ways to distribute with qll children over limit.
            result -= comb(n - 3 * (limit + 1) + 2, 2)           #To calculate that, assign limit + 1 to 3 children respectively, then distribute the rest.
        return result
