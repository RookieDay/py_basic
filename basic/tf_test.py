#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20
# @Author  : RookieDay
# @Site    : 
# @File    : tf_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition
import tensorflow as tf
input_x = [
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]

]

result = tf.transpose(input_x, perm=[0, 2, 1])
with tf.Session() as sess:
    print(sess.run(result))