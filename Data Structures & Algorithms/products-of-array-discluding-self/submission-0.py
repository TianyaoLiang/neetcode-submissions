class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,3,4]
        results = [1] * len(nums)
        # results = [1,1,1,1]
        #prefix -> results = [1, 1, 2, 6]
        prefix = 1
        for i in range(len(nums)):
            results[i] = prefix
            prefix = prefix * nums[i]
        #postfix -> results = []
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]
        return results