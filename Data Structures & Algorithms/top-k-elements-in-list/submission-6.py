class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {} # num:count
        freq = [[] for i in range(len(nums)+1)] #
        result = []
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        for n,c in num_dict.items():
            freq[c].append(n)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result