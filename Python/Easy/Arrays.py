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
# 3. https://leetcode.com/problems/roman-to-integer/
def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                ans = ans - roman[s[i]]
            else:
                ans = ans + roman[s[i]]
        
        return ans + roman[s[-1]]

# 4. http://leetcode.com/problems/intersection-of-two-arrays-ii/description/ (2 pointer algo)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        op = []
        i = 0
        j = 0
        
        nums1.sort()
        nums2.sort()
        
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                op.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        
        return op

#5. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] +=1
                return digits
            
            digits[i] = 0 
        
        return [1] + digits


# 6.  Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                #Swapping
                nums[i],nums[j]=nums[j],nums[i]
                j+=1

# 7. Majority Element
#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res = 0
        # numsSet = set(nums)
        # for i in numsSet:
        #     if maxCount < nums.count(i):
        #         maxCount = nums.count(i)
        #         res = i
        
        # return 
        
        nums = sorted(nums)
        return nums[int(len(nums)/2)]
