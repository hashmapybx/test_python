# VADER 一个基于规则的情感分析算办法

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()
print(sa.lexicon)

res = [(tok, score) for tok, score in sa.lexicon.items() if ' ' in tok]
print(res[1:5])

s1 = "Python is very readable and it's great for NLP."
print(sa.polarity_scores(text=s1))
# {'neg': 0.0, 'neu': 0.661, 'pos': 0.339, 'compound': 0.6249}
# vader 算法是用三个不同的分数来表示情感 中立 正向 负向 复合



