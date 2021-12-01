import os,sys,shutil
import cv2
import numpy as np


USAGE = "python %s inPath [outPath]"%sys.argv[0]
USAGE += "\n example: python %s ../masks ./output.mp4"%sys.argv[0]

if len(sys.argv) < 2 or '-h' in sys.argv or '--help' in sys.argv:
    print(USAGE)
    os._exit(0)

if len(sys.argv)>=3:
    inPath = sys.argv[1]
    video = sys.argv[2]
elif len(sys.argv)==2:
    inPath = sys.argv[1]
    video = inPath+'.mp4'

print(f'inPath is {inPath}')
print(f'video is {video}')
fs = os.listdir(inPath)
fs = [i for i in fs if i.endswith('.png') or i.endswith('.jpg')]
fs.sort()
print(inPath, fs[0], os.path.join(inPath, fs[0]), os.path.isfile(os.path.join(inPath, fs[0])))
img = cv2.imread(os.path.join(inPath, fs[0]))
h,w = img.shape[:2]


# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video, fourcc, 30.0, (w,h))

for f in fs:
    img = cv2.imread(os.path.join(inPath, f))
    img = cv2.putText(img, f, (30,30), cv2.FONT_HERSHEY_COMPLEX_SMALL , 1, (0,0,255), 1)
    out.write(img)
    #cv2.imshow('frame', img)
    #c = cv2.waitKey(1)
    #if c & 0xFF == ord('q'):
    #    break

out.release()
cv2.destroyAllWindows()


