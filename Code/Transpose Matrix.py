class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))      #Flatten matrix to each row and traverse each row simultaneously to convert each column to row and then return as a list of list.
