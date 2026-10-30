class Solution:
    def twoSum(self, nums: List[3,4,5,6], target: 7) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]
            
            seen[num] = index
        
        return []  