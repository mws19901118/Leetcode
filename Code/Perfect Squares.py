class Solution:
    def numSquares(self, n: int) -> int:
        q = [n]                                                     #Store numbers in current level.
        s = set()                                                   #Store all the appeared number.
        step = 1                                                    #Initialize steps.
        while q:                                                    #BFS.
            newq = []
            for x in q:
                for i in reversed(range(int(math.sqrt(x)) + 1)):    #Check from the floor of root of x to 1.
                    curr = x - i * i
                    if not curr:                                    #If reach 0, return step.
                        return step
                    if curr not in s:                               #If it's not is s, add it to s and aopend it to newq.
                        newq.append(curr)
                        s.add(curr)
            q = newq                                                #Replace q with newq.
            step += 1                                               #Increase step by 1.
