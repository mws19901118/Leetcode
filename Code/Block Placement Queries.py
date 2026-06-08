class SegmentTree:                                                                              #The segment tree class.
    def __init__(self, n: int):
        self.n = 1 << n.bit_length()                                                            #Round up to the nearest power of 2.
        self.tree = [0] * (self.n * 2)                                                          #Initialize the tree with 2 * n nodes. Node 0 is unused, node 1 is the root. Then for every parent node at index i, 2 * i is the index of left child and 2 * i + 1 is the index of right child.

    def update(self, index: int, val: int):                                                     #Update the value at the given leaf index.
        index += self.n                                                                         #Convert leaf index to the actual node index in tree.
        self.tree[index] = val                                                                  #Update the value an index.
        while index > 1:                                                                        #Surface the change to root.
            index //= 2                                                                         #Move to the parent of current node.
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])              #Update the max value at parent to be the greater of both children.

    def query(self, index: int) -> int:                                                         #Query the max gap from the leftmost leaf index(0) to the given leaf index.
        index += self.n                                                                         #Convert leaf index to the actual node index in tree.
        result = self.tree[index]                                                               #Initialize the result to be the value on the node index.
        while index > 1:                                                                        #Go from the leaf node to the root node to get overall result.
            if index % 2 == 1:                                                                  #If current node is right child of its parent, also take the left child into consideration because the left child segment is within the range.
                result = max(result, self.tree[index - 1])
            index //= 2                                                                         #Move to the parent of current node.
        return result

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        sl = SortedList()                                                                       #Store obstacles distances in a sorted list.
        st = SegmentTree(max(q[1] for q in queries))                                            #Initialize the segment tree with the max distance in queries; each distance is a leaf node.
        result = []
        sl.add(0)                                                                               #Add distance 0 to the sorted list.
        st.update(0, 0)                                                                         #Set distance 0 to 0 in segment tree.
        for q in queries:                                                                       #Traverse queries.
            if q[0] == 1:                                                                       #Process the type 1 query.
                index = sl.bisect_right(q[1])                                                   #Binary search the obstacle to insert the queried distance in the sorted list.
                if index < len(sl):                                                             #If index is not the end, get sl[index], which is the distance of next obstacle.
                    next = sl[index]
                    st.update(next, next - q[1])                                                #Update the value at distance next, as next - q[1] is a new gap.
                st.update(q[1], q[1] - sl[index - 1])                                           #Update the value at distance q[1]. as q[1] - sl[index - 1] is a new gap.
                sl.add(q[1])                                                                    #Add q[1] to the sorted list.
            else:                                                                               #Process the type 2 query.
                prev = sl[sl.bisect_right(q[1]) - 1]                                            #Binary search the prev obstacle in the sorted list. 
                maxGap = max(q[1] - prev, st.query(prev))                                       #The max gap is the max gap from 0 to prev and from prev to q[1].
                result.append(q[2] <= maxGap)                                                   #Append if q[2] is not greater than the max gap.
        return result
