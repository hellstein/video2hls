from video2hls.video import Video
import os
import sys

def run():
    vfile = sys.argv[1]
    os.environ['HLS_DIR'] = sys.argv[2]
    v = Video(vfile)
    v.process()
    print(v.vmeta)

