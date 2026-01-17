class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]  # store the max subarray sum
        current_sum = nums[0]  # max sum ending at current position

        for num in nums[1:]:
            # either start new subarray at num or extend the current subarray
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
