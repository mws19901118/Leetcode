class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)                                                #Count each answer.
        return sum((x + 1) * ceil(count[x] / (x + 1)) for x in count)           #For each answer x, (x + 1) rabbits can form a group that satisfy the answer, thus sum up (x + 1) * ceil(count[x] / (x + 1)) for each answer x.
