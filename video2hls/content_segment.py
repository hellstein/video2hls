from video2hls.processor import Processor
import os
from pathlib import Path

class ContentSegment(Processor):

    cmd_pattern = "ffmpeg -i {} -c:a aac -ar 48000 -b:a 128k -c:v h264 -profile:v main -crf 23 -g 61 -keyint_min 61 -sc_threshold 0 -b:v 5300k -maxrate 5300k -bufsize 10600k -hls_time 6 -hls_playlist_type vod {}/video.m3u8"

    def get_segment_cmd(self):
        meta = self.video.vmeta
        dest_dir = os.path.join(str(Path.home()), os.environ.get('HLS_DIR'))
        self.orig, self.dest = meta["file"], os.path.join(dest_dir, meta["encoded_name"][:16])
        return self.__class__.cmd_pattern.format(self.orig, self.dest) 

    def run(self):
        cmd = self.get_segment_cmd()
        if not os.path.exists(self.dest):
            os.mkdir(self.dest)
            print("Directory " , self.dest ,  " Created ")

        os.system(cmd)



if __name__ == "__main__":
    pass


