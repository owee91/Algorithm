import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            return bool(re.match(r"^{p}$".format(p=re.sub(r"\*+", "*", p)), s))
        
            