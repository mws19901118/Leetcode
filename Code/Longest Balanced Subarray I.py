class SegmentTree:                                                                                  #Segment tree with lazy propogation class.
    def __init__(self, n: int):
        self.n = n
        self.minTree = [0] * (4 * n)
        self.maxTree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def push(self, node: int, start: int, end: int) -> None:                                        #Apply lazy updates from a node to its actual values and propagate to children.
        if not self.lazy[node]:                                                                     #If there is no pending update, directly return.
            return
        self.minTree[node] += self.lazy[node]                                                       #Update self.minTree[node].
        self.maxTree[node] += self.lazy[node]                                                       #Update self.maxTree[node].
        if start != end:                                                                            #If current node is not a leaf node, pass the update to its children.                                 
            self.lazy[2 * node] += self.lazy[node]
            self.lazy[2 * node + 1] += self.lazy[node]
        self.lazy[node] = 0                                                                         #Reset the pending update.

    def updateRange(self, node: int, start: int, end: int, l: int, r: int, sign: int) -> None:      #Add sign to all elements in the segment [l, r].
        self.push(node, start, end)                                                                 #Apply pending changes first.
        if start > end or start > r or end < l:                                                     #If current subtree is none or [l, r] is outside of current subtree, directly return.
            return 
        if l <= start and end <= r:                                                                 #If current subtree is completely within [l, r], apply the update immediately and return.
            self.lazy[node] += sign
            self.push(node, start, end)
            return
        mid = (start + end) // 2
        self.updateRange(2 * node, start, mid, l, r, sign)                                          #Update left child recursively.
        self.updateRange(2 * node + 1, mid + 1, end, l, r, sign)                                    #Update right child recursively.
        self.minTree[node] = min(self.minTree[2 * node], self.minTree[2 * node + 1])                #Update self.minTree[node].
        self.maxTree[node] = max(self.maxTree[2 * node], self.maxTree[2 * node + 1])                #Update self.maxTree[node].

    def findLeftmostZero(self, node: int, start: int, end: int) -> int:                             #Find the leftmost position where the value equals 0.
        self.push(node, start, end)                                                                 #Apply pending changes first.
        if self.minTree[node] > 0 or self.maxTree[node] < 0:                                        #If current subtree can't contain 0, return -1 as not found.
            return -1
        if start == end:                                                                            #If current subtree is a left node, return start if itself is 0 or -1 if not.
            return start if self.minTree[node] == 0 else -1
        mid = (start + end) // 2
        left = self.findLeftmostZero(2 * node, start, mid)                                          #Find in left child first.
        return left if left != -1 else self.findLeftmostZero(2 * node + 1, mid + 1, end)            #If found, then return the result; otherwise, return the result in right child.

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        prev = defaultdict(lambda: -1)                                                              #Store the previous index of each number; initially all -1.
        st = SegmentTree(len(nums))                                                                 #Initialize the segment tree.
        result = 0
        for i, x in enumerate(nums):                                                                #Traverse nums.
            sign = 1 if not x & 1 else -1                                                           #Get the sign of x.
            if prev[x] != -1:                                                                       #If x has occurred before, unset its contribution to the segment tree by add the opposite sign to [0, prev[x]].
                st.updateRange(1, 0, len(nums) - 1, 0, prev[x], -sign)
            st.updateRange(1, 0, len(nums) - 1, 0, i, sign)                                         #Add sign to [0, i].
            prev[x] = i                                                                             #Update prev[x].
            j = st.findLeftmostZero(1, 0, len(nums) - 1)                                            #Find the leftmost index that has value 0, now the segment [j, i] has a net 0 diff between distinct odd and even numbers.
            if j != -1 and j <= i:                                                                  #If found such index j, update result if i - j + 1 is longer.
                result = max(result, i - j + 1)
        return result
