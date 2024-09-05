class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        n_sum = mean * (n + len(rolls)) - sum(rolls)                #Calculate the sum of n.
        if n_sum < n or n_sum > 6 * n:                              #If sum is smaller than n or greater than 6 * n, there is no possible solution.
            return []
        n_mean, gap = divmod(n_sum, n)                              #Calculate the mean of n and the gap between sum and total of if all n rolls are at the mean value of n.
        return [n_mean] * (n - gap) + [n_mean + 1] * gap            #Then, we put all n rolls at the mean value of n and increase gap rolls by 1.
