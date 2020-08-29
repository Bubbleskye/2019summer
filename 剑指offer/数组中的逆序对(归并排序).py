class Solution:
    def __init__(self):
        self.cnt=0
    def reversePairs(self, nums):
        def merge(left,right):
            # 合并
            res=[]
            i=0
            j=0
            while i < len(left) and j < len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i=i+1                 
                else:
                    self.cnt=self.cnt+len(left)-i
                    res.append(right[j])
                    j=j+1
            if i<len(left):
                res=res+left[i:]
            if j<len(right):
                res=res+right[j:]
            return res

        def mergesort(nums):
            # 归并排序
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