# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]                                          #Initialize matrix.
        x, y, u, v = 0, 0, 0, 1                                                                      #Initialize starting cell and direction.
        rightTurn = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}             #Use dictionary to store the direction after right turn.
        while head:                                                                                  #Traverse while head is not none.
            matrix[x][y] = head.val                                                                  #Set the value of current cell to the value of head.
            head = head.next                                                                         #Move head to next.
            if x + u < 0 or x + u >= m or y + v < 0 or y + v >= n or matrix[x + u][y + v] != -1:     #If continue current direction will move out of bound or a visited cell, take a right turn.
                u, v = rightTurn[(u, v)]
            x += u                                                                                   #Move forward.
            y += v
        return matrix
