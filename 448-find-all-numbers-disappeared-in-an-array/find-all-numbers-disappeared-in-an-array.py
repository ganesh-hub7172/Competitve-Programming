class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        
        # Mark numbers as negative at their corresponding indices
        for num in nums:
            index = abs(num) - 1  # Convert value to index
            nums[index] = -abs(nums[index])
        
        # Collect indices which are still positive → missing numbers
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)  # Convert index back to value
        
        return result
