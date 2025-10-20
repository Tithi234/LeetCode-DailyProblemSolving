class Solution:
    def permute(self, nums):
        res = []
        path = []

        def backtrack(remaining):
            # Base case: if no elements left to permute
            if not remaining:
                res.append(path[:]) #Add a copy of current path
                return

            # Try each number in the remaining list
            for i in range(len(remaining)):
                # Choose
                path.append(remaining[i])
                # Explore
                backtrack(remaining[:i] + remaining[i+1:])
                # Un-choose (backtrack)
                path.pop()

        backtrack(nums)
