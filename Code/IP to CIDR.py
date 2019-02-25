class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        result = []
        power = [2 ** 24, 2 ** 16, 2 ** 8, 2 ** 0]                #Record the power of 2 for each IP segment.
        ipSegments = list(map(lambda x:int(x), ip.split(".")))    #Convert IP from string to a list of integers; each integer is a segment of IP, ordering from high to low.
        ipInt = 0
        for i in range(4):                                        #Convert IP to int.
            ipInt += ipSegments[i] * power[i]
        while n > 0:                                              #While there are remaining IPs in range.
            p = 1
            while ipInt % p == 0 and n >= p:                      #Find the largest power of 2 that is not large than remaining IPs and is a divider of current IP integer.
                p *= 2                                            #Such power of 2 can form the largest possible CIDR block.
            p /= 2
            
            t = ipInt                                             #Covert IP integer to CIDR.
            CIDR = ""
            for i in range(4):
                CIDR += str(int(t / power[i]))
                t %= power[i]
                if i != 3:
                    CIDR += "."
                else:
                    CIDR += "/"
            CIDR += str(32 - int(math.log(p, 2)))
            result.append(CIDR)
            
            n -= p                                                #Update IP integer and remaining IPs.
            ipInt += p
        return result
