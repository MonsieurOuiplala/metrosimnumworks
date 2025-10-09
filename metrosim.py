version=0.5
try:from keyboard import *
except Exception:
	from ion import *
	def is_pressed(touche):
		touches={"v":"KEY_ONE","b":"KEY_TWO","n":"KEY_THREE","g":"KEY_FOUR","a":"KEY_EXP","up":"KEY_UP","down":"KEY_DOWN","p":"KEY_LEFTPARENTHESIS","c":"KEY_LOG","m":"KEY_SEVEN","o":"KEY_FIVE","f":"KEY_FIVE","echap":"KEY_SHIFT","enter":"KEY_EXE","d":"KEY_IMAGINARY","control":"KEY_ALPHA","backspace":"KEY_BACKSPACE","i":"KEY_TANGENT"}
		if touche in touches:return keydown(eval(touches[touche]))
from time import *
from kandinsky import *
from random import *
def BLANC():fill_rect(0,0,320,222,BlancC)
BlancC=(240,240,240)
VACMA=[False,0,0,0,True]

# Coordonnees espace restant : x40,y5

#---
# Personnaliser l'experience de conduite :
VitessePlus=0.05 # Puissange d'acceleration (normal = 0.05)
VitesseMoins=0.08 # Puissance de freinage (normal = 0.08)
Rame="286" # Numero de la rame
Agent="---" # Identifiant agent
#VACMA[4]=False # Enlever le premier croisillon (#) pour desactiver la VACMA
#---

print("Bienvenue sur Metro Simulator Numworks !")
sleep(1)
NomsArrets=["Abbesses","Adrienne Bolland","Aeroport d'Orly"] # Rentrer plus de stations prendrait trop de place, la Numworks a un espace de stockage tres limite
FU=False
#[Distance,DSO?,Nom]
prochainArret=[5,False,"Sortie du garage"]
#[Distance,Rouge?]
prochainFeu=[10,False]
#[Distance,Limite]
prochaineLimite=[10,50]
DefautOP=False
def Porte(PorteCouleur):fill_rect(155,50,10,10,PorteCouleur)
Limite=30
Vitesse=0
AEAU=[None,None,None,None,True]
Routes=[]
Aleatoire="0"
gris=(245,245,245) # Couleur grisee, pour afficheurs

def arriveeDistance(arriveeDistanceSimVitesse,arriveeDistanceDistance=0):
   for AffichageArriveeIteration in range(int(arriveeDistanceSimVitesse)):
   	arriveeDistanceSimVitesse-=VitesseMoins
   	arriveeDistanceDistance+=arriveeDistanceSimVitesse/24
   return arriveeDistanceDistance
  
def demarrerService():
	print("Service demarre a "+str(monotonic()))
	draw_string("Demarrer service",10,130,'green')
	sleep(1)
	draw_string("Demarrer service",10,130)
def finService():
	print("Service termine a "+str(monotonic()))
	draw_string("Fin service",10,155,'green')
	sleep(1)
	draw_string("Fin service",10,155)

def bienvenuMenu0Affichage():BienvenuePasserMenu("Service","Train","Bienvenue")
def rien():pass   
def bienvenueMenu0():bienvenueMenu(["Service",bienvenueMenuA,"Train",bienvenueMenuB,"Bienvenue",bienvenueMenuC],bienvenueMenuFonctionPassage=BienvenueAfficherMenu)
def bienvenueMenuA():bienvenueMenu(["Agent",rien,"Demarrer service",bienvenueMenuAB,"Fin service",bienvenueMenuAC])
def bienvenueMenuAB():bienvenueMenu(["",rien,"",rien,"",rien],bienvenueMenuFonctionPassage=BienvenueAfficherMenu,bienvenueMenuAuChargement=demarrerService)
def bienvenueMenuAC():bienvenueMenu(["",rien,"",rien,"",rien],bienvenueMenuFonctionPassage=BienvenueAfficherMenu,bienvenueMenuAuChargement=finService)
def bienvenueMenuB():bienvenueMenu(["Securites",bienvenueMenuBA,"Informations","",rien])
def bienvenueMenuBA():bienvenueMenu(["VACMA",BienvenueMenuSecurites("VACMA"),"AEAU",BienvenueMenuSecurites("AEAU"),"",rien])
def bienvenueMenuC():bienvenueMenu(["MSN v"+str(version),rien,"Technicentre",rien,"",rien])

