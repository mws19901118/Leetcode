class Solution(object):
    def backtracking(self, p):
        if p == []:                                         #If p is empty, there is no valid move, return false.
            return False
        r = False                                           #Store the result.
        dict = {}                                           #Use a dict to rule out all the sequences with same length, because we only have to pick one out of them.
        for j in range(len(p)):
            if p[j] in dict:                                #If we already pick one with the same length, continue.
                continue
            else:                                           #Otherwise, put it in the dict.
                dict[p[j]] = True
            c = p[j]                                        #Record current lenth.
            index = j                                       #Record current index in p.
            del p[j]                                        #Delete it from p.
            for i in range((c - 2) / 2 + 1):                #Flip a consecutive "++" to "--" will break a consecutive "+"s in to 2 parts, enum all the possible situations.
                if i >= 2:                                  #Append the remaining parts to p which are longer than 2.
                    p.append(i)
                if c - 2 - i >= 2:
                    p.append(c - 2 - i)
                t = self.backtracking(p)                    #Backtracking.
                r |= not t                                  #If your opponent can win in next situation, you will lose; vice versa. So for current situation, if you can find a sub-situation where your opponent can't win, you will win at this situation. Otherwise, you will lose.
                if c - 2 - i >= 2:                          #Pop item to restore the list.
                    p.pop()
                if i >= 2:
                    p.pop()
            p.insert(index, c)                              #Insert the length back to its original place.
        return r
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = []                                           #Store all the available length of consecutive "+"s.
        i = 0
        while i < len(s):
            if s[i] == '-':
                i += 1
            else:
                j = i
                while j < len(s) and s[j] == '+':       #Find all the consecutive "+"s and record their length.
                    j += 1
                if j - i >= 2:                          #If the length is not smaller than 2, append it to list p.
                    p.append(j - i)
                i = j
        return self.backtracking(p)
