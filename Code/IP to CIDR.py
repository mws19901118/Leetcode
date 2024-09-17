class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def intToCIDR(x: int, length: int) -> str:                                                #Convert ip in int to CIDR string with given length.
            chunks = [0, 0, 0, 0]
            for i in range(4):                                                                    #Calculate the 4 chunks of ip.
                chunks[i], x = divmod(x, 1 << 8 * (3 - i))
            return ".".join([str(x) for x in chunks]) + "/" + str(length)                         #Convert each chunk to string and join by "," then add "/" and length as string.

        ipInt = sum(int(x) * 1 << 8 * (3 - i) for i, x in enumerate(ip.split(".")))               #Convert ip string to int.
        masks = {i: 1 << (32 - i) for i in range(33)}                                             #Create bit mask for each length of CIDR from 0 to 32 inclusive.
        limit = ipInt + n                                                                         #Calculate the limit of ips.
        result = []
        while ipInt < limit:                                                                      #Iterate while ipInt is smaller than limit.
            i = 0
            while i <= 32 and ipInt & (masks[i] - 1) != 0:                                        #Find if current ip can be the start of CIDR at any length(from longer to shorter).
                i += 1                                                                            #Basically for CIDR length x, check if the last 32 - i bits are all 0.
            coverage = masks[i]                                                                   #For the CIDR length x, it can cover 1 << (32 - i) number of ip.
            while ipInt + coverage - 1 >= limit:                                                  #While the whole coverage reaches ip limit, shrink the length and coverage until not reaching ip limit.
                coverage >>= 1
                i += 1
            result.append(intToCIDR(ipInt, i))                                                    #Covert current ip to CIDR with length i and add CIDR to result.
            ipInt += coverage                                                                     #Move ipInt forward to the first ip that cannot cover by this CIDR.
        return result
