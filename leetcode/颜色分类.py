# 荷兰国旗问题
# 三个指针，把0往前放，2最后放，1不管
nums=[2,0,2,1,1,0]
left=0
right=len(nums)-1
curr=0
while curr<=right:
    # 右指针与当前指针比较
    if nums[curr]==2:
        nums[curr],nums[right]=nums[right],nums[curr]
        right=right-1
    elif nums[curr]==0:
        nums[curr], nums[left] = nums[left], nums[curr]
        curr=curr+1
        left=left+1
    else:
        curr=curr+1
print(nums)

