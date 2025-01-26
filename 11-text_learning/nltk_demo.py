import nltk
from nltk.corpus import stopwords

nltk.download()
sw = stopwords.words("english")

print(sw)
print("Stopwods count:", len(sw))