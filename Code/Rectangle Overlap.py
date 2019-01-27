class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[0] >= rec2[2] or rec1[1] >= rec2[3] or rec1[2] <= rec2[0] or rec1[3] <= rec2[1])

#The answer for whether they don't overlap is LEFT OR RIGHT OR UP OR DOWN, where OR is the logical OR, and LEFT is a boolean that represents whether rec1 is to the left of rec2. The answer for whether they do overlap is the negation of this.
#The condition "rec1 is to the left of rec2" is rec1[2] <= rec2[0], that is the right-most x-coordinate of rec1 is left of the left-most x-coordinate of rec2. The other cases are similar.
