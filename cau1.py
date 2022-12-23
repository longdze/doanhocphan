import numpy as np
import random
random.seed(123)



def tinh_tich_xA():
    n=int(input('nhap n= '))
    m=int(input('nhap m= '))
    x=[np.random.random(n)]
    x=np.array(x)
    print('vector')
    print("x= ",x)
    A=np.random.rand(m,n)
    print('ma tran')
    print('A= ',A)
    z=x*A
    print('tich cua vector x va matran A la: z= ',z)
    return z

def tinh_tich_AB():
    n=int(input('n= '))
    m=int(input('m= '))
    A=np.random.rand(m,n)
    print('ma tran A=',A)
    B= np.random.rand(m,n)
    print('ma tran B=',B)
    f = np.multiply(A,B)
    print('A*B=',f)
    AT = np.transpose(A)
    print('ma tran chuyen vi A = ',AT)
    fx =np.dot(AT, B)
    print('A^T * B= ',fx)
    return f, fx

