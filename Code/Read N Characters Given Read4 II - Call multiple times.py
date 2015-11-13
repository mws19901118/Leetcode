# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffer = [None for i in range(4)]                        #Use a global variable to store the buffer result of read4 method.
        self.buffer_size = 0                                          #Use a global variable to store the buffer size.
        self.offset = 0                                               #Use a global variable to store the offset, where we start reading next time.
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        while n > 0 and self.offset < self.buffer_size:               #While n is not 0 and there is still characters in buffer, add them to buf.
            buf[count] = self.buffer[self.offset]
            count += 1
            self.offset += 1
            n -= 1
        while n >= 4:                                                 #Call read4 method as we did in Read N Characters Given Read4.
            c = read4(self.buffer)
            for i in range(c):
                buf[count + i] = self.buffer[i]
            count += c
            if c < 4:
                break
            else:
                n -= 4
        if n == 0 or n >= 4:
            return count
        else:                                                         #Deal the last few characters to read.
            self.buffer_size = read4(self.buffer)                     #Read 4 characters.
            self.offset = 0                                           #Set offset to the beginning.
            while n > 0 and self.offset < self.buffer_size:           #While n is not 0 and there is still characters in buffer, add them to buf.
                buf[count] = self.buffer[self.offset]
                count += 1
                self.offset += 1
                n -= 1
            return count
