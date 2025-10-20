class Solution:
    def permteUnique(self, nums):
        res = []
        nums.sort()         # Step 1: sort to group duplicates
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # Step 2: skip used numbers
                if used[i]:
                    continue

                # Step 3: skip duplicates (if same as previous and previous not used)
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path)

                # Un-Choose (backtrack)
                path.pop()
                used[i] = False

        backtrack([])
        return res


