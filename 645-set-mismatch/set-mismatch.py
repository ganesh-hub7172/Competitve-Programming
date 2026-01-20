class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        seen = set()
        duplicate = missing = -1
        
        # Find the duplicate
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
        
        # Find the missing number
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
        
        return [duplicate, missing]
