
# 词形归并

# 在Python中如何识别词元？NLTK包提供了相关的函数。
# 需要注意的是，如果需要得到更精确的词元，需要告诉WordNetLemmatizer你感兴趣的词性是什

import nltk

# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("better",pos='a'))
print(lemmatizer.lemmatize('best', pos='a'))

# best不会和better产生同样的词根。WordNet词义图中也忽略了goodness和good之间的关联
