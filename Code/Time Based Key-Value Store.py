class TimeMap:

    def __init__(self):
        self.values = defaultdict(lambda: [(0, "")])                        #Use default dict to store time based values for each key. Each list has a default value represents key timestamp not found, cause 0 is smaller than all timestamp and "" is expected result when not found.

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))                         #Add (timestamp, value) to the values for key.

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_right(self.values[key], (timestamp, "~"))            #Find the right most index to insert (timestamp, "~") in the values for key("~" is lexicographically greater than all letters and digits).
        return self.values[key][index - 1][1]                               #Return the value at index - 1 of the values for key.


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
