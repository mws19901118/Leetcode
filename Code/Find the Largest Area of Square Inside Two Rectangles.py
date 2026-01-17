class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        rectangles = [(x, y, u, v) for [x, y], [u, v] in zip(bottomLeft, topRight)]              #Put the bottom left coordinate and top right coordinate of each rectangle in one list.
        result = 0
        for i, (x0, y0, u0, v0) in enumerate(rectangles):                                        #Traverse rectangles to get the 2 coordinates of rectangle 0.
            for j in range(i + 1, len(rectangles)):                                              #Traverse the rest of list to get the 2 coordinates of rectangle 1.
                x1, y1, u1, v1 = rectangles[j]
                length = max(0, min(min(u0, u1) - max(x0, x1), min(v0, v1) - max(y0, y1)))       #Calculate the min length(cannot be smaller than 0) of intersection rectangle.
                result = max(result, length ** 2)                                                #Update result if necessary.
        return result
