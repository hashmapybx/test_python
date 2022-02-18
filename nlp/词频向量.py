
import nltk
from nltk.tokenize import TreebankWordTokenizer

sentence = "Tom Sellers tells his story and the story of British food through an ever-evolving tasting menu of seasonal dishes."
tok = TreebankWordTokenizer()
tokens = tok.tokenize(sentence.lower())
print(tokens)
document_vector = []
doc_len = len(tokens)
# 统计list里面的次数
from collections import Counter

bag_of_words  = Counter(tokens)
print(bag_of_words)

# most_common 按照频率进行排序 只是获取前面5个
res = bag_of_words.most_common(5)
print(res)


for key, value in bag_of_words.most_common():
    document_vector.append(value / doc_len)

print(document_vector)


docs = ['these words she greeted Prince Vasili Kuragin, a man of high rank and'
        ,'had had a cough for some days. She was, as she said, suffering from',
        'embroidered court uniform, knee breeches, and shoes, and had stars on'
        ]

doc_tokens = []

for doc in docs:
    doc_tokens += [sorted(tok.tokenize(doc.lower()))]

print(doc_tokens)
all_doc_tokens = sum(doc_tokens,[])
print(len(all_doc_tokens))

# 词库
lexicon = sorted(set(all_doc_tokens))
print(lexicon)
# 计算频率
from  collections import OrderedDict

zero_vector = OrderedDict((token, 0) for token in lexicon)
print(zero_vector)

# 更新向量的值
import copy
doc_vectors = []
for doc in docs:
    vec = copy.copy(zero_vector)
    tokens = tok.tokenize(doc.lower())
    token_counts = Counter(tokens)
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)
    doc_vectors.append(vec)

print(doc_vectors)





