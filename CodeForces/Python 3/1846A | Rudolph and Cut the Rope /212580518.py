n = int(input())
for i in range(n):
    num = int(input())
    store = []
    for i in range(num):
        store.append(list(map(int, input().split())))
    counter = 0
    for i,j in store:
        if i > j:
            counter += 1
    print(counter)