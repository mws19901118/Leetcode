class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter(sum(int(x) for x in str(i)) for i in range(1, n + 1))    #Count the numbers by its sum of digits.
        max_count = max(count.values())                                          #Get the max count
        return sum(count[x] == max_count for x in count)                         #Count the groups with max count.
