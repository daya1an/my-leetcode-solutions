# 1. https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    ans.append(i)
                    ans.append(j)
                    return ans
