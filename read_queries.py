
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

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
        cont=ligne.strip().split()
        aux=[]
        aux.append(cont[0])
        aux.append(cont[2])
        
        tab.append(aux)

    return tab
