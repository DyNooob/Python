import cv2
import glob
import argparse
import numpy as np
from tqdm import tqdm  # 进度条
from itertools import product  # 迭代器


def parseArgs():
    parser = argparse.ArgumentParser('拼接马赛克图片')
    parser.add_argument('--targetpath', type=str, default='examples/1.jpg', help='目标图像路径')
    parser.add_argument('--outputpath', type=str, default='output.jpg', help='输出图像路径')
    parser.add_argument('--sourcepath', type=str, default='E:\Python\Reptiles\表情包\saves', help='用于拼接图像的所有源图像文件夹路径')
    parser.add_argument('--blocksize', type=int, default=15, help='马赛克块大小')
    args = parser.parse_args()
    return args


def readSourceImages(sourcepath, blocksize):
    print('开始读取图像')
    # 合法图像列表
    sourceimages = []
    # 平均颜色列表
    avgcolors = []
    for path in tqdm(glob.glob("{}/*.jpg".format(sourcepath))):
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        if image is None or image.shape[-1] != 3:
            continue
        image = cv2.resize(image, (blocksize, blocksize))
        avgcolor = np.sum(np.sum(image, axis=0), axis=0) / (blocksize * blocksize)
        sourceimages.append(image)
        avgcolors.append(avgcolor)
    print('结束读取')
    return sourceimages, np.array(avgcolors)


def main(args):
    targetimage = cv2.imread(args.targetpath)
    outputimage = np.zeros(targetimage.shape, np.uint8)  # int8 int16 int32 int64
    sourceimages, avgcolors = readSourceImages(args.sourcepath, args.blocksize)
    print('开始制作')
    for i, j in tqdm(product(range(int(targetimage.shape[1] / args.blocksize)),
                             range(int(targetimage.shape[0] / args.blocksize)))):
        block = targetimage[j * args.blocksize: (j + 1) * args.blocksize, i * args.blocksize: (i + 1) * args.blocksize,
                :]
        avgcolor = np.sum(np.sum(block, axis=0), axis=0) / (args.blocksize * args.blocksize)
        distances = np.linalg.norm(avgcolor - avgcolors, axis=1)
        idx = np.argmin(distances)
        outputimage[j * args.blocksize: (j + 1) * args.blocksize, i * args.blocksize: (i + 1) * args.blocksize, :] = \
            sourceimages[idx]
    cv2.imwrite(args.outputpath, outputimage)
    cv2.imshow('result', outputimage)
    print('制作完成')


if __name__ == '__main__':
    # run
    main(parseArgs())
