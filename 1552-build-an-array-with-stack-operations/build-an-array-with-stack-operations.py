class Solution:
    def buildArray(self, target, n):
        operations = []
        current = 1  # Stream starts from 1
        i = 0        # Pointer in target array

        while i < len(target):
            if current == target[i]:
                operations.append("Push")
                i += 1
            else:
                operations.append("Push")
                operations.append("Pop")
            current += 1

        return operations

