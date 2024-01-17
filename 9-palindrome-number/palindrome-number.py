class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = False
        if x < 0 :
            print(x)
            result = False
        else :
            revers = int(str(x)[::-1])
            print(type(x))
            print(type(revers))
            if x == revers :
                result = True
            else:
                result = False
        print(result)
        return result
            
                