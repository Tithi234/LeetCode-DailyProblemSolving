class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()   # Sort to handle duplicates easily
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(list(path))
                return
            if remaining < 0:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicates (only skip if same as previous on same level)
                if candidates[i] == prev:
                    continue

                # Stop if number exceeds remaining target (since sorted)
                if candidates[i] > remaining:
                    break

                # Choose current number
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

                prev = candidates[i]

        backtrack(0, [], target)
        return res
