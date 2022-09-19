"""Compress video with moviepy"""

import os
import moviepy.editor as mpy

def compress_video(input_file, output_file, bitrate='5000k'):
    """Compress video with moviepy"""
    clip = mpy.VideoFileClip(input_file)
    clip.write_videofile(output_file, bitrate=bitrate)

if __name__ == '__main__':
    compress_video('runs/track/exp/demo.mp4', 'runs/track/exp/demo_001.mp4')