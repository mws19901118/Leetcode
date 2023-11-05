class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner, count, index = arr[0], 0, 1        #Initialize current winner, count of winning and index in arr.
        while index < len(arr):                    #Traverse arr.
            if v > arr[index]:                     #If winner is greater than current number, increase count.
                count += 1
            else:                                  #Otherwise, replace winner to current number and reset count to 1.
                winner = arr[index]
                count = 1
            if count == k:                         #If count equals k, break.
                break
            index += 1                             #Move to next number.
        return winner                              #Return winner and don't have to simulate all k comparisions because the number that lost cannot win again.
