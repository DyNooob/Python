# coding:utf-8
import jieba
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']


def load_file_segment():
    # 读取文本文件并分词
    f = codecs.open("E:/Python/文本分析/yel.txt", 'r', encoding='utf-8')
    # 打开文件
    content = f.read()
    # 读取文件到content中
    f.close()
    # 关闭文件
    segment = []
    # 保存分词结果
    segs = jieba.cut(content)
    # 对整体进行分词
    for seg in segs:
        if len(seg) > 1 and seg != '\r\n':
            # 如果说分词得到的结果非单字，且不是换行符，则加入到数组中
            segment.append(seg)
    return segment


# 获得分词结果
segment = load_file_segment()

# 将分词数组转化为pandas数据结构
df = pandas.DataFrame({'segment': segment})

# 加载停用词
stopwords = pandas.read_csv("E:/Python/文本分析/stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding="utf-8")

# 如果不是在停用词中
df = df[~df.segment.isin(stopwords.stopword)]

# 计数
words_stat = df.groupby(by=['segment'])['segment'].agg([("计数", numpy.size),])
words_stat = words_stat.reset_index().sort_values(by="计数", ascending=False)
words = words_stat.set_index("segment").to_dict()

# 计算总词汇分布
for i in range(0, 20):
    plt.bar((list(words['计数'].keys())[i],), (list(words['计数'].values())[i],))
plt.title('《坠落》词频(TOP1-20)')
plt.xlabel('词语')
plt.ylabel('词频')
plt.legend('词频直方图')
plt.show()

# 计算黄色词汇
yellow_words = [word.strip('\n') for word in open('E:/Python/文本分析/yellow.txt', 'r', encoding='utf-8').readlines()]
origin_yellow_count = {
    word: words['计数'][word]
    for word in words['计数'] if word in yellow_words
}
# 计算非黄色词汇
not_yellow_count = {
    word: words['计数'][word]
    for word in words['计数'] if word not in yellow_words
}
for i in range(0, 20):
    plt.bar((list(origin_yellow_count.keys())[i],), (list(origin_yellow_count.values())[i],))
plt.title('《坠落》敏感词频(TOP1-20)')
plt.xlabel('词语')
plt.ylabel('词频')
plt.legend('词频直方图')
plt.show()

# 设定图片
bimg = imread('E:/Python/文本分析/unnamed.jpg')
wordcloud = WordCloud(background_color="white",mask=bimg, font_path='simhei.ttf', min_font_size=1)
# 生成词云
wordcloud = wordcloud.fit_words(words["计数"])
bimgColors = ImageColorGenerator(bimg)

# 渲染词云
plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=bimgColors))
plt.show()
