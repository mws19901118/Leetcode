class Solution(object):
    def BFS(self, i, j, rooms):
        m = len(rooms)
        n = len(rooms[0])
        q = [(i, j)]
        while q != []:                                    #For coordinate in queue, find all the neighbors that are valid and have a larger value than the value of current coordinate.
            newq = []                                     #Set the value of them to be the value of current coordinate plus 1 and append them to new queue.
            for t in q:
                for nbr in [(t[0] + 1, t[1]), (t[0] - 1, t[1]), (t[0], t[1] + 1), (t[0], t[1] - 1)]:
                    if nbr[0] >= 0 and nbr[0]< m and nbr[1] >= 0 and nbr[1] < n and rooms[nbr[0]][nbr[1]] > rooms[t[0]][t[1]] + 1:
                        rooms[nbr[0]][nbr[1]] = rooms[t[0]][t[1]] + 1
                        newq.append(nbr)
            q = newq
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        if n == 0:
            return
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.BFS(i, j, rooms)                   #Start BFS from every gate.
