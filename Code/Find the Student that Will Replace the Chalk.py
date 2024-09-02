class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)                  #Take the modulo by sum of chalk so we don't need to repeative process every student.
        index = 0                        #Initialize index.
        while k >= chalk[index]:         #Traverse while k >= chalk[index].
            k -= chalk[index]            #Substract chalk[index] from k.
            index += 1                   #Move forward index.
        return index
