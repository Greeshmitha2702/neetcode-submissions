class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hm = {}
        for val in nums:
            hm[val] = hm.get(val,0) + 1
        sortedDict = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        c = 0
        for val in sortedDict:
            c += 1
            if c > k:
                break
            res.append(val)
        return res