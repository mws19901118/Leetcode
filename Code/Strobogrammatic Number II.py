class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dict = {'0':'0','1':'1','6':'9','8':'8','9':'6'}                                                  #Use a dict to store strobogrammatic relation.
        if n == 0:                                                                                        #Because there shouldn't be leading zeros, we have to enum all the possible value when n is form 0 to 3.
            return ""
        elif n == 1:
            return ["0","1","8"]
        elif n == 2:
            return ["11", "69", "88", "96"]
        elif n == 3:
            return ["101","111","181","609","619","689","808","818","888","906","916","986"]
        else:
            result = []
            for x in self.findStrobogrammatic(n - 2):                                                     #Recursively find the answer of n - 2.
                for c in dict:
                    if n % 2 == 0:                                                                        #If n is even, add numbers in the middle.
                        result.append(x[:len(x) / 2] + c + dict[c] + x[len(x) / 2:])
                    else:                                                                                 #Otherwise, add numbers on both side of the middle character.
                        result.append(x[:len(x) / 2] + c + x[len(x) / 2] + dict[c] + x[len(x) / 2 + 1:])
            return result
