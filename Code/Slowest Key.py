class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        previousKeyPressedTime, maxDuration = 0, 0                                      #Initialize the time when previous key is pressed and max duration.
        result = None
        for k, t in zip(keysPressed, releaseTimes):                                     #Traverse keyPressed and releaseTimes.
            duration, previousKeyPressedTime = t - previousKeyPressedTime, t            #Compute duration of current key and update previousKeyPressedTime to be current time.
            if duration > maxDuration or (duration == maxDuration  and k > result):     #If duration is greater than maxDuration or duration is equal to maxDuration and k is lexicographically larger than result, update maxDuration and result to duration and k.
                maxDuration = duration
                result = k
        return result                                                                   #Return result.
