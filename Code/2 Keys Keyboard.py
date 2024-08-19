class Solution:
    def minSteps(self, n: int) -> int:
        steps = [inf] * (n + 1)                                #Initialize steps for each number.
        steps[1] = 0                                           #Initially steps[1] = 0.
        @cache                                                 #Cache result, basically only need to run once for each number in clipboard.
        def dfs(clipboard: int) -> None:
            count = steps[clipboard] + 1                       #Initialize count, which is one copy all operations on top of steps[clipboard].
            x = clipboard * 2                                  #Double clipboard to start traverse.
            while x <= n:                                      #Traverse while x <= n.
                steps[x] = min(steps[x], count + 1)            #Update steps[x] if count + 1 is smaller.
                dfs(x)                                         #Continue dfs on x.
                x += clipboard                                 #Add clipboard to x.
                count += 1                                     #Increase count.
        dfs(1)                                                 #Start dfs from 1.
        return steps[-1]                                       #Return steps[-1].
