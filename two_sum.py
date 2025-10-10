class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  # step 1: create a dictionary to store numbers we've already seen

        for i, num in enumerate(nums):  # step 2: loop through nums with index
            complement = target - num  # step 3: find what number we need to reach target


            if complement in seen:      # step 4: if we already saw that complement
                return [seen[complement], i]  # step 5: return indices

            seen[num] = i  # step 6: store thhe number with its index for later lookup
