class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):            #If s and goal don't have same length, return false.
            return False
        return (s + s).find(goal) != -1    #Double s, and if goal is a rotate string, it will be part of doubled s.
