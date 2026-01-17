class Solution:
    def permute(self, nums):
        result = []
        n = len(nums)
        
        def backtrack(path, used):
            if len(path) == n:
                result.append(path[:])  # Found a permutation
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()         # Backtrack
                    used[i] = False
        
        backtrack([], [False]*n)
        return result

# Example usage (for local testing)
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))
