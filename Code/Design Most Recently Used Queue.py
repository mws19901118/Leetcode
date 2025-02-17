class MRUQueue:

    def __init__(self, n: int):
        self.n = n                                                                #Store n.
        self.bucket_size = floor(sqrt(n))                                         #Set the bucket size to be floor of square root of n; this is used for Square Root Decomposition.
        self.data = []                                                            #Initialize data, which stores data of each bucket.
        self.index = []                                                           #Store the starting index of each bucket.
        for i in range(1, n + 1):                                                 #Traverse from 1 to n.
            bucket_index = (i - 1) // self.bucket_size                            #Calculate the bucket index which i is supposed to belong to.
            if bucket_index == len(self.data):                                    #If bucket_index is the end, append a new empty bucket to data and also append i to index as the starting index of new bucket.
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)                                               #Append i to last bucket.

    def fetch(self, k: int) -> int:
        bucket_index = bisect_right(self.index, k) - 1                            #Binary search for the bucket index which k belongs to.
        element = self.data[bucket_index][k - self.index[bucket_index]]           #Get the element from corresponding bucket with offset from starting index.
        self.data[bucket_index].pop(k - self.index[bucket_index])                 #Delete the element from bucket.
        for i in range(bucket_index + 1, len(self.index)):                        #For all the buckets after current bucket, reduce their starting index by 1.
            self.index[i] -= 1

        if len(self.data[-1]) >= self.bucket_size:                                #If the last bucket is full, create a new empty bucket and also append n to index as the starting index of new bucket.     
            self.data.append([])
            self.index.append(self.n)
        self.data[-1].append(element)                                             #Append element to last bucket.

        if not len(self.data[bucket_index]):                                      #If the previous bucket of the element is empty, pop it from data and index.
            self.data.pop(bucket_index)
            self.index.pop(bucket_index)

        return element                                                            #Return element.
