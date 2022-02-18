from sklearn.feature_extraction.text import  ENGLISH_STOP_WORDS as sklearn_stop_words



# sklearn 里面停用词的长度
print(len(sklearn_stop_words))

import nltk
# nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
print("nltk 里面的stop word", len(stop_words))
# 查看stopword 里面长度等于1的数据
len_1_word = [w for w in stop_words if len(w) == 1]



