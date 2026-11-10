class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        max_count = 1
        count = 1
        for i in range(len(sorted_nums)-1):
            # [1,2,3,4,5]
            if (sorted_nums[i+1] - sorted_nums[i]) == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count
