# vidsmaller.py
# goes through a directory & makes all mp4s smaller.
# v0.1 - 07/22/19

# 17.1 MB -> 3.27 (mp4 to webm)
# crf 20 made it bigger by .4 MB, 24 made it smaller by ~6 MB, 26 made it smaller by ~8 MB, 28 made it smaller by ~10 MB
# crf 28 -> webm sliced off 14 MB | 

import os
import subprocess
import argparse

def build_ffmpeg_cmd(filename, args):
    input_piece = "ffmpeg -i " + filename

    base_filename, file_ext = os.path.splitext(filename)
    output_piece = base_filename + "-converted" + args.fileext

    # figure out what transformations to make
    transforms = ""

    if args.width != None and args.height != None:
        print("new scale is " + str(args.width) + "x" + str(args.height))
        transforms += "-vf scale=" + str(args.width) + ":" + str(args.height)

    # doesn't work combined with change filename
    if args.crf != None:
        print("new crf is " + str(args.crf))
        transforms += "-vcodec libx265 -crf " + str(args.crf)

    ffmpeg_cmd = input_piece + " " + transforms + " " + output_piece
    return ffmpeg_cmd + " -hide_banner"

def main():
    # setup the argparser
    desc = "Make a video smaller by resizing & compressing it."
    parser = argparse.ArgumentParser(description=desc)

    # add all the arguments
    parser.add_argument("--fileext",
        help="the extension to convert videos to.", default=".mp4")
    parser.add_argument("--width",
        help="the new width of the video. default = no change.", type=int)
    parser.add_argument("--height",
        help="the new height of the video. default = no change.", type=int)
    parser.add_argument("--crf",
        help="new constant rate factor for the video, from 18-24. varies the average bitrate. default = no change.", type=int)

    # make args available for use
    # TODO: validate input
    args = parser.parse_args()

    for root, dirs, files in os.walk("."):
        print("**** Smallify-ing all videos in " + root)
        for item in files:
            # make sure it's a video file!
            base_filename, file_ext = os.path.splitext(item)

            if file_ext == ".mp4":
                print("** smallify-ing " + item + " ...")
                ffmpeg_cmd = build_ffmpeg_cmd(item, args)
                print("executing command >>>" + ffmpeg_cmd)
                subprocess.run(ffmpeg_cmd)
            else:
                print("** skipping " + item + " because it's not a video file.")

main()
