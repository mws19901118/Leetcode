class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [x for x in str(num)]                      #Convert num to string and split.
        digitIndexes = defaultdict(list)               #Store the indexes of each digit in reverse order.
        for i in reversed(range(len(s))):
            digitIndexes[s[i]].append(i)
        for i in range(len(s)):                        #Traverse s.
            maxDigit = max(digitIndexes.keys())        #Find current max digit.
            if s[i] == maxDigit:                       #If s[i] is max digit, pop its index from digitIndexes[s[i]].
                digitIndexes[s[i]].pop()
                if not digitIndexes[s[i]]:             #If this is the last index of s[i], pop s[i] from digitIndexes.
                    digitIndexes.pop(s[i])
                continue
            index = digitIndexes[maxDigit][0]          #Find the last index of maxDigit.
            s[i], s[index] = s[index], s[i]            #Swap it with i.
            break                                      #Stop as we can only make 1 swap at most.
        return int("".join(s))                         #Join s and convert to int and return.
