
from bs4 import BeautifulSoup


def corresTheme(nom_fichier,requete):
     with open(nom_fichier, 'r') as f:
          lignes = f.readlines() 
          tab=[]
          i=0
         
          
          for cle,fd in requete.items():
             
            total_req=0
            tab.append([cle])
            for  freq in fd.items():
                   
                   
                total_req+=freq[1]
            tab[i].append(total_req)
            i+=1
          print(total_req)


          return tab
          #for ligne in lignes:
             
