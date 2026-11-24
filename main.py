from read_queries import charger_requete,charger_stopWord,charger_donnees
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup

charger_stopWord("data/stopwords.txt")
#print(charger_requete("data/queries.txt"))
data = charger_donnees(["data/AP/AP891216/AP891216"])
print(data["AP891216-0001"])