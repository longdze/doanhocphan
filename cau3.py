import matplotlib.pyplot as plt
import numpy as np


def dao_ham_pt_y(x):
    pt=x**4 - 2*x**2 - 3
    return pt
def dao_ham_pt_y1(x):
    pt1=4*x**3 - 4*x
    return pt1
def dao_ham_pt_y2(x):
    pt2 = 12*x**2 - 4
    return pt2
def dao_ham_pt_y3(x):
    pt3 = 24*x
    return pt3
fig, ax = plt.subplots()
x=np.linspace(-10,10,200)
y= dao_ham_pt_y(x)
ax.plot(x,y)
y1= dao_ham_pt_y1(x)
ax.plot(x,y1)
y2= dao_ham_pt_y2(x)
ax.plot(x,y2)
y3= dao_ham_pt_y3(x)
ax.plot(x,y3)
ax.set_xlabel("Trục hoành - x")
ax.set_ylabel("Trục tung - y")
plt.show()

