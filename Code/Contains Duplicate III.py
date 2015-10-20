class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k<1 or t<0:
            return False
        od=collections.OrderedDict()
        for i in nums:
            key=i if not t else i/t                                           #If t equals 0, the key is the value of element; else, the key is the quotient of value divided by t.
            for m in (od.get(key-1), od.get(key), od.get(key+1)):
                if m is not None and abs(i-m)<=t:                             #If there is a number in the neighbor of current value in ordered dict and their distance are not greater than t, return true.
                    return True
                    
            if len(od)==k:                                                    #Maintain a window of size k.
                od.popitem(False)                                             #Pop item from the ordered dict as a queue.
            od[key]=i                                                         #Add the value to the ordered dict.
            
        return False
