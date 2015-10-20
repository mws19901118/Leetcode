class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        def convert(version):                                   #Convert string to a list of integer.
            n=[]
            if version.find('.')==-1:                           #If string doesn't contain '.', convert directly.
                n.append(int(version))
            else:                                               #If it does, split the string first, then convert.
                v=version.split('.')
                for i in v:
                    n.append(int(i))
            return n
        
        def isZero(n):                                          #Determine if a list if integer only contains 0.
            for i in n:
                if i!=0:
                    return False
            return True
        
        n1=convert(version1)
        n2=convert(version2)
        i=0
        while i<len(n1) and i<len(n2):                          #Compare two lists digit by digit.
            if n1[i]>n2[i]:
                return 1
            elif n1[i]<n2[i]:
                return -1
            else:
                i+=1
        if i==len(n1) and i==len(n2):
            return 0
        else:
            if i==len(n1) and i<len(n2):
                if isZero(n2[i:]):                              #If all the extra digits are 0, return 0.
                    return 0
                else:
                    return -1
            elif i==len(n2) and i<len(n1):
                if isZero(n1[i:]):
                    return 0
                else:
                    return 1
