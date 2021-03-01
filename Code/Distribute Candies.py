class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)      #Covert list to set to get candy types count then return the min value of candy types count and half of candy amount.
