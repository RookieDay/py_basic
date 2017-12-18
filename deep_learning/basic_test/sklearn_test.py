#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/18
# @Author  : RookieDay
# @Site    : 
# @File    : sklearn_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import numpy as np
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegressionCV

np.random.seed(0)
# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons
# 生成200个点  shuffle默认为true 代表打乱顺序 noise 代表高斯白噪声的标准差加入数据
# make_moons(n_samples=100, shuffle=True, noise=None, random_state=None)
# 如下 生成的数据 X.shape (200,2) y.shape(200,)
X,y = make_moons(200,noise=0.2)
# 绘制散点图
plt.scatter(X[:,0],X[:,1],s = 40, c = y,cmap=plt.cm.Spectral)
plt.show()

def plot_decision_boundary(model,X,y):
    # Set min and max values and give it some padding
    # 设置最大 最小值 并且加一些边缘值填充
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01

    # Generate a grid of points with distance h between them
    # 生成网格点 h 为间距
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)


clf = LogisticRegressionCV()
clf.fit(X,y)
# 画一下决策边界
plot_decision_boundary(lambda x: clf.predict(x),X,y)
plt.title("Logistic Regression")
plt.show()