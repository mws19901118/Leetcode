class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def convert(log):
            id, logitem = log.split(" ", 1)                             #Split log at the first space. Before the space, it's id; after the space, it's log item.
            return (0, logitem, id) if logitem[0].isalpha() else (1,)   #If the first charactor of log item is letter, return a tuple with 3 elements.
                                                                        #The first element in tuple is a flag, 0, indicating the log is letter log.
                                                                        #The second is the logitem.
                                                                        #The third is id.
                                                                        #Otherwise return a tuple with 2 elements.
                                                                        #The first element in tuple is a flag, 1, indicating the log is letter log.
                                                                        #The second is an empty holder.
        return sorted(logs, key = convert)                              #Sort the logs, after applying convert function on each log to convert log to tuple.
                                                                        #Because the first element in tuple is flag, so letter logs are always before number logs.
                                                                        #Since the second item in tuple of number log is an empty holder, sort won't change the order of number logs("sorted" is guaranteed to be stable).
                                                                        #For letter logs, the sort will base on log items first, then id.
