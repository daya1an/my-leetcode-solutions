nums = [0,0,1,1,1,2,2,3,3,4]

# my solution 
def removeDuplicates1(self, nums: list[int]) -> int:
     expnums = sorted(list(set(nums)))
     print("Array :: " + str(expnums))
     return len(expnums)

# my solution with leet code complaince

def removeDuplicates2(self, nums: List[int]) -> int:
     expnums = list(set(nums))
     expnums.sort()
     for i in range (len(expnums)):
          nums[i] = expnums[i]

     return len(expnums) 

# top leet code solution (0ms)
# 2 pointer algorithm used

def removeDuplicates3(self, nums: List[int]) -> int:
     i = 1
     for j in range(1, len(nums)):
          if nums[j] != nums[i-1]:
               nums[i] = nums[j]
               i += 1
     return i

print(str(nums) + "\n" + "Result = "+ str(removeDuplicates3(0, nums)))
