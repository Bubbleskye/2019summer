# 查并集解决的是两个顶点是否连通的问题
# 首先遍历所有的等式，构造并查集。同一个等式中的两个变量属于同一个连通分量，因此将两个变量进行合并。
# 然后遍历所有的不等式。同一个不等式中的两个变量不能属于同一个连通分量
# 因此对两个变量分别查找其所在的连通分量，如果两个变量在同一个连通分量中，则产生矛盾，返回 false。
# 如果遍历完所有的不等式没有发现矛盾，则返回 true。
#

def equationsPossible(equations):
    abcs = [0 for _ in range(26)]
    tmp=1
    for equation in equations:
        if equation[1] == '=':
            first = ord(equation[0]) - ord('a')
            end = ord(equation[3]) - ord('a')
            if abcs[first]==0 and abcs[end]==0:
                #都没有出现过
                abcs[first]=tmp
                abcs[end]=tmp
                tmp=tmp+1
            elif abcs[first]==0 or abcs[end]==0:
                value=max(abcs[first], abcs[end])
                abcs[first] = value
                abcs[end]=value
            else:
                value=max(abcs[first], abcs[end])
                key1=abcs[first]
                key2=abcs[end]
                for i in range(len(abcs)):
                    # 将之前于first和end连接的一并都改成新的值
                    if abcs[i]==key1 or abcs[i]==key2:
                        abcs[i]=value

    for equation in equations:
        if equation[1] == '!':
            first = ord(equation[0]) - ord('a')
            end = ord(equation[3]) - ord('a')
            if first==end:
                return False
            if abcs[first]!=0 and abcs[end]!=0 and abcs[first]==abcs[end]:
                return False
    return True

equations=["a==z","a==b","b==c","c==d","b==y","c==x","d==w","g==h","h==i","i==j","a==g","j!=y"]
print(equationsPossible(equations))