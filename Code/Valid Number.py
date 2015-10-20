class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)                        #Try to convert s to a float number, if success, return true; else, return false.
            return True
        except Exception, e:
            return False
