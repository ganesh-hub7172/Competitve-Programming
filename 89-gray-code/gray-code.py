class Solution:
    def grayCode(self, n):
        length = 1 << n  # 2^n
        result = []
        for i in range(length):
            gray_num = i ^ (i >> 1)
            result.append(gray_num)
        return result
