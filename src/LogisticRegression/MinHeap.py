import heapq
def F(arr):
    heapq.heapify(arr)
    p = 1
    ans  = 0 
    while arr:
        n = heapq.heappop(arr)
        if n >= p:
            ans += n-p
            p+=1
    return ans
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(F(a))
    