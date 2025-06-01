class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = comb(n + 2, 2)                                  #Initialize result to be the number of ways to distribute without limit.
        if n - (limit + 1) + 2 >= 0:                             #Deduct the number of ways to distribute with at least one child over limit.
            result -= 3 * comb(n - (limit + 1) + 2, 2)           #To calculate that, assign limit + 1 to one child, then distribute the rest then multiply by 3(3 choices to choose over limit children).
        if n - (limit + 1) * 2 + 2 >= 0:                         #Add back the number of ways to distribute with at least two children over limit, because they are deducted twice.
            result += 3 * comb(n - (limit + 1) * 2 + 2, 2)       #To calculate that, assign limit + 1 to 2 children respectively, then distribute the rest then multiply by 3(3 choices to choose over limit children).
        if n - 3 * (limit + 1) + 2 >= 0:                         #Deduct the number of ways to distribute with qll children over limit.
            result -= comb(n - 3 * (limit + 1) + 2, 2)           #To calculate that, assign limit + 1 to 3 children respectively, then distribute the rest.
        return result
