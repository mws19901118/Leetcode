class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)                  #Count each task difficulty.
        rounds = 0
        for k, v in count.items():              #Traverse each difficulty and its count.
            if v == 1:                          #If the count is 1, cannot be fulfilled, return -1.
                return -1
            rounds += ceil(v / 3)               #Otherwise, it taks ceil(v / 3) to fulfil all tasks at current difficulty level. The count can be 3 * k(k rounds of 3 tasks), 3 * k + 1(k - 1 rounds of 3 tasks and 2 round of 2 tasks), 3 * k + 2(k rounds of 3 tasks and 1 round of 2 tasks). 
        return rounds