class Afficheur():
	def __init__(self,afficheurX,afficheurY,afficheurTexteInitial="00",afficheurCouleurInitiale="black"):
		self.x=afficheurX
		self.y=afficheurY
		self.texte=afficheurTexteInitial
		self.longueur=len(str(self.texte))
		self.couleur=afficheurCouleurInitiale
		self.ecrire(self.texte)
	def ecrire(self,afficheurTexte=None):
		if afficheurTexte!=None:
			self.texte=afficheurTexte
			self.longueur=len(str(self.texte))
		draw_string(self.texte,self.x,self.y,self.couleur)
	def changerCouleur(self,afficheurCouleur):
		self.couleur=afficheurCouleur
		self.ecrire()
	def nettoyer(self,nettoyerCommencement=0):fill_rect(self.x+nettoyerCommencement*10,self.y,self.longueur*10,18,BlancC) # Caractère draw_string prend 10*18

class AfficheurModeConduite():
	def __init__(self,afficheurPAX,afficheurPAY,afficheurCMX,afficheurCMY,modeInitial=False): # Pour le mode, True est le PA et False la CM
		self.PA=Afficheur(afficheurPAX,afficheurPAY,"PA",)
		self.CM=Afficheur(afficheurCMX,afficheurCMY,"CM")
		self.mode=modeInitial
		if self.mode:self.CM.changerCouleur(gris)
		else:self.PA.changerCouleur(gris)
	def afficheurChangerMode(self,afficheurNouveauMode): # Ne change que l'afficheur, pas le mode reel
		if afficheurNouveauMode: # Si le mode de conduit voulu est le PA
			self.mode=True # Changer en PA
			self.PA.changerCouleur("black")
			self.CM.changerCouleur(gris)
		else: # Si le mode de conduite voulu est la CM
			self.mode=False # Changer en CM
			self.PA.changerCouleur(gris)
			self.CM.changerCouleur("black")
	def afficheurRaffraichir(self): # Raffraichir l'affichage du mode de conduite, notamment apres un arrêt en station
		self.PA.ecrire()
		self.CM.ecrire()

def BienvenuePasserMenu(BPMA,BPMB,BPMC):
  fill_rect(0,103,250,75,'white')
  sleep(0.3)
  BienvenueAfficherMenu(BPMA,BPMB,BPMC)
  sleep(0.1)
def BienvenueAfficherMenu(BienvenueAfficherMenuA,BienvenueAfficherMenuB,BienvenueAfficherMenuC):
  fill_rect(0,103,250,75,'white')
  draw_string(BienvenueAfficherMenuA,10,105)
  draw_string(BienvenueAfficherMenuB,10,130)
  draw_string(BienvenueAfficherMenuC,10,155)
  
  
toucheBienvenueMenuA="v"
toucheBienvenueMenuB="b"
toucheBienvenueMenuC="n"
toucheBienvenueMenuSortie="g"
def bienvenueMenu(bienvenueMenuMenu=["Erreur",rien,"Erreur",rien,"Erreur",rien],bienvenueMenuFonctionPassage=BienvenuePasserMenu,bienvenueMenuAuChargement=None): # bienvenueMenuAfficherA,bienvenueMenuActionA,bienvenueMenuAfficherB,bienvenueMenuActionB,bienvenueMenuAfficherC,bienvenueMenuActionC
	bienvenueMenuFonctionPassage(bienvenueMenuMenu[0],bienvenueMenuMenu[2],bienvenueMenuMenu[4])
	if bienvenueMenuAuChargement!=None:bienvenueMenuAuChargement()
	while not is_pressed("g"):
		if is_pressed(toucheBienvenueMenuA) or is_pressed(toucheBienvenueMenuB) or is_pressed(toucheBienvenueMenuC):
			if is_pressed(toucheBienvenueMenuA):bienvenueMenuMenu[1]()
			elif is_pressed(toucheBienvenueMenuB):bienvenueMenuMenu[3]()
			elif is_pressed(toucheBienvenueMenuC):bienvenueMenuMenu[5]()
			BienvenuePasserMenu(bienvenueMenuMenu[0],bienvenueMenuMenu[2],bienvenueMenuMenu[4])
