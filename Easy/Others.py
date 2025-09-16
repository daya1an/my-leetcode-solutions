#  Number of 1 Bits
def hammingWeight(self, n: int) -> int:      
    sbin = bin(n)[2:]
    
    #my solution - 0ms
    # count = 0
    # for s in sbin:
    #     if s == '1':
    #         count+=1
    # return count
    
    #better solution
    return sbin.count('1')

#   Hamming Distance

def hammingDistance(self, x: int, y: int) -> int:
    xbin = bin(x)
    xbin = format(x & 0xFFFFFFFF, '032b')
    
    ybin = bin(y)
    ybin = format(y & 0xFFFFFFFF, '032b')
    
    count = 0
    for i in range(len(xbin)):
        if xbin[i] != ybin[i]:
            count+=1
    
    return count

#   Reverse Bits

def reverseBits(self, n: int) -> int:
        
    # my solution - 37ms
    
    # bn = format(n & 0xFFFFFFFF, '032b')
    # bn = bn[::-1]
    # res = int(bn)
    # return int(str(res),2)
    
    # best solution - 0ms 
    return int(f'{n:032b}'[::-1], 2)