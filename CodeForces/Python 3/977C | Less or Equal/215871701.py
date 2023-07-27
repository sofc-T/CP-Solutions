def xoo():
    n , k =  map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    if n == k:
        return nums[-1]
    elif k == 0:
        if nums[0] == 1:
            return -1
        else:
            return nums[0] - 1
    
    if nums[k-1] == nums[k]:
        return -1
    else:
        return nums[k-1]
print(xoo())