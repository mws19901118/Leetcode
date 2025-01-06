class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operations, ball_count = sum(int(x) * i for i, x in enumerate(boxes)), boxes.count('1')      #Calculate the total operations needed to move all balls to first box, also count the balls.
        prefix_count = int(boxes[0])                                                                 #Count balls in visited box.
        result = [operations]                                                                        #Initialize result with operations.
        for x in boxes[1:]:                                                                          #Traverse boxes[1:].
            operations += prefix_count * 2 - ball_count                                              #For each ball in visited box, it needs one more operation to move to current box; for each ball in unvisited box, it needs one less operation to move to current box. 
            prefix_count += int(x)                                                                   #Update prefix count.
            result.append(operations)                                                                #Append operations to result.
        return result
