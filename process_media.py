# @Author  : Junting Dong
# @Mail    : jtdong@zju.edu.cn

import cv2
from os.path import join
import os
import numpy as np
from tqdm import tqdm


def process_img(img, resize=(600, 600)):
    # construct the large image
    height, width = img.shape[:2]
    diff = height - width
    if bg == 'white':
        bg_value = 255
    elif bg == 'black':
        bg_value = 0
    else:
        bg_value = 255
    if diff == 0:
        pass
    elif diff > 0:
        addition = np.ones((height, diff//2, 3)) * bg_value
        processed_img = np.concatenate((addition, img, addition), axis=1)
    else:
        addition = np.ones((-diff // 2, width, 3)) * bg_value
        processed_img = np.concatenate((addition, img, addition), axis=0)

    processed_img = cv2.resize(processed_img.astype(np.uint8), resize)

    return processed_img

def process_video(file_name):
    save_path = join(os.path.dirname(file_name), '.'.join(os.path.basename(file_name).split('.')[:-1]))
    os.makedirs(save_path, exist_ok=True)
    video = cv2.VideoCapture(file_name)
    totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    index = 0
    for cnt in tqdm(range(totalFrames)):
        ret, frame = video.read()
        if not ret:
            print('[ATTN] {} not valid'.format(cnt))
            continue
        process_frame = process_img(frame)
        cv2.imwrite(join(save_path, '{:06d}.jpg'.format(index)), process_frame)
        index += 1
    video.release()
    cmd = 'ffmpeg -f image2 -i {}/%06d.jpg {}/{}'.format(
        save_path, os.path.dirname(file_name), 'processed_'+os.path.basename(file_name))
    os.system(cmd)

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str)
    parser.add_argument('--bg', type=str, default='white')
    args = parser.parse_args()

    file_name = args.input_path
    bg = args.bg
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # deal with images
        img = cv2.imread(file_name)
        processed_img = process_img(img)
        save_path = join(os.path.dirname(file_name), 'processed_'+os.path.basename(file_name))
        cv2.imwrite(save_path, processed_img)
    elif file_name.endswith('.mp4'):
        # deal with videos
        import ipdb; ipdb.set_trace(context=11)
        process_video(file_name)
        pass
    else:
        pass

