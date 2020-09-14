# 归并排序同时进行逆序个数统计
class Solution:
    def __init__(self):
        self.cnt=0
    def reversePairs(self, nums):
        def merge(left,right):
            res=[]
            i=0
            j=0
            while i < len(left) and j < len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i=i+1
                else:
                    self.cnt=self.cnt+len(left)-i
                    # 逆序数算的是 left[i]及其之后的所有对right[j]
                    res.append(right[j])
                    j=j+1
            if i<len(left):
                res=res+left[i:]
            #     前面已经计算过这一部分的逆序数
            if j<len(right):
                res=res+right[j:]
            return res

        def mergesort(nums):
            if len(nums)<=1:
                return nums
            elif len(nums)==2:
                return merge([nums[0]],[nums[1]])
            else:
                left=0
                right=len(nums)-1
                mid=left+(right-left)//2
                L=mergesort(nums[:mid])
                R=mergesort(nums[mid:])
                return merge(L,R)

        mergesort(nums)
        return self.cnt