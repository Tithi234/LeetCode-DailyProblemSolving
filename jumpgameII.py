class Solution:
  def jump(self, nums):
    # Edge case: already at last index
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest =0

    # iterate until the second last index
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break

        return jumps


