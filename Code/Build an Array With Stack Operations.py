class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        latest, index = 1, 0              #Initialize latest number and current index at target.
        result = []
        while index < len(target):        #Iterate while not all target are built.
            result.append("Push")         #Push latest number to stack.
            if latest < target[index]:    #If latest number is not in target, pop it.
                result.append("Pop")
            else:                         #Otherwise move to next number in target.
                index += 1
            latest += 1                   #Move to next number.
        return result
