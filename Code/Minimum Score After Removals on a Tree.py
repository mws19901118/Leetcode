class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        adjacentList = defaultdict(list)                                                                #Build adjacent list.
        for x, y in edges:
            adjacentList[x].append(y)
            adjacentList[y].append(x)

        total_xor = reduce(lambda x, y: x ^ y, nums)                                                    #Calculate the total XOR result.
        result = inf                                                                                    #Initialize result to be large.

        def calculate_score(xor1: int, xor2: int, xor3: int) -> int:                                    #Given the xor of 3 components, calculate score.
            return max(xor1, xor2, xor3) - min(xor1, xor2, xor3)

        def dfs_first_edge(curr: int, prev: int) -> int:                                                #DFS to remove the first edge and return the XOR result of current subtree rooting at node curr.
            xor = nums[curr]                                                                            #Initialize xor with root value.
            for x in adjacentList[curr]:                                                                #Traverse the neighbors of curr and skip its parent prev.
                if x == prev:
                    continue
                xor ^= dfs_first_edge(x, curr)                                                          #Keep dfs to remove the first edge in current subtree and update XOR result with the XOR result of subtree rooting at node x.
            if prev != -1:
                dfs_second_edge(prev, curr, xor, curr)                                                  #DFS to delete each edge as the second edge outside of current subtree(reverse direction of current DFS); also pass curr as the anchor to indicate that the edge between curr and prev is already removed.
            return xor                                                                                  #Return xor as the XOR result of current subtree.

        def dfs_second_edge(curr: int, prev: int, parent_xor: int, anchor: int) -> int:
            xor = nums[curr]                                                                            #Initialize xor with root value.
            for x in adjacentList[curr]:                                                                #Traverse the neighbors of curr and skip its parent prev.
                if x == prev:
                    continue
                xor ^= dfs_second_edge(x, curr, parent_xor, anchor)                                     #Keep dfs to remove the second edge in current subtree and update XOR result with the XOR result of subtree rooting at node x.
            if prev != anchor:                                                                          #If prev is anchor, cannot remove the edge between curr and prev because it is already removed as the first edge.
                nonlocal result
                result = min(result, calculate_score(parent_xor, xor, total_xor ^ parent_xor ^ xor))    #Update result if necessary: component 1 XOR is passed from parent(parent_xor); component 2 XOR is current subtree XOR(xor); component 3 XOR can be calculated from total_xor ^ parent_xor ^ xor.
            return xor

        dfs_first_edge(0, -1)                                                                           #Start dfs_first_edge at node 0 with no prev node.
        return result
