def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    else:
        last = generate(numRows - 1)
        # print(last[numRows-2])
        lastlayer = last[numRows - 2]
        newlayer = [1]
        for i in range(len(lastlayer) - 1):
            newlayer.append(lastlayer[i] + lastlayer[i + 1])
        newlayer.append(1)
        new=last+[newlayer]
        return new

print(generate(5))
