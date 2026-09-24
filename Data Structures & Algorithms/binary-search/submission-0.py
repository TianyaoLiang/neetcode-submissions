class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # 1 2 3 4 5 6 7
        while left <= right:
            mid = (right+left) // 2

            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid -1
            if target > nums[mid]:
                left = mid + 1
        return -1