# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0                                                     #Count characters read.
        buffer = [' ' for i in range(4)]                              #New an empty list of characters to be passed to read4 method.
        while n >= 4:                                                 #While we can read an entire 4 characters, call read4 method.
            c = read4(buffer)
            for i in range(c):                                        #Set correspoding characters to be characters read by read4 method.
                buf[count + i] = buffer[i]
            count += c                                                #Update count.
            if c < 4:                                                 #If reach the end of available characters, break.
                break
            else:
                n -= 4
        if n == 0 or n >= 4:                                          #If we already read enough charaacters or there is no more characters available, return count.
            return count
        else:
            c = min(read4(buffer), n)                                 #Otherwise, read the remaining characters.
            for i in range(c):
                buf[count + i] = buffer[i]
            return count + c                                          #Return count.
