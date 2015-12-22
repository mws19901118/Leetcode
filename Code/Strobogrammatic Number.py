class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {'0':'0','1':'1','6':'9','8':'8','9':'6'}                #Use a dict to store strobogrammatic relation.
        for i in range(len(num) / 2):
            if num[i] not in dict or num[-(i + 1)] not in dict or num[-(i + 1)] != dict[num[i]]:
                return False                                            #All the charactors should be in the dict and num[i] should be strobogrammatic with num[-(i + 1)].
        if len(num) % 2 == 1 and num[len(num) / 2] != '0' and num[len(num) / 2] != '1' and num[len(num) / 2] != '8':
            return False                                                #If the length is odd, the middle charactor should be 0, 1 or 8.
        return True
