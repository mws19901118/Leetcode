class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = set()                         #Use a set to store the tuple of local name and domain name.
        for e in emails:
            splits = e.split("@")             #Split email by '@' to get the local name and domain name.
            local = splits[0]
            domain = splits[1]
            index = local.find("+")           #Find the index of '+' in local name.
            if index != -1:
                local = local[:index]         #Ignore '+' and everything after it in local name.
            local = local.replace(".", "")    #Remove all '.' in local name.
            count.add((local, domain))        #Add the tuple of local name and domain name to set.
        return len(count)                     #Return the unique count of tuples.
            
