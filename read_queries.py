
from nltk.stem import PorterStemmer

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
    tab=[]
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines() 

      for ligne in lignes:
        tab.append(ligne.strip())

    return tab


def charger_stemp(nom_fichier):
    tab=[]
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines() 

      for ligne in lignes:
        tab.append(ligne.strip())

    return tab
