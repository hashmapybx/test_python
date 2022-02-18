from nltk.stem.porter import  PorterStemmer

# 词干还原 两种流行的方式是poter snowball
# stemming

stem = PorterStemmer()
sens = "dish washer's washed dishes"
res = [stem.stem(s).strip("'") for s in sens.split()]
print(res)
