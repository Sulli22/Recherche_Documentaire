import nltk
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

nltk.download("stopwords")
def charger_requete(nom_fichier):
    stemmer = PorterStemmer()
    tab=[]
    stopW=charger_stopWord("data/stopwords.txt")
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines() 

      for ligne in lignes:
        lg=[]
        lg.append(ligne.strip().split())
        for aux in lg:
            w=[]
            for wrd in aux:
              if(wrd not in stopW):
               
                w.append(stemmer.stem(wrd))

            tab.append(w)

    return tab


    

def charger_stopWord(nom_fichier):
    tab=set(stopwords.words("english"))
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines() 

      for ligne in lignes:
        if ligne.strip() not in tab:
           tab.add(ligne.strip())

    return tab


def charger_stemp(nom_fichier):
    tab=[]
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines() 

      for ligne in lignes:
        tab.append(ligne.strip())

    return tab


def charger_donnees(fichiers):
  stemmer = PorterStemmer()
  donnees = {}
  stopW = charger_stopWord("data/stopwords.txt")
  
  for fichier in fichiers:
     with open(fichier, 'r') as f:
        contenu = BeautifulSoup(f.read(), "html.parser")
    
        for doc in contenu.find_all("doc"):
          docno = doc.find("docno").get_text(strip=True)
    
          texte = doc.find("text").get_text()
      
          texte = texte.replace("'", " ").replace("`", " ")
          texte = texte.split()
          
          fdist = FreqDist()
          for mot in texte:
            if mot.lower() not in stopW:
              fdist[mot.lower()] += 1
          donnees[docno] = {"texte":fdist}

  return donnees
          
           

     
