from read_queries import charger_requete,charger_stopWord
from nltk.stem import PorterStemmer

charger_stopWord("data/stopwords.txt")
print(charger_requete("data/queries.txt"))
