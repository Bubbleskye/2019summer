def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    win = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] < win[0]:
            win[0] = nums[i]
        elif nums[i] > win[0] and nums[i] < win[-1]:
            win[-1] = nums[i]
        elif nums[i] > win[-1]:
            win.append(nums[i])
        else:
            pass
        if len(win) == 3:
            return True
    return False

# 用win保存最小值和次小值
# 更新win的规则：比最小值小，即替换最小值
# 此时不用考虑顺序，因为后面有比次小值大的时候，加入win，满足三个，此时可以想成用的是更新前的最小值，这三个数是满足顺序的
# 比次小值大，即加入win，满足三个
# 在次小值和最小值之间，此时更新次小值，这时候更新前的次小值就没有用了，因为要满足顺序。
nums=[0,0,0,0,10,0,0,0,1000]
print(increasingTriplet(nums))