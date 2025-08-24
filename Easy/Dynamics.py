#   Climbing Stairs
def climbStairs(self, n: int) -> int:
    r=[0,1]
    for i in range(2,n+2):
        r.append(r[-1]+r[-2])

    return r[-1]

#   Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
    pft = 0
    low = max(prices)+1
    
    for p in prices:
        pft = max(pft, p-low)
        low = min(low,p)
        
    return pft

#  Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
    
    maxSum = nums[0]
    curSum = nums[0]
    
    for i in range(1,len(nums)):
        curSum = max(nums[i], curSum + nums[i])
        maxSum = max(maxSum, curSum)

    return maxSum


#  House Robber
def rob(self, nums: List[int]) -> int:
    
    cur = pre = bef = 0
    
    for n in nums:
        bef = pre
        pre = cur
        cur = max(pre,n+bef) 

    return cur