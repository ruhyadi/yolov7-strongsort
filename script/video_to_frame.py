"""Convert video to frame"""

import os
import cv2
import argparse

def main(video_path: str, output_path: str, start: int, long: int):
    """convert video to frame"""
    os.makedirs(output_path) if not os.path.exists(output_path) else None
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, start * 1000)
    fps = cap.get(cv2.CAP_PROP_FPS)
    time_count = 1 / fps
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if time_count <= long:
                cv2.imwrite(os.path.join(output_path, f"frames{frame_count:03d}.jpg"), frame)
                frame_count += 1
                time_count += 1 / fps
            else:
                break
        else:
            break
    cap.release()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Convert video to frame")
    parser.add_argument("--video_path", default="demo/demo.mp4", type=str, help="video path")
    parser.add_argument("--output_path", default="demo/frames001", type=str, help="output path")
    parser.add_argument("--start", type=int, default=110, help="start time")
    parser.add_argument("--long", type=int, default=10, help="long time")
    args = parser.parse_args()

    main(args.video_path, args.output_path, args.start, args.long)