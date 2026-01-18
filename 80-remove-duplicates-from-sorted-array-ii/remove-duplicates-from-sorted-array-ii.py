class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        write = 2  # index to place the next valid element

        for i in range(2, len(nums)):
            # Allow nums[i] if it is different from nums[write - 2]
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1

        return write
