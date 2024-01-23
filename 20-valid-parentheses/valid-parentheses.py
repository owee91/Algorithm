class Solution:
    def isValid(self, s: str) -> bool:
        output = False

        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')

        if len(s) == 0:
            output = True
        else:
            output = False
        return output