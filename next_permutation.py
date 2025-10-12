class Solution:
    def nextPermutation(self, nums):
        # Step 1: find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: if found, find the next greater element and swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse the remaining part
        nums[i + 1:] = reversed(nums[i + 1:])


