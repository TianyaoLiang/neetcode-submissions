class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_dict = {} # value:index

        for i,v in enumerate(nums):
            need = target - v
            if need in need_dict:
                return [need_dict[need], i]
            if v not in need_dict:
                need_dict[v] = i


            