class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        result=[]
        if words==[] or L==0:                                             #Deal with this special situation.
            result.append("")
            return result
        length=len(words)
        i=0
        j=0
        while i+j<length:
            clength=0                                                     #Record the length of current line.
            cline=[]                                                      #Record the current line.
            while i+j<length and clength+len(words[i+j])<=L:
                cline.append(words[i+j])                                  #Traverse forward to add suitable words for current line and update clength.
                clength+=len(words[i+j])+1
                j+=1
            no=len(cline)                                                 #Calculate the number of words in current line.
            clength-=no                                                   #Calculate the number of charactors without spaces.
            str=""
            if i+j==length:                                               #If current line is the last line, add one space between every 2 adjacent words, also add spaces at the end to make up a string whose length is L.
                for k in range(i,length-1):
                    str+=words[k]+" "
                str+=words[-1]
                while len(str)<L:
                    str+=" "
                result.append(str)
            else:
                if no==1:                                                 #If there is only one word in current line, add spaces at the end to make up a string whose length is L.
                    str+=cline[0]
                    for k in range(clength,L):
                        str+=" "
                    result.append(str)
                else:                                                     #If current line is not the last line and contains more than one word, do the followings.
                    a=(L-clength)/(no-1)                                  #Caculate the min spaces between 2 words.
                    b=(L-clength)%(no-1)                                  #The first b intevals should contain a+1 spaces.
                    for k in range(no-1):
                        str+=cline[k]
                        for t in range(a):
                            str+=" "
                        if k<b:
                            str+=" "
                    str+=cline[-1]
                    result.append(str)
            i+=j                                                          #Clear j.
            j=0
        return result
