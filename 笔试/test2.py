T=int(input())
for _ in range(T):
    N,M=map(int, input().split())
    if N%2==0 or M%2==0:
        print("1/2")
    else:
        print(str(int((N*M-1)/2))+"/"+str(int(N*M)))