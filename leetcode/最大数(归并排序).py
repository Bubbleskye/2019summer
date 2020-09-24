# 定义自己的比较大小的方式：根据拼接起来之后的数字的大小来进行排序
# [30,3] 因为303<330 所以3>30 3排在前面
class Solution:
    def merge(self,nums1,nums2):
        i=0
        j=0
        res=[]
        while i < len(nums1) and j < len(nums2):
            if int(str(nums1[i])+str(nums2[j]))>int(str(nums2[j])+str(nums1[i])):
                res.append(nums1[i])
                i=i+1
            else:
                res.append(nums2[j])
                j=j+1
        if i<len(nums1):
            for k in range(i,len(nums1)):
                res.append(nums1[k])
        if j<len(nums2):
            for k in range(j,len(nums2)):
                res.append(nums2[k])
        return res
    def mergesort(self,nums):
        if len(nums)<=1:
            output=nums
        elif len(nums)==2:
            if int(str(nums[0])+str(nums[1]))>int(str(nums[1])+str(nums[0])):
                output=nums
            else:
                output=[nums[1]]+[nums[0]]
        else:
            left=0
            right=len(nums)-1
            mid=left+(right-left)//2
            left=self.mergesort(nums[:mid+1])
            right=self.mergesort(nums[mid+1:])
            output=self.merge(left,right)
        return output
    def largestNumber(self, nums: List[int]) -> str:
        output=self.mergesort(nums)
        out=""
        flag=False
        for o in output:
            out=out+str(o)
            if o!=0:
                flag=True
        if not flag:
            return "0"       
        return out