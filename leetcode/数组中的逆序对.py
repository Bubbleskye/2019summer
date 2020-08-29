class Solution:
    # 归并排序同时进行逆序个数统计
    def reversePairs(self, nums):
        if len(nums)<=1:
            return 0
        res,count=self.reversecnts(nums)
        return count
    def reversecnts(self, nums):
        if len(nums)==1:
            return nums,0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return [nums[1]]+[nums[0]],1
            else:
                return nums,0
        count=0
        left=0
        right=len(nums)-1
        mid=left+(right-left)//2
        nums1,cnt1=self.reversecnts(nums[0:mid+1])
        nums2,cnt2=self.reversecnts(nums[mid+1:])
        count=count+cnt1+cnt2
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                count=count+(mid-i+1)
                j=j+1
            else:
                i=i+1
        return sorted(nums1+nums2),count
nums= [1,2,1,2,1]
solution=Solution()
count=solution.reversePairs(nums)
print(count)