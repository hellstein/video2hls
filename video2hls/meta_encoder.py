from video2hls.processor import Processor
from video2hls.commonlib import get_meta_from_filename, encoding_meta_to_filename

class MetaEncoder(Processor):
    def encode(self):
        self.meta = get_meta_from_filename(self.video.vfile)
        self.meta["encoded_name"] = encoding_meta_to_filename(self.meta)
        return self.meta

    def is_valid(self, code):
        return self.encode() == code

    def run(self):
        self.video.vmeta.update(self.encode())

if __name__ == "__main__":
    pass
