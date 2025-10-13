class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]:
        :type target: int
        :rtype: List[int]
        """
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # keep going left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
