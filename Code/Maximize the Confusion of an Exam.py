class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = 0                                            #Initialize length.
        count = Counter()                                     #Count T and F.
        for i, x in enumerate(answerKey):                     #Traverse answerKeys.
            count[x] += 1                                     #Increase count[x].
            minor = min(count['T'], count['F'])               #Get the minor of count['T'] and count['F'].
            if minor <= k:                                    #If minor is not greater than k, increase length because we change all answers for minor to make all answer consecutive.
                length += 1
            else:                                             #Otherwise, decrease the count of answerKey[i - length] as we have to move it out of window.
                count[answerKey[i - length]] -= 1             #The window now may still be invalid but it doesn't matter since we already found a valid window with same length.

        return length
