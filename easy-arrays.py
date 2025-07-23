# 1. https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array

def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    ans.append(i)
                    ans.append(j)
                    return ans

# 2. https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=array
def searchInsert(self, nums: List[int], target: int) -> int:
        res = len(nums)
        if target in nums:
            res = nums.index(target)
        elif nums[0] >= target:
            res = 0
        else:
            for i in range(1,len(nums)):
                if nums[i-1] < target and nums[i] > target:
                    res = i
                    break
        return res
