class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for x in nums:
            c = 0
            temp = x

            # count trailing 1s
            while temp & 1:
                c += 1
                temp >>= 1

            if c == 0:
                ans.append(-1)
            else:
                ans.append(x - (1 << (c - 1)))

        return ans
