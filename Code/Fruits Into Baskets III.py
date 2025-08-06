class SegTree:                                                                                        #Segment tree class.
    def __init__(self, baskets):
        size = 1 << (len(baskets) - 1).bit_length() + 1
        self.segments = [0] * size                                                                    #Initialize segments.
        self.build(baskets, 1, 0, len(baskets) - 1)                                                   #Build the segment tree.

    def maintain(self, node: int):                                                                    #Maintain the segment root node has the max value in current segment.
        self.segments[node] = max(self.segments[node * 2], self.segments[node * 2 + 1])

    def build(self, origin: List[int], node: int, left: int, right: int):                             #Build segement tree on origin[left:right + 1] with node as root.
        if left == right:                                                                             #If left == right, current segment only has 1 element, so set self.segments[node] to origin[left] and return.
            self.segments[node] = origin[left]
            return
        mid = (left + right) // 2                                                                     #Calculate mid.
        self.build(origin, node * 2, left, mid)                                                       #Recursively build the left segment tree.
        self.build(origin, node * 2 + 1, mid + 1, right)                                              #Recursively build the right segment tree.
        self.maintain(node)                                                                           #Maintain root node value.

    def find_first_and_update(self, node: int, left: int, right: int, target: int):                   #Find the first node in segment tree that is at least target then remove that node(mark as -1) and return node index.
        if self.segments[node] < target:                                                              #If the value at root is smaller than target, target is for sure not in current segment, so return -1.
            return -1
        if left == right:                                                                             #If left == right, we found a value that is at least target, mark the node as -1 and return node index.
            self.segments[node] = -1
            return left
        mid = (left + right) // 2                                                                     #Calculate mid.
        i = self.find_first_and_update(node * 2, left, mid, target)                                   #Try to find target in left segment tree.
        if i == -1:                                                                                   #If not found, find target in right segment tree.
            i = self.find_first_and_update(node * 2 + 1, mid + 1, right, target)
        self.maintain(node)                                                                           #Maintain root node value.
        return i                                                                                      #Return index.

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegTree(baskets)                                                                       #Build a segment tree on baskets.
        return sum(tree.find_first_and_update(1, 0, len(baskets) - 1, x) == -1 for x in fruits)       #Return the count of fruits that cannot be found in the segment tree.
