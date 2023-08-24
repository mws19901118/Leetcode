class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []                                                                        #Initialize result.
        i  = 0
        while i < len(words):                                                              #Traverse words with 2 pointers.
            j = i
            length = 0                                                                     #Initialize sum of words length on current line.
            while j < len(words) and length + j - i + len(words[j]) <= maxWidth:           #While words[j] can be added to current line with minimum white spaces, add words[j] to current line.
                length += len(words[j])
                j += 1
            if j == len(words):                                                            #If j reaches the end of words, it is the last line.
                line = " ".join(words[i:])                                                 #Join words[i:] by white space.
                result.append(line + " " * (maxWidth - len(line)))                         #Add extra white spaces at the end to make it maxWidth then append line to result.
            elif j == i + 1:                                                               #If current line only has one word, add extra white spaces after words[i] to make it maxWidth then append line to result.
                result.append(words[i] + " " * (maxWidth - len(words[i])))
            else:
                gap, cou t = divmod(maxWidth - length, j - i - 1)                          #Calulate the min length of gap and how many gaps will have one extra white space to distribute white spaces as evenly as possible.
                line = ""
                for k in range(i, j - 1):                                                  #Traverse words[i:j - 1].
                    line += words[k]                                                       #Append words[k] to line.
                    line += " " * (gap + (1 if k < i + count else 0))                      #Append needed white spaces(at least gap, and for the first count slots, add one more extra white space).
                result.append(line + words[j - 1])                                         #Append words[j - 1] then append line to result.
            i = j
        return result
