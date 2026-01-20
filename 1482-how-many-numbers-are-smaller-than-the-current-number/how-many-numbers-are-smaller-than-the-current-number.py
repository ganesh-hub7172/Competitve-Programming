class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # Count the occurrences of each number
        count = [0] * 101  # Since 0 <= nums[i] <= 100
        for num in nums:
            count[num] += 1
        
        # Compute how many numbers are smaller than the current number
        for i in range(1, 101):
            count[i] += count[i - 1]
        
        # Build the answer
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1])
        
        return result
