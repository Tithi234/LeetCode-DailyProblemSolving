class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Place numbers in their correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first index where value != index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all positions are correct, return n + 1
        return n + 1


