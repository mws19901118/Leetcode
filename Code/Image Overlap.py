class Solution:
    def check(self, img1Int: List[int], img2Int: List[int]) -> int:                                                                     #Given 2 n * n image(in the form of list of integer), calculate the overlap.
        return sum((x & y).bit_count() for x, y in zip(img1Int, img2Int))                                                               #Traverse 2 lists simultaneously, count the bit of 1 in x & y.

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1Int = [reduce(lambda a, b: a << 1 | b, x) for x in img1]                                                                    #Treat each row in img1 as binary and convert it to an integer.
        img2Int = [reduce(lambda a, b: a << 1 | b, x) for x in img2]                                                                    #Treat each row in img2 as binary and convert it to an integer.
        mask = (1 << len(img1Int)) - 1                                                                                                  #Calculate the bit mask so the integer remain m bit after shifting left.
        overlap = 0                                                                                                                     #Intialize overlap.
        for i in range(len(img1Int)):                                                                                                   #Try not shfiting and shifting left and right m - 1 times respectively.
            shiftRight = [x >> i for x in img1Int]                                                                                      #Shift right each integer.
            for j in range(1, len(img1Int) + 1):                                                                                        #Try not moving and moving up and down m - 1 times respectively.
                overlap = max(overlap, self.check(shiftRight[:j], img2Int[-j:]), self.check(shiftRight[-j:], img2Int[:j]))              #Calculate current overlap and update final result if necessary.

            shiftLeft = [(x << i) & mask for x in img1Int]                                                                              #Shift left each integer.
            for j in range(1, len(img1Int) + 1):                                                                                        #Try not moving and moving up and down m - 1 times respectively.
                overlap = max(overlap, self.check(shiftLeft[:j], img2Int[-j:]), self.check(shiftLeft[-j:], img2Int[:j]))                #Calculate current overlap and update final result if necessary.
        return overlap                                                                                                                  #Return final result.
