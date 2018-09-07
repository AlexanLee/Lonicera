#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()

# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
#
# print("done")
# plt.figure()
# df.plot()
# plt.legend(loc='best')
# plt.show()
#
#

# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

x = range(0, 5)
y1 = [3, 6, 6, 8, 9]
y2 = [2, 5, 5, 7, 8]
y3 = [6, 6, 8, 8, 1]
p1 = plt.scatter(x, y1, marker='x', color='g', label='1', s=30)
p2 = plt.scatter(x, y2, marker='+', color='r', label='2', s=30)
p3 = plt.scatter(x, y3, marker='*', color='c', label='3', s=30)
plt.title('Scatter')
plt.legend(loc='upper right')
plt.xticks(x)
plt.show()
