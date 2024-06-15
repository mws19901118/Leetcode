class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        effectiveHeight = [0] * len(warehouse)                                #Initialize the effective height at each room, which is the max possible box to put here from left and right.
        minHeight = inf                                                       #Initialize the min height from left.
        for i in range(len(warehouse)):                                       #Traverse warehouse from left to right.
            minHeight = min(warehouse[i], minHeight)                          #Update min height.
            effectiveHeight[i] = minHeight                                    #Set effectiveHeight[i] to minHeight.
        minHeight = inf                                                       #Initialize the min height from right.
        for i in reversed(range(len(warehouse))):                             #Traverse warehouse from right to left.
            minHeight = min(warehouse[i], minHeight)                          #Update min height.
            effectiveHeight[i] = max(effectiveHeight[i], minHeight)           #Set effectiveHeight[i] to the max of minHeight and its current value.
        effectiveHeight.sort()                                                #Sort effectiveHeight so it is guaranteed that effective[i] can be reach even if all effective[:i] are filled.
        boxes.sort()                                                          #Sort boxes.
        index = 0                                                             #Initialize an index to traverse boxes so boxes[:index] can all be put in warehouse.
        for x in effectiveHeight:                                             #Traverse effectiveHeight.
            if index < len(boxes) and boxes[index] <= x:                      #If index is valid and boxes[index] can be put here, put it here and move forward index.
                index += 1
        return index                                                          #Return index.
