class SegmentTree:                                                                                                                          #The segment tree class.
    def __init__(self, nums: List[int]):
        self.n = 1 << len(nums).bit_length()                                                                                                #Round up to the nearest power of 2.
        self.nodes = [(inf, -inf)] * 2 * self.n                                                                                             #Initialize the tree with 2 * n node, and each node has the min and max value of the segment.
        for i, x in enumerate(nums):                                                                                                        #Since the segment tree is static, populate the leaf nodes min and max value.
            self.nodes[i + self.n] = (x, x)
        for i in reversed(range(1, self.n)):                                                                                                #Populate the parent nodes min and max value in bottom up fashion.
            self.nodes[i] = (min(self.nodes[2 * i][0], self.nodes[2 * i + 1][0]), max(self.nodes[2 * i][1], self.nodes[2 * i + 1][1]))

    def query(self, l: int, r: int) -> int:                                                                                                 #Query the value(max value - min value) of each subarry nums[l:r + 1].
        minV, maxV = inf, -inf                                                                                                              #Initialize the min value and max value,
        l += self.n                                                                                                                         #Move l to its leaf node index.
        r += self.n                                                                                                                         #Move r to its leaf node index.
        while l <= r:                                                                                                                       #Traverse while l <= r.
            if l % 2:                                                                                                                       #If l is right node, the current segment is fully within the subarry, so update min value and max value.
                minV, maxV = min(minV, self.nodes[l][0]), max(maxV, self.nodes[l][1])
                l += 1                                                                                                                      #Move l to next left node in the same level. If it goes out of current level, l must be the end of current level then l <= r would be no longer valid so the loop will stop.
            if not r % 2:                                                                                                                   #If r is left node, the current segment is fully within the subarry, so update min value and max value.
                minV, maxV = min(minV, self.nodes[r][0]), max(maxV, self.nodes[r][1])
                r -= 1                                                                                                                      #Move r to last right node in the same level. If it goes out of current level, r must be the start of current level then l <= r would be no longer valid so the loop will stop.
            l //= 2                                                                                                                         #Move l to its parent node.
            r //= 2                                                                                                                         #Move r to its parent node.
        return maxV - minV                                                                                                                  #Return maxV - minV.

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        sg = SegmentTree(nums)                                                                                                              #Initialize the segment tree.
        heap = [(-sg.query(i, len(nums) - 1), i, len(nums) - 1) for i in range(len(nums))]                                                  #For each index i, put the value of subarray nums[i:] together with the starting and ending indexes to the max heap.
        heapq.heapify(heap)
        result = 0
        while k:                                                                                                                            #Iterate k times.
            x, l, r = heapq.heappop(heap)                                                                                                   #Pop the max heap.
            result -= x                                                                                                                     #Add the value to result.
            if l <= r - 1:                                                                                                                  #If l <= r - 1, push the value of subarray nums[l:r] together with the starting and ending indexes to the max heap, since if l is fixed, the value is non increasing when r moves leftward.
                heapq.heappush(heap, (-sg.query(l, r - 1), l, r - 1))
            k -= 1
        return result
