 
n = int(input())
def medium():
    rray = input()
    array =list(map(int  , rray.split()))
    array =sorted(array)
    return array[1]
while n:
    print(medium())
    n -= 1