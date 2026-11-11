class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first have each element with its count
        res = []
        count_n = {}
        for n in nums:
            count_n[n] = count_n.get(n, 0) + 1

        sorted_count = dict(sorted(count_n.items(), key=lambda item: item[1], reverse=True))


        for key, values in sorted_count.items():
            if len(res) < k:
                res.append(key)
        return res