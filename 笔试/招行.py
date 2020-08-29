def stick(length,weight,cnt):
    flag = [0 for _ in range(cnt)]
    wood = []
    for i in range(cnt):
        wood.append([length[i], weight[i]])
    wood.sort(key=lambda x: (x[0], x[1]))
    # res=[]
    res = 0
    for i in range(len(wood)):
        if flag[i] == 0:
            res = res + 1
            output = wood[i]
            flag[i] = 1
            j = i + 1
            while j < len(wood):
                if flag[j] == 0:
                    l, w = wood[j]
                    if l >= output[0] and w >= output[1]:
                        output = wood[j]
                        flag[j] = 1
                j = j + 1
    return res
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        cnt = int(input())
        length = list(map(int, input().split()))
        weight = list(map(int, input().split()))
        print(stick(length,weight,cnt))






