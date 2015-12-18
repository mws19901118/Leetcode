class Solution(object):
    def backtracking(self, p, dict, result):
        k = dict.keys()                                     #Get the list of characters.
        if len(k) == 0:                                     #If there are no characters, append the concatenation of current string and its reverse to the result list.
            result.append(p + p[::-1])
        elif len(k) == 1 and dict[k[0]] == 1:               #If there is only 1 character and it appears only once now, append the concatenation of current string, that character and the reverse of current string to the result list.
            result.append(p + k[0] + p[::-1])
        else:                                               #Otherwise, we haven't reach the end condition of backtracing.
            for x in k:
                if dict[x] >= 2:                            #For each character appears more than or equal to twice, decrease its appearance times by 2.
                    dict[x] -= 2
                    if dict[x] == 0:                        #If the appearance times reaches 0, remove it from dict.
                        dict.pop(x, None)
                    self.backtracking(p + x, dict, result)  #Append is to the current string and keep backtracking.
                    if x not in dict:                       #After backtracking, restore the number of appearance.
                        dict[x] = 2
                    else:
                        dict[x] += 2
    
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict = {}
        for x in s:                                         #Count the number of appearance of each character.
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        count = 0
        for x in dict.keys():
            if dict[x] % 2 == 1:                            #Rule out the no palindromic string.
                count += 1
        if count > 1:
            return []
        p = ""
        result = []
        self.backtracking(p, dict, result)                  #Find every palindrome by backtracking.
        return result
