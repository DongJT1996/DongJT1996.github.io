# @Author  : Junting Dong
# @Mail    : jtdong@zju.edu.cn

import cv2
from os.path import join
import os

if __name__ == '__main__':
    # image
    if False:
        img = join('images', 'tmvpose.png')
        img = cv2.imread(img)
        img_save = cv2.resize(img, (160, 160))
        cv2.imwrite(join('images', 'tmvpose.jpg'), img_save)
    # video
    if True:
        # os.system('ffmpeg -i tmvpose.mp4 -ss 00:00:40 -t 00:00:07 -vcodec h264 -strict -2 tmvpose_.mp4') # select time range
        # os.system('ffmpeg -i tmvpose_.mp4 -strict -2 -vf crop=500:500:1200:200 tmvpose_crop.mp4') # select space range
        # os.system('ffmpeg -i tmvpose_crop.mp4 -vf scale=160:160, setsar=1:1 tmvpose_resize.mp4')
        os.system('ffmpeg -i /mnt/data/download/homie.mp4 -ss 00:00:00 -t 00:00:20 -vcodec h264 -strict -2 /mnt/data/download/homie_.mp4')
        # os.system('ffmpeg -i tmvpose_.mp4 -strict -2 -vf crop=500:500:1200:200 tmvpose_crop.mp4')
        os.system('ffmpeg -i /mnt/data/download/homie_.mp4 -vf "scale=160:160:force_original_aspect_ratio=decrease,pad=160:160:(ow-iw)/2:(oh-ih)/2:white" -c:a copy /mnt/data/download/homie_final.mp4')
        # os.system('ffmpeg -i /mnt/data/download/homie_.mp4 -vf scale=160:160, setsar=1:1 /mnt/data/download/homie_final.mp4')
