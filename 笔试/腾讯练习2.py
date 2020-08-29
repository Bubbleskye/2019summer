# 有n个数，两两组成二元组，相差最小的有多少对呢？相差最大呢？
# 输入例子1:
# 6
# 45 12 45 32 5 6
# 输出例子1:
# 1 2
def smallbig(nums):
    nums.sort()
    b = nums.count(nums[-1])
    s = nums.count(nums[0])
    big=b*s
    resdict={}
    flag=0
    for i in range(len(nums)-1):
        tmp=nums[i+1]-nums[i]
        if tmp==0:
            flag=1
            break
        if tmp not in resdict:
            resdict[tmp]=1
        else:
            resdict[tmp]=resdict[tmp]+1
    if flag==0:
        res=resdict.keys()
        return resdict[min(res)],big
    else:
        zero={}
        for i in range(len(nums)):
            if nums[i] not in zero:
                zero[nums[i]]=1
            else:
                zero[nums[i]] = zero[nums[i]]+1
        count=0
        for key,value in zero.items():
            if value!=1:
                count=count+value*(value-1)/2
        return int(count),big

# 一组数据中第一行表示个数
# 第二行是一个列表
# 的读入方式
if __name__ == "__main__":
    import sys
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        line = sys.stdin.readline().split()
        nums = [int(i) for i in line]
        count=len(nums)
        if count==0 or count==1:
            print(0,0)
        if count==2:
            print(1,1)
        else:
            s,b=smallbig(nums)
            print(s,b)
