class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        result = False
        for num in nums:
            if num in unique:
                result = True
            else:
                unique.add(num)
        return result