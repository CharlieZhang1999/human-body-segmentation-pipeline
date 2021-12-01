import os,sys,shutil
import cv2
import numpy as np


USAGE = "python %s video [outPath]"%sys.argv[0]
USAGE += "\n example: python %s video.mp4 ./output"%sys.argv[0]



def convert(video, outPath=None):
    if outPath is None:
        pos = video.rfind('.')
        outPath = video[:pos]+'_dir'
    video_name = os.path.split(video)[-1].replace('.mp4','').replace('.avi','')
    print('video_name#%s#'%video_name)

    if os.path.isdir(outPath):
        shutil.rmtree(outPath)
    os.makedirs(outPath)

    cap = cv2.VideoCapture(video)
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    count = 0
    skip = 1
    while(1):
        ret, frame = cap.read()
        #frame = frame[:, 960-300:960+300]
        if ret:
            if count % skip == 0:
                #frame = np.rot90(frame,k=3)
                cv2.imwrite(os.path.join(outPath, "F%05d_%s.png"%(count, video_name)), frame)
            count += 1
        else:
            break
    print(outPath, count, 'frames')

if __name__ == '__main__':
    if len(sys.argv) < 2 or '-h' in sys.argv or '--help' in sys.argv:
        print(USAGE)
        os._exit(0)

    if len(sys.argv)>=3:
        video = sys.argv[1]
        outPath = sys.argv[2]
    elif len(sys.argv)==2:
        video = sys.argv[1]
        outPath = None
    convert(video, outPath)
