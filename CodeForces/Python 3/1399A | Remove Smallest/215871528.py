t = int(input())
for i in range(t):
    def xoo():
        n = int(input())
        nums = list(map(int,input().split()))
        nums.sort()
        i = 1
        while i < n:
            if nums[i-1] == nums[i] or nums[i] == nums[i-1] + 1:
                i += 1
            else:
                return "NO"
        return "YES"
    print(xoo())
        
            
            