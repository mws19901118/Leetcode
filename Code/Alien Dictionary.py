class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        matrix = [[0 for i in range(26)] for j in range(26)]            #This is adjacent matrix.
        indegree = {}                                                   #Record the indegree of each character.
        alphabet = set()                                                #Record the set of characters
        for i in range(len(words)):
            flag = False
            for j in range(len(words[i])):
                alphabet.add(words[i][j])                               #Add character to alphabet.
                                                                        #The first different between current word and next word will generate a topological order of 2 characters.
                if flag == False and i < len(words) - 1 and j < len(words[i + 1]) and words[i][j] != words[i + 1][j]:
                    matrix[ord(words[i][j]) - ord('a')][ord(words[i + 1][j]) - ord('a')] = 1
                    flag = True
                    
        for i in alphabet:                                              #Calculate the indegree of each character.
            count = 0
            for j in range(26):
                if matrix[j][ord(i) - ord('a')] == 1:
                    count += 1
            indegree[i] = count
        result = []
        while len(alphabet) != 0:                                       #Topological sort.
            c = '0'
            for i in alphabet:                                          #Find the character with 0 indgree.
                if indegree[i] == 0:
                    c = i
                    break
            if c == '0':                                                #If can not find, there are cycles, thus no order is valid.
                return ""
            for j in range(26):                                         #Update indgree of the characters which have direct link from character.
               if matrix[ord(c) - ord('a')][j] == 1:
                   indegree[chr(j + ord('a'))] -= 1
            result.append(c)                                            #Append current character to result list.
            alphabet.remove(c)                                          #Remove current character from alphabet.
        return ''.join(result)
