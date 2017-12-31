# _*_coding:utf-8_*_

from statsmodels.tsa.stattools import adfuller as ADF

import numpy as np

ADF(np.random.rand(200))
