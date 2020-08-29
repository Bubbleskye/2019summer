def Find(target, array):
    # write code here
    if len(array) == 0 or len(array[0])==0:
        return False
    row = len(array)
    col = len(array[0])
    if target == array[0][col - 1]:
        return True
    elif target < array[0][col - 1]:
        return Find(target, [array[i][0:col-1] for i in range(row)])
    else:
        return Find(target, [array[i][0:col] for i in range(1,row)])

array=[]
target=7
print(Find(target, array))