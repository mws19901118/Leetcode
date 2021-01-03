class Solution:
    def backtracking(self, n: int, position: int, divisible: dict, visited: set) -> int:      #Backtracking.
        if position == n:                                                                     #If current position equals n, backtracking reaches end, so return 1 for finding beautiful arrangement.
            return 1
        count = 0                                                                             #Count the number of beautiful arrangements from this position.
        for x in divisible[position + 1]:                                                     #Try all possible integers at this position.
            if x not in visited:                                                              #If x is already visited, skip.
                position += 1                                                                 #Increase to next position.
                visited.add(x)                                                                #Add x to visited.
                count += self.backtracking(n, position, divisible, visited)                   #Backtracking for next position.
                visited.remove(x)                                                             #Remove x from visited.
                position -= 1                                                                 #Fall back to current position.
        return count
    
    def countArrangement(self, n: int) -> int:
        divisible = defaultdict(list)                                                         #Preprocesse: find out the integers can be arranged at each index.
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    divisible[j].append(i)
        return self.backtracking(n, 0, divisible, set())                                      #Backtracking from the first index.
