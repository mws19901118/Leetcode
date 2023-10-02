class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0                                                                #Count moves Alice have more than Bob.
        i = 0
        while i < len(colors):                                                   #Traverse colors with 2 pointers.
            j = i
            while j < len(colors) and colors[j] == colors[i]:
                j += 1
            count += max(j - i - 2, 0) * (1 if colors[i] == 'A' else -1)         #If there are more than 2 consecutive letters, there are moves. If it is 'A', then add moves to count; otherwise, decrease moves from count.
            i = j
        return count > 0    
