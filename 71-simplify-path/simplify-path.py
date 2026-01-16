class Solution:
    def simplifyPath(self, path):
        stack = []
        # Split path by '/'
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                # Ignore empty and current directory
                continue
            elif part == '..':
                # Go up one directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(part)

        # Join stack to form canonical path
        return '/' + '/'.join(stack)
