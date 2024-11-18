class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)                                                      #Initialize result to be all 0.
        if k > 0:                                                                     #If k > 0, calculate result[0] to be sum of code[1:k + 1].
            result[0] = sum(code[1:k + 1])
            for i in range(1, len(code)):                                             #Traverse forward to the end, and update result[i], which is adding code[(i + k) % len(code)] and substracting code[i] from result[i - 1].
                result[i] = result[i - 1] + code[(i + k) % len(code)] - code[i]
        elif k < 0:                                                                   #If k < 0, calculate result[-1] to be sum of code[k - 1:-1].
            result[-1] = sum(code[k - 1:-1])
            for i in reversed(range(len(code) - 1)):                                  #Traverse backward to the start, and update result[i], which is adding code[(i + k) % len(code)] and substracting code[i] from result[i - 1].
                result[i] = result[i + 1] + code[(i + k) % len(code)] - code[i]
        return result
