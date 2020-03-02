from video2hls.meta_encoder import MetaEncoder
from video2hls.content_segment import ContentSegment
import sys
import os

class Video:

    def __init__(self, vfile, vmeta={}):
        self.vfile, self.vmeta = vfile, vmeta
        self.processors = []
        self.register(MetaEncoder).register(ContentSegment)

    def register(self, p_class):
        p = p_class(self)
        self.processors.append(p)
        return self

    def process(self):
        for p in self.processors:
            p.run()

