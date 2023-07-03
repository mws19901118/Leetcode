class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):                                                                                                #The length of s and goal must be equal.
            return False
        misMatches = [[x, y] for x, y in zip(s, goal) if x != y]                                                               #Find the mismatch pairs between s and goal.
        if not misMatches:                                                                                                     #If s and goal is same, s should contain at least one duplicated character.
            return any(x > 1 for x in Counter(s).values())
        return len(misMatches) == 2 and misMatches[0][0] == misMatches[1][1] and misMatches[0][1] == misMatches[1][0]          #If s and goal are not same, there must be exactly 2 mismatch paires and they are able to be swapped.
