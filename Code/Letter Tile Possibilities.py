class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)                                                                #Count each tile.
        keys = list(count.keys())                                                             #Get the unique tiles in a list.
        @cache                                                                                #Cache result.
        def backtracking(index: int, total: int, numerator: int, denominator: int) -> int:    #Backtracking with current index in keys, total tiles taken and numerator and denominator for multinomial coefficient.
            if index == len(keys):                                                            #If index reaches the end, return numerator // denominator.
                return numerator // denominator
            result = 0                                                                        #Initialize result.
            for i in range(count[keys[index]] + 1):                                           #Traverse from 0 to count[keys[index]].
                result += backtracking(index + 1, total, numerator, denominator)              #Use i of current tiles and add the result of recursively backtracking to result.
                total += 1                                                                    #Increase total.
                numerator *= total                                                            #Update numerator.
                denominator *= (i + 1)                                                        #Update denominator.
            return result                                                                     #Return result.
        
        return backtracking(0, 0, 1, 1) - 1                                                   #Return the backtracking from index 0 and 0 tiles with initial numerator and denominator both at 1, then decrease by 1 to remove the empty tiles.