def BienvenueMenuSecurites(BMSSecurite):
  BienvenuePasserMenu("A manip. avec prec.","Activer","Desactiver")
  while not is_pressed("g"):
    if is_pressed("b"):
      eval(BMSSecurite)[4]=False
      print("["+BMSSecurite+"] activee, "+str(monotonic()))
      draw_string("Activer",10,130,'green')
      sleep(1.2)
      draw_string("Activer",10,130,'black')
    elif is_pressed("n"):
      eval(BMSSecurite)[4]=False
      print("["+BMSSecurite+"] desactivee, "+str(monotonic()))
      draw_string("Desactiver",10,155,'green')
      sleep(1.2)
      draw_string("Desactiver",10,155,'black')
def PauseVoyant():
  fill_rect(0,0,6,15,'red')
  fill_rect(9,0,6,15,'red')
def DepauseVoyant():fill_rect(0,0,15,15,BlancC)

limiteAfficheur=Afficheur(75,30)
prochaineLimiteAfficheur=Afficheur(75,55,str(prochaineLimite[1]))
prochaineLimiteDistanceAfficheur=Afficheur(75,80,str(int(prochaineLimite[0])))
def raffraichirProchaineLimite():
	if prochaineLimite[1]>Limite:prochaineLimiteAfficheur.changerCouleur("red")
	else:prochaineLimiteAfficheur.changerCouleur("green")
	
prochainFeuDistanceAfficheur=Afficheur(10,60,str(int(prochainFeu[0])))
prochainArretDistanceAfficheur=Afficheur(260,60,str(int(prochainArret[0])))
abc=Afficheur(0,0,"ahhhhh")

