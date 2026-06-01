class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hm = {}
        for val in nums:
            hm[val] = hm.get(val,0) + 1
        buckets = [[]for _ in range(len(nums) + 1)]
        for val, freq in hm.items():
            buckets[freq].append(val)
        c = 1
        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                if c <= k:
                    res.append(val)
                c += 1
        return res