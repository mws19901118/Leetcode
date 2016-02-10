# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffer = [None for _ in range(4)]                        #Use a global variable to store the buffer result of read4 method.
        self.buffer_size = 0                                          #Use a global variable to store the buffer size.
        self.offset = 0                                               #Use a global variable to store the offset, where we start reading next time.
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0                                                     #Indicates the beginning unfilled index in buf.
        temp = min(n, self.buffersize - self.offset)                  #Find the min value of n and remaining buffer size.
        buf[:temp] = self.buffer[self.offset:self.offset + temp]      #Fill buf with characters in buffer as many as possible.
        index += temp                                                 #Update index.
        self.offset += temp                                           #Update offset.
        if index == n:                                                #If have already read n characters, return index.
            return index
        b = [' ' for i in range(4)]                                   #Construct a list of characters to be read in read4.
        while True:
            t = read4(b)                                              #Call read4 and get the actual number of characters read.
            if index + t <= n:                                        #If number of characters so far don't exceed n, fill buf and update index.
                buf[index:index + t] = b[:t]
                index += t
                if t < 4:                                             #If no characters left to be read, break.
                    break
            else:                                                     #Otherwise, we have unused characters to become new buffer.
                buf[index:] = b[:n - index]                           #Fill buf until it's full.
                self.buffer[:t - (n - index)] = b[n - index:]         #The rest is new buffer.
                self.buffersize = t - (n - index)                     #Update buffersize.
                self.offset = 0                                       #Update offset.
                index = n                                             #Update index
                break                                                 #Break.
        return index                                                  #Return index.
