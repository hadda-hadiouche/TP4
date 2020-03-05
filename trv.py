DATA_FILE = 'D:/tpMTI/tp4/t/tp.xml'
import xml.dom.minidom as minidom
import sys
#********************** moyenne ****************************************************************
def calcule (x,y) :
  mg=(x+y)/2
  return mg


#********************** resultat ****************************************************************
def result (x,y,z):
  if x>=10 and y>=10 :
    res="Admis"
  elif z>=45 :
    res="Admis avec dette"
  else :
    res="Ajourne"
  return res
  
 #---------------- affichage--------------------------------------
def treat_doc(xmldoc): 
  etudians = xmldoc.getElementsByTagName('etudians')[0]
  print (etudians)
  cpt = 0 
# display personne by personne
  for etudian in etudians.childNodes:
    print ("-"*40)
    print ("etudian n°",cpt)
    print (etudian.toxml())
    cpt+= 1
    #--------------myn-----
    
#---------------- trie-------------------
"""def treat_doc(xmldoc):
# get the annuaire list
  liste=[]
  admi=0
  dett =0
  ajou =0
  cid=0
  som=0
 s1 =etudian.getElementsByTagName('S1')[0]
    s2 = etudian.getElementsByTagName('S2')[0]
    mg =calcule(float(s1.firstChild.data),float(s2.firstChild.data))
    res=result(float(s1),float(s2),float(c))
    if res == "Admis":
      admi +=1
    elif res == "Admis avec dette":
      dett +=1
    else :
      ajou +=1
    som=som+mg"""
  mgenerale=xmldoc.createElement('Mgenerale')
  mtext=xmldoc.createTextNode(str(mg))
  mgenerale.appendChild(mtext)
  etudiant.appendChild(mgenerale)

#********************** MAIN ****************************************************************
def main():
  try:
    xmldoc = minidom.parse(DATA_FILE)
  except:
    print ("Can't Open the file")
    sys.exit()
  #print (xmldoc.toxml()) 
  treat_doc(xmldoc)  
  return 0
if __name__ == '__main__':
  main()

 