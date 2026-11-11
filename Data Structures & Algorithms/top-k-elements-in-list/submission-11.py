class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {} # num:count
        result = []
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1

        temp = [[] for i in range(len(nums)+1)]
        for n,c in num_dict.items():
            temp[c].append(n)

        for i in range(len(temp)-1, 0, -1):
            for num in temp[i]:
                result.append(num)
                if len(result) == k:
                    return result