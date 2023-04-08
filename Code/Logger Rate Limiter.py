class Logger:

    def __init__(self):
        self.logs = {}                                                                      #Store logs in a dictionary.

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logs and self.logs[message] + 10 > timestamp:                    #If message is in dictionary and previous timestamp plus 10 is greater than current timestamp, return false.
            return False
        self.logs[message] = timestamp                                                      #Upsert the timestamp for message.
        return True                                                                         #Return true.

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
