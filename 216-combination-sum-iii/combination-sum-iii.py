class Solution:
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, path, remaining_sum, remaining_count):
            if remaining_sum == 0 and remaining_count == 0:
                result.append(path[:])
                return

            if remaining_sum < 0 or remaining_count < 0:
                return

            for num in range(start, 10):
                backtrack(
                    num + 1,
                    path + [num],
                    remaining_sum - num,
                    remaining_count - 1
                )

        backtrack(1, [], n, k)
        return result
