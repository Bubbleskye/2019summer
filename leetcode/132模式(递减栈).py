def find132pattern(nums):
    if len(nums) < 3:
        return False
    stack = []
    # 字典 存储对应到第i个位置为止的最小值
    X = {}
    X[0] = nums[0]
    # 找到最小值
    for i in range(1, len(nums)):
        X[i] = min(X[i - 1], nums[i])
    # 寻找次大值 依次以nums[j]为最大值
    # stack中存的是nums[j]后面位置的数，即次大值的候选值，次大值在小于nums[j]的前提下，尽可能的大
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] > X[j]:
            while stack and stack[-1] <= X[j]:
                # 次大值小于最小值，将这个值pop出
                # 最小值一定是非递增的，对于j来说小于X[j]的值，也一定会小于X[j-1]，所以pop出没有问题
                stack.pop()
            # 最终stack中留下比最小值大的值
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
    #         stack是一个递减栈，从底到顶递减，如果栈顶元素不符合小于最大值，后面的值也都不符合

    return False


nums= [1,4,3,2,1,1]
print(find132pattern(nums))