# Logistic 回归 工作原理
# # 每个回归系数初始化为 1
# # 重复 R 次:
# #     计算整个数据集的梯度
# #     使用 步长 x 梯度 更新回归系数的向量
# # 返回回归系数


from __future__ import print_function
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 使用 Logistic 回归在简单数据集上的分类


# 解析数据
def loadDataSet(file_name):
    '''
    Desc:
        加载并解析数据
    Args:
        file_name -- 文件名称，要解析的文件所在磁盘位置
    Returns:
        dataMat -- 原始数据的特征
        labelMat -- 原始数据的标签，也就是每条样本对应的类别
    '''
    # dataMat为原始数据， labelMat为原始数据的标签
    dataMat = []
    labelMat = []
    fr = open(file_name)
    for line in fr.readlines():
        lineArr = line.strip().split()
        if len(lineArr) == 1:
            continue    # 这里如果就一个空的元素，则跳过本次循环
        # 为了方便计算，我们将 X0 的值设为 1.0 ，也就是在每一行的开头添加一个 1.0 作为 X0 ， 相当于w0=1
        dataMat.append([1.0,float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


# sigmoid跳跃函数1/（1+exp(-(w0+w1x1+w2x2+...+wnxn))） x是输入 w是权值
def sigmoid(inX):

    return 1.0 / (1 + exp(-inX))

    # Tanh是Sigmoid的变形，与 sigmoid 不同的是，tanh 是0均值的。因此，实际应用中，tanh 会比 sigmoid 更好。
    # return 2 * 1.0/(1+exp(-2*inX)) - 1


# 正常的处理方案
# 两个参数：第一个参数==> dataMatIn 是一个2维NumPy数组，每列分别代表每个不同的特征，每行则代表每个训练样本。
# 第二个参数==> classLabels 是类别标签，它是一个 1*100 的行向量。为了便于矩阵计算，需要将该行向量转换为列向量，做法是将原向量转置，再将它赋值给labelMat。
def gradAscent(dataMatIn, classLabels):
    '''
    Desc:
        正常的梯度上升法
    Args:
        dataMatIn -- 输入的 数据的特征 List
        classLabels -- 输入的数据的类别标签
    Returns:
        array(weights) -- 得到的最佳回归系数
    参数更新次数：
       迭代次数
    '''

    # 转化为矩阵[[1,1,2],[1,1,2]....]
    dataMatrix = mat(dataMatIn)  # 转换为 NumPy 矩阵
    # 转化为矩阵[[0,1,0,1,0,1.....]]，并转制[[0],[1],[0].....]
    # transpose() 行列转置函数
    # 将行向量转化为列向量   =>  矩阵的转置
    labelMat = mat(classLabels).transpose()  # 首先将数组转换为 NumPy 矩阵，然后再将行向量转置为列向量
    # m->数据量，样本数 n->特征数
    m, n = shape(dataMatrix)
    # print m, n, '__'*10, shape(dataMatrix.transpose()), '__'*100
    # alpha代表向目标移动的步长
    alpha = 0.001
    # 迭代次数
    maxCycles = 500
    # 生成一个长度和特征数相同的矩阵，此处n为3 -> [[1],[1],[1]]
    # weights 代表回归系数， 此处的 ones((n,1)) 创建一个长度和特征数相同的矩阵，其中的数全部都是 1
    weights = ones((n, 1))
    for k in range(maxCycles):  #迭代次数
        # m*3 的矩阵 * 3*1 的单位矩阵 ＝ m*1的矩阵
        # print 'dataMatrix====', dataMatrix
        # print 'weights====', weights
        # n*3   *  3*1  = n*1
        h = sigmoid(dataMatrix * weights)  # 矩阵乘法
        # h是每一个样本通过sigmoid映射之后的值，也就是标记出的label
        # labelMat是实际值
        error = (labelMat - h)  # 向量相减

        # 0.001* (3*m)*(m*1) 表示在每一个列上的一个误差情况，最后得出 x1,x2,xn的系数的偏移量
        weights = weights + alpha * dataMatrix.transpose() * error  # 矩阵乘法，最后得到回归系数
    # ---------------------------------------------------------------------------
    # dataMatrix.transpose() * error即是我们所需要的梯度。
    # 因为f(w)=w(T)*x  根据矩阵求导法则dA(T)*B/dA = B 所以df(w)/dw=dw(T)*x/dw = x 即是输入数据
    return array(weights)


# 随机梯度下降
# 梯度下降优化算法在每次更新数据集时都需要遍历整个数据集，计算复杂都较高
# 随机梯度下降一次只用一个样本点来更新回归系数
def stocGradAscent0(dataMatrix, classLabels):
    '''
    Desc:
        随机梯度下降，只使用一个样本点来更新回归系数
    Args:
        dataMatrix -- 输入数据的数据特征（除去最后一列）
        classLabels -- 输入数据的类别标签（最后一列数据）
    Returns:
        weights -- 得到的最佳回归系数
    参数更新次数：
       数据集中点数
    '''
    m, n = shape(dataMatrix)
    alpha = 0.01
    # n*1的矩阵
    # 函数ones创建一个全1的数组
    weights = ones((n, 1))  # 初始化长度为n的数组，元素全部为 1
    for i in range(m):
        # 选用一个数据来进行参数更新
        # sum(dataMatrix[i]*weights)为了求 f(x)的值， f(x)=a1*x1+b2*x2+..+nn*xn,此处求出的 h 是一个具体的数值，而不是一个矩阵
        h=sigmoid(mat(dataMatrix[i]) * weights)[0,0]
        # h = sigmoid(sum(dataMatrix[i] * weights))
        # print 'dataMatrix[i]===', dataMatrix[i]
        # 计算真实类别与预测类别之间的差值，然后按照该差值调整回归系数
        error = classLabels[i] - h
        # 0.01*(1*1)*(1*n)
        # print weights, "*" * 10, dataMatrix[i], "*" * 10, error
        weights = weights + alpha * mat(dataMatrix[i]).transpose() * error
        weights=np.array(weights)
    return weights


# 随机梯度下降算法（随机化）
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    '''
    Desc:
        改进版的随机梯度下降，使用随机的一个样本来更新回归系数
    Args:
        dataMatrix -- 输入数据的数据特征（除去最后一列数据）
        classLabels -- 输入数据的类别标签（最后一列数据）
        numIter=150 --  迭代次数
    Returns:
        weights -- 得到的最佳回归系数
    参数更新次数：
       numIter*数据集中点数
    '''
    m, n = shape(dataMatrix)
    weights = ones((n, 1))  # 创建与列数相同的矩阵的系数矩阵，所有的元素都是1
    # 随机梯度, 循环150,观察是否收敛
    for j in range(numIter):
        # [0, 1, 2 .. m-1]
        dataIndex = list(range(m))
        for i in range(m):
            # i和j的不断增大，导致alpha的值不断减少，但是不为0
            alpha = 4 / (1.0 + j + i) + 0.0001  # alpha 会随着迭代不断减小，但永远不会减小到0，因为后边还有一个常数项0.0001
            # 随机产生一个 0～len()之间的一个值
            # random.uniform(x, y) 方法将随机生成下一个实数，它在[x,y]范围内,x是这个范围内的最小值，y是这个范围内的最大值。
            randIndex = int(random.uniform(0, len(dataIndex)))
            # sum(dataMatrix[i]*weights)为了求 f(x)的值， f(x)=a1*x1+b2*x2+..+nn*xn
            h = sigmoid(mat(dataMatrix[dataIndex[randIndex]]) * weights)[0, 0]
            # h = sigmoid(sum(dataMatrix[dataIndex[randIndex]] * weights))
            error = classLabels[dataIndex[randIndex]] - h
            # print weights, '__h=%s' % h, '__'*20, alpha, '__'*20, error, '__'*20, dataMatrix[randIndex]
            weights = weights + alpha * mat(dataMatrix[dataIndex[randIndex]]).transpose() * error
            weights = np.array(weights)
            # 随机选取一个样本但不重复，选过的样本序号被删去
            del (dataIndex[randIndex])
    return weights


# 可视化展示
def plotBestFit(dataArr, labelMat, weights):
    '''
        Desc:
            将我们得到的数据可视化展示出来
        Args:
            dataArr:样本数据的特征
            labelMat:样本数据的类别标签，即目标变量
            weights:回归系数
        Returns:
            None
    '''

    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    """
    y的由来，卧槽，是不是没看懂？
    首先理论上是这个样子的。
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
    w0*x0+w1*x1+w2*x2=f(x)
    x0最开始就设置为1叻， x2就是我们画图的y值，而f(x)被我们磨合误差给算到w0,w1,w2身上去了
    所以： w0+w1*x+w2*y=0 => y = (-w0-w1*x)/w2   
    """
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def simpleTest():
    # 1.收集并准备数据
    dataMat, labelMat = loadDataSet("TestSet.txt")

    # print dataMat, '---\n', labelMat
    # 2.训练模型，  f(x)=a1*x1+b2*x2+..+nn*xn中 (a1,b2, .., nn).T的矩阵值
    # 因为数组没有是复制n份， array的乘法就是乘法
    dataArr = array(dataMat)
    # print dataArr
    # weights = gradAscent(dataArr, labelMat)
    # weights = stocGradAscent0(dataArr, labelMat)
    weights = stocGradAscent1(dataArr, labelMat)
    # print '*'*30, weights

    # 数据可视化
    plotBestFit(dataArr, labelMat, weights)



if __name__ == "__main__":
    simpleTest()
    # multiTest()


