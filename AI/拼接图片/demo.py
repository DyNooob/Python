import glob
import argparse
from itertools import product

import cv2
import numpy as np # 数组运算
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
    sourceimages = []
    # 平均颜色列表
    avgcolors = []

    for path in tqdm(glob.glob("{}/*.jpg".format(sourcepath))): # 读取文件路径 tqdm为进度条
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        if image.shape[-1] != 3: # RGB三原色为三, 不为三则不要
            continue

        image = cv2.resize(image, (blocksize, blocksize)) # 缩放尺寸大小
        avgcolor = np.sum(np.sum(image, axis=0), axis=0)/(blocksize, blocksize)

        sourceimages.append(image)
        avgcolors.append(avgcolor)
    print('读取结束')
    return sourceimages, np.array(avgcolors)


def main(args):
    targetimage = cv2.imread(args.targetpath)
    outputimage = np.zeros(targetimage.shape, np.uint8)

    sourceimages, avgcolors = readSourceImage(args.sourcepath, args.blocksize)

    print('开始制作')

    for i, j in tqdm(product(range(int(targetimage.shape[1]/args.blocksize)),
                             range(int(targetimage.shape[0]/args.blocksize)))):
        block = targetimage[j * args.blocksizeL(j + 1) * args.blocksize, i * args.blocksize:(i + 1) * args.blocksize, :]
        avgcolor = np.sum(np.sum(block, axis=0), axis=0) / (args.blocksize * args.blocksize)
        distances = np.linalg.norm(avgcolor - avgcolors, axis=1)

        idx = np.argmin(distances)
        outputimage[j * args.blocksizeL(j + 1) * args.blocksize, i * args.blocksize:(i + 1) * args.blocksize, :] = sourceimages[idx]

    cv2.imwrite(args.outputpath, outputimage)
    cv2.imshow('result', outputimage)
    print('Done')




if __name__ == '__main__':

    main(parsArgs())