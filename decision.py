#!/usr/bin/python

from scipy import optimize
import numpy as np
import time


class Decision(object):
    def __init__(self, m, n, w, imp, cost, sum_imp, sum_cost):
        self.m = m
        self.n = n
        self.w = w
        self.cost = cost
        self.imp = imp
        self.x = np.ones(m * n)
        self.sum_cost = sum_cost
        self.sum_imp = sum_imp

    def train(self):
        start = time.clock()
        print(self.m, self.n)
        a = np.concatenate((self.imp, self.cost), axis=0)
        b = np.concatenate((self.sum_imp, self.sum_cost), axis=0)
        bounds = [(0, 1)] * self.n * self.m
        a_t = np.zeros((self.m, self.n))
        a_t[:, 0] = 1
        a_e = a_t.reshape(1, self.n * self.m)
        for i in range(1, self.n):
            a_t = np.zeros((self.m, self.n))
            a_t[:, i] = 1
            a_t = a_t.reshape(1, self.n * self.m)
            a_e = np.vstack((a_e, a_t))
        b_e = [1] * self.n
        print(a_e, b_e)
        print(a, b)
        print("w:%s" % self.w)
        print("bounds:%s" % bounds)
        op = optimize.linprog(-self.w, a, b, a_e, b_e, bounds=bounds)
        self.x = op.x
        print("max:%.2f,x_value:%s" % (-op.fun, self.x))
        end = time.clock()
        print("elapse:%f" % (end - start))
        return self.x


def test():
    m = 2
    n = 3
    w = np.ones(m * n) * ([np.random.random()] * 3 * 2)
    cost_1 = np.ones(m * n) * ([np.random.random()] * 3 * 2)
    cost_2 = np.ones(m * n) * ([np.random.random()] * 3 * 2)
    cost = np.concatenate(([cost_1], [cost_2]), axis=0)
    imp_1 = np.ones(m * n) * ([np.random.random()] * 3 * 2)
    imp_2 = np.ones(m * n) * ([np.random.random()] * 3 * 2)
    imp = np.concatenate(([imp_1], [imp_2]), axis=0)
    D = Decision(m=m, n=n, w=w, imp=imp, cost=cost, sum_imp=[100, 20], sum_cost=[20, 10])
    D.train()


class Corpus(object):
    def __init__(self, f, d):
        self.d = d
        self.file = f

    def __iter__(self):
        with open(self.file, 'r') as f_in:
            for line in f_in:
                arr = line.strip().split()
                if len(arr) >= (self.d + 1):
                    yield (np.array([float(x) for x in arr[0:self.d]]), float(arr[self.d]))


if __name__ == '__main__':
    print("main")
    test()
    # m - order
    # n - deal
    # x_1,1+x_2,1+
