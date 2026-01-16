import re

class Solution:
    def isNumber(self, s):
        s = s.strip()  # remove leading/trailing spaces
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return re.match(pattern, s) is not None
