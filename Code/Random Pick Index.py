class Solution:

    def __init__(self, nums: List[int]):
        self.indexes = defaultdict(list)                            #Store the indexes of each number.
        for i, x in enumerate(nums):
            self.indexes[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indexes[target])                  #Randomly pick one from self.indexes[target].


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
