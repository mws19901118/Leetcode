class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        if l3!=l1+l2:                                             #If the sum of length of s1 and length of s2 is not equal to that of s3, return false.
            return False
        i=0
        current=[(-1,-1)]                                         #Record current valid tuple of indexes of s1 and s2, initially (-1,-1).
        while i<=l3:
            if current==[]:                                       #If current is empty, it means s3 can not be formed by the interleaving of s1 and s2, then return false.
                return False
            else:
                next=[]                                           #Record next iteration of list.
                for t in current:
                    if t[0]+1<l1 and s1[t[0]+1]==s3[i]:           #If s3[i] equals s1[t[0]+1] and next doesn't contain (t[0]+1,t[1]), append it to next.
                        if (t[0]+1,t[1]) not in next:
                            next.append((t[0]+1,t[1]))
                    if t[1]+1<l2 and s2[t[1]+1]==s3[i]:           #If s3[i] equals s2[t[1]+1] and next doesn't contain (t[0],t[1]+1), append it to next.
                        if (t[0],t[1]+1) not in next:
                            next.append((t[0],t[1]+1))
                current=next                                      #Replace current with next.
                i=i+1
        return True
