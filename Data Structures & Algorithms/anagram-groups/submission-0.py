class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        res = []
        hm =  {}
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            if key not in hm:
                hm[key] = []
            hm[key].append(word)
        for word in hm.values():
            res.append(word)
        return res
