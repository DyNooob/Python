import glob
import argparse
from itertools import product

import cv2
import numpy as py
from tqdm import tqdm

'''
NOTE(Jan.21.2021):
- 输入
- 计算处理
- 输出
- 展示
'''



# 图片文件
def parsArgs():
    parser = argparse.ArgumentParser('拼接马赛克图片')# 说明
    parser.add_argument('--targetpath', type=str, default='target/1.jpg', help='目标图像路径')
    parser.add_argument('--outputpath', type=str, default='output/done.jpg', help='输出图像路径') # eg:out/a.jpg
    parser.add_argument('--sourcepath', type=str, default='sourceimages', help='拼接图像所有原图像')
    parser.add_argument('--blocksize', type=int, default='15', help='马赛克块大小')

    args = parser.parse_args()

    return args

# 读取图像内容, 并且计算对应色彩平局值
def readSourceImage(sourcepath,blocksize):
    print('开始读取图像')
    # 符合颜色要求图像
    sourceimage = []
    # 平均颜色列表
    avgcolors = []

    for path in tqdm(range(glob.glob("{}/*jpg".format(sourcepath)))): # 读取文件路径 tqdm为进度条
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        if image.shape[-1] != 3: # RGB三原色为三, 不为三则不要
            continue

        image = cv2.resize(image, (blocksize, blocksize)) # 缩放尺寸大小



image = cv2.imread('sourceimages/desktop1.jpg')
print(image)
