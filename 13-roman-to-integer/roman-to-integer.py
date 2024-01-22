class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        object = {
            'I' : 1,
            'V' : 5,
            'X' :10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        for x in s :
            output +=object[x]

        if 'IV' in s :
            output -= 2
        if 'IX' in s:
            output -= 2
        if 'XL' in s:
            output -= 20
        if 'XC' in s:
            output -= 20
        if 'CD' in s:
            output -= 200
        if 'CM' in s:
            output -= 200
        
        return output