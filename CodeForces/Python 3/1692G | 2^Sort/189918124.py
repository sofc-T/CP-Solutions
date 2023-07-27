testcases = int(input()) 
 
for _  in range(testcases):
    n,k=map(int,input().split())
 
 
    lists=list(map(int,input().split()))
 
 
    
    result, dos = 0,0
    for i in range(1,n):
        if lists[i]>lists[i-1]/2:
            dos+=1
            if dos>=k:
                #inequalities checkpoints 
                result+=1
        else:
            #We reset back 
            dos=0
    print(result)