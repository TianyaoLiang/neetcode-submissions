class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # value : index

        for i,v in enumerate(nums):
            need = target - v
            if need in dict:
                return [dict[need],i]
            if v not in dict:
                dict[v] = i