class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()                                                                                                   #Store local name and domain name tuple in a set.
        for e in emails:                                                                                            #Traverse emails.
            atIndex = e.index('@')                                                                                  #Find the index of '@'.
            localName, domainName = e[:atIndex].replace('.', '').split('+')[0], e[atIndex + 1:]                     #Local name is the substring before '@' then remove all '.' and ignore substring after '+'; domain name is the substring after '@'.
            s.add((localName, domainName))                                                                          #Add tuple to s.
        return len(s)                                                                                               #Return length of s.
