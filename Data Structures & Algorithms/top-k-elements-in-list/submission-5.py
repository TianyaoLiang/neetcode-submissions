class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {} # num:count
        result = []
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        for _ in range(k):
            max_key = max(num_dict, key=num_dict.get)
            result.append(max_key)
            num_dict.pop(max_key)
        return result