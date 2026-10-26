class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dups = set(nums)
        return len(nums) != len(no_dups)