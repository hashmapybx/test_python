# 下面给出了一个统计词出现次数很有用的例

# 这里引入第一个近似假设，假设一个词在文档中出现的次数越多，那么该词对文档的意义的贡献就越大
import math

import nltk
from nltk.tokenize import TreebankWordTokenizer

sentence = "Tom Sellers tells his story and the story of British food through an ever-evolving tasting menu of seasonal dishes."
tok = TreebankWordTokenizer()
tokens = tok.tokenize(sentence.lower())
print(tokens)

# 统计list里面的次数
from collections import Counter

bag_of_words  = Counter(tokens)
print(bag_of_words)

# most_common 按照频率进行排序 只是获取前面5个
res = bag_of_words.most_common(5)
print(res)

print("计算词频")
# 计算词频
all_words = len(bag_of_words.keys())
print(all_words)

# 下面是计算每一个词的词频
every_word_freq = [(k, round(y/all_words, 4)) for k,y in bag_of_words.items()]
print(every_word_freq)

# 去除停用词
stopwords = nltk.corpus.stopwords.words('english')

s_tok = [w for w in tokens if w not in stopwords]
print(s_tok)









