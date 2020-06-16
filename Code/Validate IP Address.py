import re
class Solution:
    def validateIPv4(self, IP: str) -> str:
        pattern = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"       #Use regex to validate IPv4 address.
        result = re.match(pattern, IP)
        if result:
            return "IPv4"
        else:
            return "Neither"
    
    def validateIPv6(self, IP: str) -> str:
        groups = IP.split(':')                                                                                                      #Split IP to groups by ':'.
        if len(groups) != 8:                                                                                                        #If there aren't 8 groups, it's not IPv6 address.
            return "Neither"
        for g in groups:
            if len(g) == 0 or len(g) > 4:                                                                                           #For each group, if it's length is not between 1 and 4, it's not IPv6 address.
                return "Neither"
            for x in g:
                if x not in "0123456789abcdefABCDEF":                                                                               #If any character is not a hexadecimal digit(either upper case or lower case), it's not IPv6 address.
                    return "Neither"
        return "IPv6"
    
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:                                                                                                               #If '.' is in IP, validate if it's IPv4 address.
            return self.validateIPv4(IP) 
        elif ":" in IP:                                                                                                             #If ':' is in IP, validate if it's IPv6 address.
            return self.validateIPv6(IP)
        else:                                                                                                                       #Otherwise, it's neither.
            return "Neither"
