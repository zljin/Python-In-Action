'''
两数之和
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []


if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter target number: "))
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target} are: {result}")