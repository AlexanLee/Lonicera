#!/usr/bin/python
# coding=utf-8
__author__ = "lijianli"
import numpy as np


class LR(object):
    @staticmethod
    def fn(w, x):
        """决策函数为sigmoid函数
        """
        print("predict w:", w, "x:", x)
        print("w*x:", -w.dot(x))
        print(1.0 / (1.0 + np.exp(-w.dot(x))))
        return 1.0 / (1.0 + np.exp(-w.dot(x)))

    @staticmethod
    def loss(y, y_hat):
        """交叉熵损失函数
        """
        return np.sum(np.nan_to_num(-y * np.log(y_hat) - (1 - y) * np.log(1 - y_hat)))

    @staticmethod
    def grad(y, y_hat, x):
        """交叉熵损失函数对权重w的一阶导数
        """
        return (y_hat - y) * x


class FTRL(object):
    def __init__(self, dim, l1, l2, alpha, beta, decisionFunc=LR):
        self.dim = dim
        self.decisionFunc = decisionFunc
        self.z = np.zeros(dim)
        self.n = np.zeros(dim)
        self.w = np.zeros(dim)
        self.l1 = l1
        self.l2 = l2
        self.alpha = alpha
        self.beta = beta

    def predict(self, x):
        return self.decisionFunc.fn(self.w, x)

    def update(self, x, y):
        print 'update========================================'
        print 'x:', x, "y:", y
        print 'self.z:', self.z, ' self.l1:', self.l1, ' self.l2:', self.l2, ' self.alpha:', self.alpha, ' self.bata:', self.beta
        self.w = np.array([0 if np.abs(self.z[i]) <= self.l1 else (np.sign(
                self.z[i]) * self.l1 - self.z[i]) / (self.l2 + (
            self.beta + np.sqrt(self.n[i])) / self.alpha) for i in xrange(self.dim)])
        print 'self.w:', self.w
        y_hat = self.predict(x)
        print 'y_hat:', y_hat, ' y:', y, ' x:', x, ' (y_hat-y)*x'
        g = self.decisionFunc.grad(y, y_hat, x)
        print 'self.n:', self.n
        print 'grad:', g
        sigma = (np.sqrt(self.n + g * g) - np.sqrt(self.n)) / self.alpha
        self.z += g - sigma * self.w
        self.n += g * g
        return self.decisionFunc.loss(y, y_hat)

    def train(self, trainSet, verbos=False, max_itr=100000000, eta=0.01, epochs=100):
        itr = 0
        n = 0
        while True:
            for x, y in trainSet:
                loss = self.update(x, y)
                if verbos:
                    print "itr=" + str(n) + "\tloss=" + str(loss)
                if loss < eta:
                    itr += 1
                else:
                    itr = 0
                if itr >= epochs:  # 损失函数已连续epochs次迭代小于eta
                    print "loss have less than", eta, " continuously for ", itr, "iterations"
                    return
                n += 1
                if n >= max_itr:
                    print "reach max iteration", max_itr
                    return


class Corpus(object):
    def __init__(self, file, d):
        self.d = d
        self.file = file

    def __iter__(self):
        with open(self.file, 'r') as f_in:
            for line in f_in:
                arr = line.strip().split()
                if len(arr) >= (self.d + 1):
                    yield (np.array([float(x) for x in arr[0:self.d]]), float(arr[self.d]))


if __name__ == '__main__':
    d = 4
    corpus = Corpus("train.txt", d)
    test = Corpus("test.txt", d)
    ftrl = FTRL(dim=d, l1=1.0, l2=1.0, alpha=0.1, beta=1.0)
    ftrl.train(corpus, verbos=True, max_itr=20, eta=0.01, epochs=3)
    w = ftrl.w
    print w

    correct = 0
    wrong = 0
    print 'test=============================='
    for x, y in test:
        print 'raw data:', x, y
        y_hat = 1.0 if ftrl.predict(x) > 0.5 else 0.0
        if y == y_hat:
            correct += 1
        else:
            wrong += 1
    print "correct ratio", 1.0 * correct / (correct + wrong)
