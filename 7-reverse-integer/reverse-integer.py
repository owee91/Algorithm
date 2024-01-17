class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 :
            remove = x * -1
            num_result = str(remove)[::-1]
            if( int(num_result)<((2**31)-1) and int(num_result)>=(-(2**31))):
                return -int(num_result)
            else:
                return 0
        else :
            num_result = str(x)[::-1]
            if( int(num_result)<((2**31)-1) and int(num_result)>=(-2**31)):
                return int(num_result)
            else:
                return 0
        