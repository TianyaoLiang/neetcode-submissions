class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in set_nums:
                return [set_nums[diff], i]
            set_nums[n] = i


            