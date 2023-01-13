class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adjacentList = collections.defaultdict(list)                            #Build adjacent list, since we know the parent-child relation. We treat it as directed graph.
        for i, x in enumerate(parent):
            adjacentList[x].append(i)
        
        def DFS(index: int) -> (int, int):                                      #DFS.
            size, path = 1, 1                                                   #Inititalize the longest path size under this node, and the longest path size ending at current node.
            longest, secondLongest = 0, 0                                       #Inititalize the sizes of longest path and second longest path ending at children of current node that characters not equal current node..
            for x in adjacentList[index]:                                       #Traverse children.
                n_size, n_path = DFS(x)                                         #Get the longest path size under child and the longest path size ending at child.
                size = max(size, n_size)                                        #Update size.
                if s[x] == s[index]:                                            #If child character equals current character, continue.
                    continue
                path = max(path, n_path + 1)                                    #Update path if necessary.
                if n_path > longest:                                            #Update longest and secondLongest if n_path > longest.
                    longest, secondLongest = n_path, longest
                elif n_path > secondLongest:                                    #Otherwise, update secondLongest if n_path > longest.
                    secondLongest = n_path
            return max(size, 1 + longest + secondLongest), path                 #Update size if the path formed by longest, secondLongest and current node is longer than size. Return size and path.

        return DFS(0)[0]                                                        #Return the size from DFS starting from 0.
