class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, current, total):
            # Base cases
            if total == target:
                res.append(list(current))
                return
            if total > target:
                return

            # Explore further
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # not i+1 because we can reuse the same element
                current.pop()  # backtrack

        backtrack(0, [], 0)
        return res
