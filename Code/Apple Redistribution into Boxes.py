class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)        #Sort the capacity in descending order.
        s, index = sum(apple), 0             #Sum up apple and initilaize index to traverse capacity.
        while s > 0:                         #Iterate while s is greater than 0.
            s -= capacity[index]             #Distribute apples to currnet box.
            index += 1                       #Move to next box.
        return index                         #Return index.
