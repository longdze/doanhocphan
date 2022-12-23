from p2_lap_trinh_voi_thu_vien.cau4 import *

def main():
    fig,(ax1,ax2,ax3)=plt.subplots(1,3, subplot_kw = {"projection": "3d"})
    x = np.linspace(start=-15.0, stop=15.0, num=1000)
    y = np.linspace(start=-15.0, stop=15.0, num=1000)
    x, y = np.meshgrid(x, y)
    x2 = np.linspace(start=-10.0, stop=10.0, num=1000)
    y2 = np.linspace(start=-10.0, stop=10.0, num=1000)
    x2, y2 = np.meshgrid(x2, y2)
    x3 = np.linspace(start=-6, stop=2, num=2000)
    y3 = np.linspace(start=-3, stop=5, num=2000)
    x3, y3 = np.meshgrid(x3, y3)
    ax1.set_zlim(-60, 40)
    ax2.set_zlim(-8, 8)
    ax3.set_zlim(0, 7)
    z1=giai_bai(x,y)
    z2=giai_bai_hyperbolic1(x2,y2)
    z22=giai_bai_hyperbolic2(x2,y2)
    z3=do_thi_mat_cau(x3,y3)
    z33=do_thi_mat_cau2(x3,y3)
    ax1.plot_surface(x,y,z1,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax2.plot_surface(x2,y2,z2,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax2.plot_surface(x2, y2, z22,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax3.plot_surface(x3,y3,z3,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    ax3.plot_surface(x3, y3, z33,cmap= cm.gist_heat_r,linewidth=0, antialiased=False)
    plt.show()


if __name__ =='__main__':
    main()