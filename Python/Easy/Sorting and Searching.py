#  First Bad Version
def firstBadVersion(self, n: int) -> int:
    vrs = []
    
    if n == 0:
        return 0
    
    if n == 1:
        if isBadVersion(1):
            return 1
        else:
            return 0
    if isBadVersion(n):
        if not isBadVersion(n-1):
            return n
    
    
    #[1T,2T,3T,4F,5F]
    #[1T,2F,3F,4F,5F,6F]
    
    s = 1
    e = n
    
    while s <= e:
        m = (s+e)//2
        # print(s,e,m)
        
        if isBadVersion(m) and not isBadVersion(m-1):
            return m
        elif isBadVersion(m):
            e = m
        else:
            s = m

#  Merge Sorted Array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = sorted(nums1[:m] + nums2[:n])
