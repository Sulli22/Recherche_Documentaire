
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

nltk.download("stopwords")
nltk.download('punkt_tab')
def charger_requete(nom_fichier):
    stemmer = PorterStemmer()
    tab={}
    stopW=charger_stopWord("data/stopwords.txt")
    with open(nom_fichier, 'r') as f:
      lignes = f.readlines() 

      for ligne in lignes:
        lg=[]
        lg.append(ligne.strip().split())
        print(lg[0][0])
        id_req=lg[0][0]
        tab.setdefault(id_req,{})
        for aux in lg:
           
            cont=[]
            for wrd in aux[1:]:
              if(wrd not in stopW):
               
               w=stemmer.stem(wrd)
               cont.append(w)
            tab[id_req]=FreqDist(cont)



          

    return tab


    

def charger_stopWord(nom_fichier):
    tab=set(stopwords.words("english"))

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
        cont=ligne.strip().split()
        aux=[]
        aux.append(cont[0])
        aux.append(cont[2])
        
        tab.append(aux)

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
      
          texte = word_tokenize(texte)
          
          fdist = FreqDist()
          for mot in texte:
            if mot.lower() not in stopW:
              fdist[mot.lower()] += 1
          donnees[docno] = {"texte":fdist}

  return donnees
          
           

     
