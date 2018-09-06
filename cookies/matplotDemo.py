# _*_coding:utf-8_*_

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x ** 2) + 1

plt.figure(figsize=(8, 4))
plt.subplot(223)
plt.plot(x, y, label='$\sin x +1$', color='red', linewidth=2)
plt.plot(x, z, 'b--', label='$\cos x^2+1$')

plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Example')
plt.ylim(0, 2.2)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.legend()
plt.show()
