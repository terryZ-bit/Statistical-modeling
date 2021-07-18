"""
    此代码用于分析灰色关联度并画图
"""
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib

# 设置中文字体部分
font = {'family': 'MicroSoft Yahei',
        'weight': 'bold',
        'size': 12}

matplotlib.rc("font", **font)

x = pd.read_excel("gery.xlsx", names=None)
# x = pd.read_csv("2017_2main.csv", names=None)
x = x.iloc[:, 0:].T
# 2、提取参考队列和比较队列
ck = x.iloc[0, :]
cp = x.iloc[1:, :]

# 比较队列与参考队列相减
t = pd.DataFrame()
for j in range(cp.index.size):
    temp = pd.Series(cp.iloc[j, :] - ck)
    t = t.append(temp, ignore_index=True)

# 求最大差和最小差
mmax = t.abs().max().max()
mmin = t.abs().min().min()
rho = 0.5
# 3、求关联系数
ksi = ((mmin + rho * mmax) / (abs(t) + rho * mmax))
df = pd.DataFrame(data=ksi, index=range(0, 28))
df.to_csv('关联系数.csv')
print(ksi)
# 4、求关联度
r = ksi.sum(axis=1) / ksi.columns.size

''' 绘制柱状图 '''
plt.bar(range(0, len(r)), r)
plt.xticks(range(0, len(r)), ['x1', 'x2', 'x3', 'x4',
                                   'x5', 'x6', 'x7', 'x8',
                                   'x9', 'x10', 'x11', 'x11'],
           fontsize=10)
plt.xlabel('指标')
plt.ylabel('灰色关联度')
plt.title('指标关联度')
plt.show()
# 5、关联度排序，得到结果r3>r2>r1
result = r.sort_values(ascending=False)
print(result)
