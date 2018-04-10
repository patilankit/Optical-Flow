import os
import imageio
from compareGraphs import compareGraphs
from hornschunck import HornSchunck
import scipy

base_dir = '/home/ankit/Desktop/CV/OpticalFlow'

img0 = os.path.join(base_dir,'box_0.bmp')
img1 = os.path.join(base_dir,'box_1.bmp')
img0 = imageio.imread(img0, as_gray=True)
img1 = imageio.imread(img1, as_gray=True)
lamda = 1.;
n = 100;

u,v = HornSchunck(img0, img1, 1., 100)
compareGraphs(u,v, img1,scale=9, fn="Test")



vid_path = '/home/ankit/Desktop/CV/OpticalFlow/Translational_motion_1.mp4'
reader = imageio.get_reader(vid_path)

for i, im in enumerate(reader):
    if i < (reader._get_length() - 1) and i%15 == 0 and i<48:
        img0 = reader.get_data(i);
        img1 = reader.get_data(i+1);

        # img0 = scipy.misc.imresize(img0[:,:,0],0.3)
        # img1 = scipy.misc.imresize(img1[:,:,0],0.3)
        img0 = scipy.misc.imresize(img0[:,:,0],(200,200))
        img1 = scipy.misc.imresize(img1[:,:,0],(200,200))


        #compute u,v parameters
        u, v = HornSchunck(img0, img1, 0.00001, 100)
        compareGraphs(u,v, img1,scale=3,quivstep=7, fn="Image{:1}".format(i))




#---------------------------------------------------------------- :Read a video frame by frame:
# vid_path = '/home/ankit/Desktop/CV/OpticalFlow/SampleVideo_1280x720_1mb.mp4'
# reader = imageio.get_reader(vid_path)
#
# for i, im in enumerate(reader):
#     print("i is ", i, "Image is ")
#     print('Mean of frame %i is %1.1f' % (i, im.mean()))

























# def horn_schunck(stem, pat:str):
#     flist = getimgfiles(stem, pat)
#
#     for i in range(len(flist)-1):
#         fn1 = flist[i]
#         im1 = imageio.imread(fn1, as_gray=True)
#
#  #       Iold = gaussian_filter(Iold,FILTER)
#
#         fn2 = flist[i+1]
#         im2 = imageio.imread(fn2, as_gray=True)
# #        Inew = gaussian_filter(Inew,FILTER)
#
#         U,V = HornSchunck(im1, im2, 1., 100)
#         compareGraphs(U,V, im2, fn=fn2.name)
#
#     return U,V
#
#
#
# from argparse import ArgumentParser
# p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
# p.add_argument('stem',help='path/stem of files to analyze')
# p.add_argument('pat',help='glob pattern of files',default='*.bmp')
# p = p.parse_args()
#
# U,V = horn_schunck(p.stem, p.pat)
