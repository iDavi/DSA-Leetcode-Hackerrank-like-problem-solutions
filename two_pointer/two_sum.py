#unsorted array:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_find = {}
        for i, val in enumerate(nums):
            if val in to_find:
                return [to_find[val], i]
            to_find[target-val] = i