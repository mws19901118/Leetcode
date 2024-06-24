class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        targetCount = Counter(target)                                                                                #Count letters in target.
        counters = [Counter(s) & targetCount for s in stickers]                                                      #Count letters in each sticker and only keep letters in target.

        for i in reversed(range(len(counters))):                                                                     #Dedupe stickers that are fully covered by other stickers.
            if any(counters[i] == counters[i] & counters[j] for j in range(len(counters)) if i != j):
                counters.pop(i)

        result = len(target) + 1                                                                                     #Initialize result to be an impossible value.
        def dfs(stickersUsed: int):                                                                                  #DFS with stickers already used.
            nonlocal result
            if stickersUsed >= result:                                                                               #If stickers already used is greater than result, it is not a candidate, so return.
                return                                            
            if not counters:                                                                                         #If no more counters, we have to stop. If no more uncovered letters in target, update result.
                if all(targetCount[letter] <= 0 for letter in targetCount):
                    result = stickersUsed
                return

            sticker = counters.pop()                                                                                 #Use current sticker.
            newUsed = max(max(ceil(targetCount[letter] / sticker[letter]) for letter in sticker), 0)                 #Calculate the max stickers needed to cover all letters can be covered by current sticker.

            for c in sticker:                                                                                        #Update each coverred letters.
                targetCount[c] -= newUsed * sticker[c]

            dfs(stickersUsed + newUsed)                                                                              #Keep DFS.
            for i in reversed(range(newUsed)):                                                                       #Gradually remove usage of current sticker.
                for letter in sticker:
                    targetCount[letter] += sticker[letter]
                dfs(stickersUsed + i)                                                                                #DFS.

            counters.append(sticker)                                                                                 #Append sticker back.

        dfs(0)                                                                                                       #DFS starting with 0.
        return result if result <= len(target) else -1                                                               #Return result if it is not greater than target; otherwise return -1.
