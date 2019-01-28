from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = defaultdict(int)                                    #Use default dict to store the count of sub domain.
        for cpd in cpdomains:
            t = cpd.split(" ")                                  #Split counter-paired domain by space, the first string is count while the second is domain.
            count = int(t[0])
            domain = t[1]
            d[domain] += count                                  #Add count of domain in default dict.
            for i, c in enumerate(domain):
                if c == '.':                                    #Iterate through domain, if find '.', then the string behind it is a sub domain. Add count of sub domain in default dict.
                    d[domain[i + 1:]] += count
        return map(lambda x:str(x[1]) + " " + x[0], d.items())  #Covert from default dict to a list of counter-paired domain.
