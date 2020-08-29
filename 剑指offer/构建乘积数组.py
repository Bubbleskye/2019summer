A=[0,1,2,3]
B = [1 for _ in range(len(A))]
C = [1 for _ in range(len(A))]
#B[i]的意义是A数组不包括i位置的所有乘积，分为i左边的元素乘积和 i右边的所有元素乘积。
#初始化B[0]=1，是因为0左边没有元素，所以乘积为1。
for i in range(1,len(A)):
    B[i] = B[i-1]*A[i-1]
for i in range(-2,-len(A)-1,-1):
    C[i] = C[i+1]*A[i+1]
#从后往前遍历不算最后一个（num-1）因为第一个for循环中已经计算了
res=[]
for i in range(len(B)):
    res.append(B[i] *C[i])
print(res)