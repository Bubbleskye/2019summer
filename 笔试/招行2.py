def solve(N,arr):
    arr.sort(reverse=True)
    cnt0=arr.count(0)
    cnt1=arr.count(1)
    if cnt0+cnt1==N:
        return -1
    else:
        return N+1-cnt0
if __name__ == "__main__":
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        res=solve(N,arr)
        print(res)
