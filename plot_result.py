import matplotlib.pylab as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
#
# # 绘制车辆间距的变换
# x1 = [17, 19, 21, 23, 25,  29, 33,  37,39,41,43]
# y1 = [90.77, 93.65, 95.83, 97.38, 98.14, 98.66,98.94 ,99.05,99.14,99.21,99.26]
# x2 = [17, 19, 21, 23, 25,  29, 33,  37,39,41,43]
# y2 = [84.31, 88.35, 91.52,93.68, 95.2, 96.98,  98.14, 98.90, 98.99, 99.06, 99.11]
# x3 = [17, 19, 21, 23, 25,  29, 33,  37,39,41,43]
# y3 = [75.81,83.47, 87.67,90.75, 92.77, 95.24,96.97, 97.9, 97.99, 98.07, 98.12]
#
# plt.plot(x1,y1)
# plt.plot(x2,y2)
# plt.plot(x3,y3)
#
# plt.scatter(x1,y1)
# plt.scatter(x2,y2)
# plt.scatter(x3,y3)
#
# # pyl.title("")
# plt.xlabel('distance', fontsize = 12)
# plt.ylabel('success rate', fontsize=12)
#
# # x_major_locator = MultipleLocator(1)
# # # 把x轴的刻度间隔设置为1，并存在变量里
# # y_major_locator = MultipleLocator(2)
# # # 把y轴的刻度间隔设置为10，并存在变量里
# # ax = plt.gca()
# # # ax为两条坐标轴的实例
# # ax.xaxis.set_major_locator(x_major_locator)
# # # 把x轴的主刻度设置为1的倍数
# # ax.yaxis.set_major_locator(y_major_locator)
# # # 把y轴的主刻度设置为10的倍数
# #
# # plt.xlim(16, 44)
# # # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
# # plt.ylim(75, 100)
# # 把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
# plt.xticks(np.arange(16, 44, 1),fontproperties = 'Times New Roman', size = 8)
# plt.yticks(np.arange(75, 100, 2),fontproperties = 'Times New Roman', size = 10)



# 绘制车辆间距的变换
x1 = [8,  12, 14, 16]
y1 = [98.96, 98.14, 92.53, 89.9]
x2 = [8, 12, 14, 16]
y2 = [98.2, 95.2, 89.51, 92.7]
x3 = [8, 12, 14, 16]
y3 = [98.7, 92.77, 85.77, 79.9]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
#
# plt.scatter(x1,y1)
# plt.scatter(x2,y2)
# plt.scatter(x3,y3)

# pyl.title("")
plt.xlabel("speed", fontsize = 12)
plt.ylabel("success rate", fontsize=12)

# x_major_locator = MultipleLocator(1)
# # 把x轴的刻度间隔设置为1，并存在变量里
# y_major_locator = MultipleLocator(1)
# # 把y轴的刻度间隔设置为10，并存在变量里
# ax = plt.gca()
# # ax为两条坐标轴的实例
# ax.xaxis.set_major_locator(x_major_locator)
# # 把x轴的主刻度设置为1的倍数
# ax.yaxis.set_major_locator(y_major_locator)
# # 把y轴的主刻度设置为10的倍数
#
# plt.xlim(7, 17)
# # 把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
# plt.ylim(78, 100)
# # 把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白

plt.xticks(np.arange(7, 17, 1),fontproperties = 'Times New Roman', size = 10)
plt.yticks(np.arange(78, 100, 2),fontproperties = 'Times New Roman', size = 10)

plt.legend(['multi_agent','single_agent','direct'])
plt.show()