prochainFeuLen=1
prochainArretLen=1
prochaineLimiteLen=6
Porte('red')
RouteOP=False
BLANC()
PA=False
i=0
Defaut=""
BienvenueAfficherMenu("Service","Train","Bienvenue")
afficheurModeConduite=AfficheurModeConduite(262,126,262,151,False)
while not is_pressed("backspace"):
  if int(Vitesse)<Limite:draw_string(str(int(Vitesse)),155,20)
  elif int(Vitesse)==Limite:draw_string(str(int(Vitesse)),155,20,'yellow')
  else:draw_string(str(int(Vitesse)),155,20,'red')
  if prochainFeu[1]:
    fill_rect(10,30,10,20,'red')
    fill_rect(20,30,10,20,'white')
  else:
    fill_rect(10,30,10,20,'white')
    fill_rect(20,30,10,20,'green')
  limiteAfficheur.ecrire(str(Limite)) 
  if is_pressed(toucheBienvenueMenuA) or is_pressed(toucheBienvenueMenuB) or is_pressed(toucheBienvenueMenuC):bienvenueMenu0()
  if is_pressed("a") and is_pressed("p"):
    if not PA:print("PA active, "+str(monotonic()))
    PA=True
    VACMA[4]=False
    afficheurModeConduite.afficheurChangerMode(True) # Afficher PA active
  elif is_pressed("c") and is_pressed("m"):
    if PA:print("PA desactive, "+str(monotonic()))
    PA=False
    VACMA[4]=True
    afficheurModeConduite.afficheurChangerMode(False) # Afficher PA desactive
  raffraichirProchaineLimite()
  prochaineLimiteDistanceAfficheur.ecrire(str(int(prochaineLimite[0])))
  if prochainArret[0]<100:
    if prochainArret[1]:
      fill_rect(270,30,8,8,'white')
      fill_rect(260,43,8,8,'white')
      fill_rect(280,43,8,8,'white')
    else:
      fill_rect(270,30,8,8,'black')
      fill_rect(260,43,8,8,'black')
      fill_rect(280,43,8,8,'black')
  else:fill_rect(260,30,28,21,BlancC)
  prochainArretDistanceAfficheur.ecrire(str(int(prochainArret[0])))
  prochainFeuDistanceAfficheur.ecrire(str(int(prochainFeu[0])))
  if is_pressed("o") and prochainArret[0]<20 and Vitesse<0.01:
    Porte('green')
    sleep(2)
    while not is_pressed("f"):
      if prochainArret[1] and randrange(0,20001)==0:
        fill_rect(270,30,8,8,'black')
        fill_rect(260,43,8,8,'black')
        fill_rect(280,43,8,8,'black')
    Porte('yellow')
    sleep(5)
    Porte('red')
    if RouteOP:
      Arret+=1
      prochainArret=RouteActuelle[Arret]
    BLANC()
    afficheurModeConduite.afficheurRaffraichir()
    print("Station, "+str(monotonic()))
    i=0
  if (is_pressed("down") and Vitesse>0) or (PA and ((prochainArret[0]<280 and Vitesse>40) or (prochainArret[0]<300 and Limite==70 and Vitesse>40) or int(320-prochainArret[0])+int(arriveeDistance(Vitesse))>=308 or (prochaineLimite[1]<Vitesse and prochaineLimite[0]<=(10*(Vitesse-prochaineLimite[1]))) or Vitesse>Limite+2*VitessePlus or prochainFeu[1])):Vitesse-=VitesseMoins
  elif is_pressed("up") or PA:
    if not DefautOP or (PA and Vitesse)<=Limite:Vitesse+=VitessePlus
    elif (PA==False and Defaut!="PE") or (Defaut!="PE" and (PA and Vitesse<=Limite-1)):Vitesse+=VitessePlus
  elif Vitesse>0.0001 and not PA:Vitesse-=0.0002
  if DefautOP and Defaut=="PE":Vitesse-=0.01
  prochainArret[0]-=Vitesse/155
  prochainFeu[0]-=Vitesse/155
  prochaineLimite[0]-=Vitesse/155
  if prochainArret[0]<0:prochainArret=[randrange(900,1600),choice([False,False,False,False,False,False,False,False,False,False,False,True]),""]
  if prochainFeu[0]<0:
    if prochainFeu[1] and AEAU[4]:
      FU=True
      print("[AEAU] FU active, "+str(monotonic()))
    prochainFeu=[randrange(330,500),choice([False,False,False,False,False,False,False,False,False,False,False,False,False,True])]
  if prochaineLimite[0]<0:
    Limite=prochaineLimite[1]
    prochaineLimite[1]=choice([40,50,60,70])
    prochaineLimite[0]=randrange(500,800+([40,50,60,70].index(prochaineLimite[1])*prochaineLimite[1]))
  if len(str(int(prochainFeu[0])))<prochainFeuLen:fill_rect(10,60,30,30,BlancC)
  prochainFeuLen=len(str(int(prochainFeu[0])))
  if len(str(int(prochaineLimite[0])))<prochaineLimiteLen:fill_rect(75,80,40,17,BlancC)
  prochaineLimiteLen=len(str(int(prochaineLimite[0])))
  if len(str(int(prochainArret[0])))<prochainArretLen:fill_rect(260,60,40,30,BlancC)
  prochainArretLen=len(str(int(prochainArret[0])))
  Porte('red')
  if not DefautOP and randrange(0,6001)==0:
    DefautOP=True
    #Panne Electrique
    Defaut=choice(["PE"])
  elif DefautOP and randrange(0,101)==0:DefautOP=False
  if prochainFeu[1] and randrange(0,1000)==0:prochainFeu[1]=False
  if prochainArret[0]<500 and prochainArret[0]>480:fill_rect(260,90,30,30,'red')
  if is_pressed("echap"):
    if not FU and not is_pressed("echap"):print("FU active manuellement, "+str(monotonic()))
    FU=True
  if FU and Vitesse>0.0845+VitesseMoins:Vitesse-=0.0846
  elif FU:Vitesse-=0.01
  if FU:draw_string("FU",152,80,'black')
  elif FU=="i":draw_string("VACMA",188,25,'blue')
  else:draw_string("FU",152,80,(245,245,245))
  if VACMA[0]:draw_string("VACMA",188,25,'red')
  else:
    if VACMA[4]:
      if Vitesse>0:draw_string("VACMA",188,25,'green')
      else:draw_string("VACMA",188,25,'black')
    elif VACMA[4]=="i":draw_string("VACMA",188,25,'blue')
    else:draw_string("VACMA",188,25,(245,245,245))
  if DefautOP:draw_string("Defaut",185,10,'orange')
  elif DefautOP=="i":draw_string("VACMA",188,25,'blue')
  else:draw_string("Defaut",185,10,(245,245,245))
  if FU and is_pressed("echap") and is_pressed("enter"):FU=False
  if prochainArret[0]<321:
    fill_rect(0,180,320,40,'white')
    fill_rect(0,190,int(320-prochainArret[0]),30,'blue')
    fill_rect(int(320-prochainArret[0])+int(arriveeDistance(Vitesse)),190,4,30,'orange')
    fill_rect(302,220,19,2,'green')
    fill_rect(0,220,302,2,'red')
  if is_pressed("a") and is_pressed("d"):
    Commande=input("Commande ? ")
    if Commande=="CreaCarte":
      print("Entree en mode creation de carte...\nPressez BAKSPACE pour quitter et enregistrer")
      sleep(2)
      DistanceCreaCarte=0
      VitesseCreaCarte=0
      CreaCarteCarte=[]
      while not is_pressed("backspace"):
        if is_pressed("down") and VitesseCreaCarte>0:VitesseCreaCarte-=0.04
        elif is_pressed("up"):VitesseCreaCarte+=0.012
        elif VitesseCreaCarte>0.0001:VitesseCreaCarte-=0.0002
        draw_string(str(VitesseCreaCarte),0,0)
        draw_string(str(DistanceCreaCarte),0,30)
        DistanceCreaCarte+=VitesseCreaCarte/160
        if is_pressed("o"):
          CreaCarteCarte.append(int(DistanceCreaCarte))
          print(DistanceCreaCarte)
          DistanceCreaCarte=0
          sleep(0.5)
          while not is_pressed("f"):pass
          sleep(1)
        if VitesseCreaCarte<0:Vitesse=0
      print(CreaCarteCarte)
      BLANC()
    elif Commande[0]=="R":
      RouteActuelleNom=Routes[int(Commande[1]+Commande[2])][0]
      RouteActuelle=Routes[int(Commande[1]+Commande[2])]
      del RouteActuelle[0]
      print("Demarrage du service : \n"+RouteActuelleNom)
      sleep(2)
      RouteOP=True
      prochainArret[0]=RouteActuelle[0]
      Arret=0
      BLANC()
    elif Commande=="AppendRoute":Routes.append(eval(input("AppendRoute ? ")))
    elif Commande=="def":exec(input("def eval ")+"="+input("def def eval "))
    elif Commande=="exec":exec(input("exec "))
    elif Commande=="TestPA0":
      PA=True
      Vitesse=70
      Limite=70
      prochainArret[0]=10000
      prochainFeu[0]=10000
      prochaineLimite=[400,40]
    elif Commande=="TestPA1":
      PA=True
      Vitesse=70
      Limite=70
      VACMA[4]=False
      prochainArret[0]=700
      prochainFeu[0]=10000
      prochaineLimite[0]=10000
  if Vitesse>0.1 and VACMA[4]:
    if is_pressed("control"):
      VACMA[1]+=1
      VACMA[2]=0
    else:
      VACMA[1]=0
      VACMA[2]+=1
  else:
    VACMA[1]=0
    VACMA[2]=0
  if VACMA[1]>99 or VACMA[2]>999:
    VACMA[0]=True
  else:VACMA[0]=False
  if VACMA[0]:VACMA[3]+=1
  else:VACMA[3]=0
  if VACMA[3]==150:
    FU=True
    print("[VACMA] FU active, "+str(monotonic()))
  if VACMA[0] or DefautOP:fill_rect(0,0,20,20,'red')
  else:fill_rect(0,0,20,20,BlancC)
  if str(Vitesse)[0]=="-":Vitesse=0
  if Vitesse>=71:
    if not FU:print("FU active, vitesse > 70, "+str(monotonic()))
    FU=True
  if prochainArret[0]>=330:
    fill_rect(0,180,320,40,'white')
    fill_rect(0,190,20,30,'blue')
    fill_rect(0,220,320,2,'red')
    if prochainFeu[0]<185:
      if prochainFeu[1]:fill_rect(int((15+prochainFeu[0])*2.5),190,10,10,'red')
      else:fill_rect(int((15+prochainFeu[0])*2.5),190,10,10,'green')
    if prochaineLimite[0]<330:draw_string(str(prochaineLimite[1]),int((15+prochaineLimite[0])*2.5),200)
    if prochainArret[0]<515:
      fill_rect(int((prochainArret[0]-320)*2.5),217,300,10,'black')
      draw_string(prochainArret[2],int((prochainArret[0]-300)*2.5),198)
  elif prochainArret[0]>322:fill_rect(0,180,320,40,BlancC)
  if is_pressed("i"):i=0
  Aleatoire=str(randrange(0,1000))
