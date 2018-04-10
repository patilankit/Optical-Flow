import cv2
import numpy as np
from matplotlib import pyplot as plt

def optFlow(img1,img2,lamda,n):
    #set up initial velocities
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)
    uInit = np.zeros([img1.shape[0],img1.shape[1]])
    vInit = np.zeros([img1.shape[0],img1.shape[1]])

    # Set initial value for the flow vectors
    u = uInit
    v = vInit


    # Averaging kernel
    kernel=np.matrix([[1/12, 1/6, 1/12],[1/6, 0, 1/6],[1/12, 1/6, 1/12]])
    # kernel=np.matrix([[0, 1/4, 0],[1/4, 0, 1/4],[0, 1/4, 0]])

    # Estimate derivatives
    Ex, Ey, Et = derivatives(img1, img2)

    # Iteration to reduce error
    for i in range(n):

        # Compute averages of the flow vectors
        uAvg = cv2.filter2D(u,-1,kernel)
        vAvg = cv2.filter2D(v,-1,kernel)

        uNumer = (Ex.dot(uAvg) + Ey.dot(vAvg) + Et).dot(Ex)
        uDenom = 1 + lamda*(Ex**2 + Ey**2)
        u = uAvg - np.divide(uNumer,uDenom)

        # print np.linalg.norm(u)

        vNumer = (Ex.dot(uAvg) + Ey.dot(vAvg) + Et).dot(Ey)
        vDenom = lamda + Ex**2 + Ey**2
        v = vAvg - np.divide(vNumer,vDenom)
    return (u,v)


def derivatives(img1,img2):
    Ex,Ey,Et = np.array(img1,copy=True),np.array(img1,copy=True),np.array(img1,copy=True)
    for i in range(1,img1.shape[0]-1):
        for j in range(1,img1.shape[0]-1):
            Ex[i][j] = (0.25*img1[i+1][j] + 0.25*img1[i+1][j+1] + 0.25*img2[i+1][j] + 0.25*img2[i+1][j+1]) - (0.25*img1[i][j] + 0.25*img1[i][j+1] + 0.25*img2[i][j]+ 0.25*img2[i][j+1])
            Ey[i][j] = (0.25*img1[i][j+1] + 0.25*img1[i+1][j+1] + 0.25*img2[i][j+1] + 0.25*img2[i+1][j+1]) - (0.25*img1[i][j] + 0.25*img1[i+1][j] + 0.25*img2[i][j]+ 0.25*img2[i+1][j])
            Et[i][j] = (0.25*img2[i][j] + 0.25*img2[i+1][j+1] + 0.25*img2[i+1][j] + 0.25*img2[i][j+1]) - (0.25*img1[i][j] + 0.25*img1[i][j+1] + 0.25*img1[i+1][j]+ 0.25*img1[i+1][j+1])
    return Ex,Ey,Et

def smoothImage(img,kernel):
    G = gaussFilter(kernel)
    smoothedImage=cv2.filter2D(img,-1,G)
    smoothedImage=cv2.filter2D(smoothedImage,-1,G.T)
    return smoothedImage

def gaussFilter(segma):
    kSize = 2*(segma*3)
    x = range(-kSize/2,kSize/2,1+1/kSize)
    x = np.array(x)
    G = (1/(2*np.pi)**.5*segma) * np.exp(-x**2/(2*segma**2))
    return G

