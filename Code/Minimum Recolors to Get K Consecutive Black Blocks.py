class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result, count = len(blocks), 0                #Initialize result to the length of blocks and the count of black blocks in last k blocks.
        for i, x in enumerate(blocks):                #Traverse blocks.
            count += int(x == 'B')                    #Update count.
            if i >= k:
                count -= int(blocks[i - k] == 'B')
            result = min(result, k - count)           #Calculate recolors for current k blocks unding at i and update result if necessary.
        return result
