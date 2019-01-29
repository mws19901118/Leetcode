from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)                                                #Use default dict to store value and timestamp for key.

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp, value))                                    #Append a tuple of timestamp and value to the list for given key.

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.map[key]
        if len(values) == 0:                                                        #If key not in map, return empty string.
            return ""
        start = 0
        end = len(values) - 1
        while start + 1 <= end :                                                    #Binary search. To avoid index out of bound, use start + 1 <= end.
            mid = (start + end) / 2
            if values[mid][0] <= timestamp and values[mid + 1][0] > timestamp:      #If current timestamp is the latest timestamp before given timestamp, return value.
                return values[mid][1]
            elif values[mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid + 1
        if end < 0:                                                                 #If end < 0, it means binary search comes to the start without found, return empty string.
            return ""
        if values[-1][0] > timestamp:                                               #Otherwise, it means means binary search comes to the end without found.
            return ""                                                               #If the last timestamp is bigger than given timestamp, it means the special case that values list only has one element.
        else:                                                                       #Return the last value.
            return values[-1][1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
