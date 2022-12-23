import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def giai_bai(x,y):
    f=(x/3)**2 - (y/2)**2
    return f
def giai_bai_hyperbolic1(x,y):
    z1=(x/3)**2 + (y/5)**2 - 1
    return 2*np.sqrt(z1)

def giai_bai_hyperbolic2(x,y):
    z2=(x/3)**2 + (y/5)**2 - 1
    return -2*np.sqrt(z2)

def do_thi_mat_cau(x,y):
    f = 4 + ((4 -(x**2 + 2*x + 4)-(y**2 - 2*y+1))**(1/2))
    return  f

def do_thi_mat_cau2(x,y):
    f2 = 4 - ((4 -(x**2 + 2*x + 4)-(y**2 - 2*y+1))**(1/2))
    return f2

def do_thi_yen_ngua(x,y):
    x, y = np.meshgrid(x, y)
    f=giai_bai(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    mat_yen_ngua_surf= ax.plot_surface(x, y,f,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax.set_zlim(-60,40)
    fig.colorbar(mat_yen_ngua_surf, shrink=0.5,aspect=5)
    plt.show()

def do_thi_hyperbolic_1tang(x,y):
    x, y = np.meshgrid(x, y)
    f1=giai_bai_hyperbolic1(x,y)
    f2=giai_bai_hyperbolic2(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    hyperbolic_surf= ax.plot_surface(x, y,f1,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    hyperbolic_surf= ax.plot_surface(x, y,f2,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax.set_zlim(-8,8)
    fig.colorbar(hyperbolic_surf, shrink=0.7,aspect=5)
    plt.show()

def do_thi_matcau(x,y):
    x, y = np.meshgrid(x, y)
    f = do_thi_mat_cau(x,y)
    f2 =do_thi_mat_cau2(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    mat_cau_surf= ax.plot_surface(x, y,f,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    mat_cau_surf= ax.plot_surface(x, y,f2,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax.set_zlim(2,6)
    fig.colorbar(mat_cau_surf, shrink=0.5,aspect=10)
    plt.show()