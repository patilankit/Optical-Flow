from matplotlib.pyplot import figure,draw,pause,gca
# from pathlib import Path



def compareGraphs(u,v,Inew,scale=9, quivstep=5, fn=''):
    """
    makes quiver
    """

    ax = figure().gca()
    ax.imshow(Inew,cmap = 'gray', origin='lower')
    # plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(0,len(u), quivstep):
        for j in range(0,len(v), quivstep):
            ax.arrow(j,i, v[i,j]*scale, u[i,j]*scale, color='red',
                     head_width=1.5, head_length=1.5)

	# plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)
    ax.set_title(fn)
    draw(); pause(0.01)
    return