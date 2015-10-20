class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        p=path.split('/')                                   #Split the string.
        i=0
        while i<len(p):
            c=p[i]                                          #Record current part of path.
            if c=='' or c=='.':                             #If current part is '' or '.', delete it.
                del p[i]
                i-=1;
            elif c=='..':                                   #If current part is '..', delete it and the part before it(if have).
                del p[i]
                if(i>0):
                    del p[i-1]
                    i-=2;
                else:
                    i-=1;
            i+=1;
        return '/'+ '/'.join(p)                             #Join the remain parts.
