class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = False
        if x < 0 :
            result = False
        else :
            revers = int(str(x)[::-1])
            if x == revers :
                result = True
            else:
                result = False
        return result
            
                