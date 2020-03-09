from video2hls.video import Video
import os
import sys
import click

@click.command()
@click.option('--vfile', prompt=True, required=True, help='Specify video file name')
@click.option('--hlsdir', prompt=True, required=True, help='Specify hls directory')
def run(vfile, hlsdir):
    os.environ['HLS_DIR'] = hlsdir 
    v = Video(vfile)
    v.process()
    print(v.vmeta)


if __name__ == "__main__":
    run()
