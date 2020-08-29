from __future__ import division, print_function
import numpy as np
import progressbar

# Import helper functions
from utils import train_test_split, standardize, to_categorical
from utils import mean_squared_error, accuracy_score
from utils.loss_functions import SquareLoss, CrossEntropy, SotfMaxLoss
from decision_tree.decision_tree_model import RegressionTree
from utils.misc import bar_widgets

class GBDT(object):
    """Super class of GradientBoostingClassifier and GradientBoostinRegressor.
    Uses a collection of regression trees that trains on predicting the gradient
    of the loss function.
    Parameters:
    -----------
    n_estimators: int
        树的数量
        The number of classification trees that are used.
    learning_rate: float
        梯度下降的学习率
        The step length that will be taken when following the negative gradient during
        training.
    min_samples_split: int
        每棵子树的节点包含的最小样本数目（小于后不继续切割）
        The minimum number of samples needed to make a split when building a tree.
    min_impurity: float
        每颗子树的最小纯度（小于后不继续切割）
        The minimum impurity required to split the tree further.
    max_depth: int
        每颗子树的最大层数（大于后不继续切割）
        The maximum depth of a tree.
    regression: boolean
        是否为回归问题
        True or false depending on if we're doing regression or classification.


n_estimators:最大弱学习器个数，默认是100，调参时要注意过拟合或欠拟合，一般和learning_rate一起考虑。
learning_rate:步长，即每个弱学习器的权重缩减系数，默认为0.1，取值范围0-1，当取值为1时，相当于权重不缩减。较小的learning_rate相当于更多的迭代次数。
subsample:子采样，默认为1，取值范围(0,1]，当取值为1时，相当于没有采样。小于1时，即进行采样，按比例采样得到的样本去构建弱学习器。这样做可以防止过拟合，但是值不能太低，会造成高方差。

由于GBDT使用CART回归决策树。以下参数用于调优弱学习器，主要都是为了防止过拟合
max_feature：树分裂时考虑的最大特征数，默认为None，也就是考虑所有特征。可以取值有：log2,auto,sqrt
max_depth：CART最大深度，默认为None
min_sample_split：划分节点时需要保留的样本数。当某节点的样本数小于某个值时，就当做叶子节点，不允许再分裂。默认是2
min_sample_leaf：叶子节点最少样本数。如果某个叶子节点数量少于某个值，会同它的兄弟节点一起被剪枝。默认是1
min_weight_fraction_leaf：叶子节点最小的样本权重和。如果小于某个值，会同它的兄弟节点一起被剪枝。一般用于权重变化的样本。默认是0
min_leaf_nodes：最大叶子节点数
'''
    """

    def __init__(self, n_estimators, learning_rate, min_samples_split,
                 min_impurity, max_depth, regression):

        self.n_estimators = n_estimators # 树的数量
        self.learning_rate = learning_rate # 学习率
        self.min_samples_split = min_samples_split # 每颗子树节点分割时候有的最小的样本数
        self.min_impurity = min_impurity
        self.max_depth = max_depth # 每颗子树的最大层次
        self.regression = regression

        # 进度条 processbar
        self.bar = progressbar.ProgressBar(widgets=bar_widgets)

        self.loss = SquareLoss()
        if not self.regression:
            self.loss = SotfMaxLoss()

        # 分类问题也使用回归树，利用残差去学习概率
        self.trees = []
        for i in range(self.n_estimators):
            self.trees.append(RegressionTree(min_samples_split=self.min_samples_split,
                                             min_impurity=self.min_impurity,
                                             max_depth=self.max_depth))

    def fit(self, X, y):
        # 主要思想就是用y和y_pred的梯度做残差rmi,把这个rmi作为'y'值与X进行fit得到一个新的树,新的树再去预测得到p_pred.继续循环
        # 让第一棵树去拟合模型
        self.trees[0].fit(X, y)
        # 预测的结果
        y_pred = self.trees[0].predict(X)
        for i in self.bar(range(1, self.n_estimators)):
        # for循环的过程就是不断让下一棵树拟合上一颗树的"残差"(梯度)
            gradient = self.loss.gradient(y, y_pred)
            # gradient是上一棵树的残差
            self.trees[i].fit(X, gradient)
            # 根据上一棵树的残差去训练新的模型
            y_pred -= np.multiply(self.learning_rate, self.trees[i].predict(X))
    #       预测y=旧y-学习率*根据残差训练模型的得到的最优的残差

    def predict(self, X):
        y_pred = self.trees[0].predict(X)
        for i in range(1, self.n_estimators):
            y_pred -= np.multiply(self.learning_rate, self.trees[i].predict(X))

        if not self.regression:
            # 分类
            # 转化为概率分布 softmax
            y_pred = np.exp(y_pred) / np.expand_dims(np.sum(np.exp(y_pred), axis=1), axis=1)
            # 将标签设置为概率最大的值
            y_pred = np.argmax(y_pred, axis=1)
        return y_pred


class GBDTRegressor(GBDT):
    def __init__(self, n_estimators=200, learning_rate=0.5, min_samples_split=2,
                 min_var_red=1e-7, max_depth=4, debug=False):
        super(GBDTRegressor, self).__init__(n_estimators=n_estimators,
                                            learning_rate=learning_rate,
                                            min_samples_split=min_samples_split,
                                            min_impurity=min_var_red,
                                            max_depth=max_depth,
                                            regression=True)


class GBDTClassifier(GBDT):
    def __init__(self, n_estimators=200, learning_rate=.5, min_samples_split=2,
                 min_info_gain=1e-7, max_depth=2, debug=False):
        super(GBDTClassifier, self).__init__(n_estimators=n_estimators,
                                             learning_rate=learning_rate,
                                             min_samples_split=min_samples_split,
                                             min_impurity=min_info_gain,
                                             max_depth=max_depth,
                                             regression=False)

    def fit(self, X, y):
        y = to_categorical(y)
        super(GBDTClassifier, self).fit(X, y)