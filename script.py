# @Author  : Junting Dong
# @Mail    : jtdong@zju.edu.cn

import cv2
from os.path import join
import os

INPUT_VIDEO = '/mnt/data/download/High-Precision2.mp4'

if __name__ == '__main__':
    video_dir = os.path.dirname(INPUT_VIDEO)
    video_name = os.path.splitext(os.path.basename(INPUT_VIDEO))[0]
    tmp_video = os.path.join(video_dir, f'{video_name}_.mp4')
    output_video = os.path.join(video_dir, f'{video_name}_final.mp4')

    # image
    if False:
        img = join('images', 'tmvpose.png')
        img = cv2.imread(img)
        img_save = cv2.resize(img, (160, 160))
        cv2.imwrite(join('images', 'tmvpose.jpg'), img_save)
    # video
    if True:
        os.system(f'ffmpeg -i {INPUT_VIDEO} -ss 00:00:05 -t 00:00:25 -vcodec h264 -strict -2 {tmp_video}')
        os.system(f'ffmpeg -i {tmp_video} -vf "scale=160:160:force_original_aspect_ratio=decrease,pad=160:160:(ow-iw)/2:(oh-ih)/2:white" -c:a copy {output_video}')
