version=0.9
try:from keyboard import *
except Exception:
	from ion import *
	def is_pressed(touche):
		touches={"a":"KEY_EXP","up":"KEY_UP","down":"KEY_DOWN","left":"KEY_LEFT","right":"KEY_RIGHT","p":"KEY_LEFTPARENTHESIS","c":"KEY_LOG","m":"KEY_SEVEN","o":"KEY_FIVE","f":"KEY_FIVE","esc":"KEY_SHIFT","enter":"KEY_EXE","d":"KEY_IMAGINARY","control":"KEY_ALPHA","backspace":"KEY_BACKSPACE","i":"KEY_TANGENT"}
		if touche in touches:return keydown(eval(touches[touche]))
from time import *
from kandinsky import *
from random import *
BLANCC=(240,240,240)
def BLANC():fill_rect(0,0,320,222,BLANCC)
VACMA=[False,0,0,0,True]

# Ecran : 320*222px

#---
# Personnaliser l'experience de conduite :
vitessePlus=0.05 # Puissange d'acceleration (normal = 0.05)
vitesseMoins=0.08 # Puissance de freinage (normal = 0.08)
Rame="286" # Numero de la rame
Agent="---" # Identifiant agent
#VACMA[4]=False # Enlever le premier croisillon (#) pour desactiver la VACMA
#---

print("Bienvenue sur Metro Simulator Numworks !")
sleep(1)
NomsArrets=["Abbesses","Adrienne Bolland","Aeroport d'Orly"]
FU=False
#[Distance,DSO?,Nom]
prochainArret=[5,False,"Sortie du garage"]
#[Distance,Rouge?]
prochainFeu=[10,False]
#[Distance,Limite]
prochaineLimiteVitesse=[10,50]
DefautOP=False
def PorteCarre(PorteCouleur):fill_rect(155,50,10,10,PorteCouleur)
limiteVitesse=30
vitesse=0
AEAU=[None,None,None,None,True]
ouverturePortesDifferee=0
GRIS=(245,245,245) # Couleur grisee, pour afficheurs

def arretDistance(arretDistanceSimVitesse,arretDistanceDistance=0):
   for AffichageArriveeIteration in range(int(arretDistanceSimVitesse)):
   	arretDistanceSimVitesse-=vitesseMoins
   	arretDistanceDistance+=arretDistanceSimVitesse/24
   return arretDistanceDistance
   
# Peut etre utilise pour simuler du trafic, plus la probabilite d'obtenir True est elevee plus il y aura de DSO, signaux fermes...
def faibleChance():return choice([False,False,False,False,False,False,False,False,False,False,False,True])

class Afficheur():
	def __init__(self,afficheurX,afficheurY,afficheurTexteInitial="00",afficheurCouleurInitiale="black",afficheurCouleurFondInitiale=(248,252,248)):
		self.x=afficheurX
		self.y=afficheurY
		self.texte=afficheurTexteInitial
		self.longueur=len(str(self.texte))
		self.couleur=afficheurCouleurInitiale
		self.couleurFond=afficheurCouleurFondInitiale
		self.ecrire(self.texte)
	def ecrire(self,afficheurTexte=None,nettoyer=True,nettoyerCouleur=BLANCC,ecrireCouleur=None,ecrireCouleurFond=None):
		if ecrireCouleur!=None:self.couleur=ecrireCouleur
		if ecrireCouleurFond!=None:self.couleurFond=ecrireCouleurFond
		if nettoyer and afficheurTexte!=None and self.longueur>len(afficheurTexte):self.nettoyer(nettoyerCouleur=nettoyerCouleur)
		if afficheurTexte!=None:
			self.texte=afficheurTexte
			self.longueur=len(self.texte)
		draw_string(self.texte,self.x,self.y,self.couleur,self.couleurFond)
	def changerCouleur(self,afficheurCouleur):
		self.couleur=afficheurCouleur
		self.ecrire()
	def nettoyer(self,nettoyerCommencement=0,nettoyerCouleur=BLANCC):fill_rect(self.x+nettoyerCommencement*10,self.y,self.longueur*10,18,BLANCC) # Caractere draw_string prend 10*18

class AfficheurModeConduite():
	def __init__(self,afficheurPAX,afficheurPAY,afficheurCMX,afficheurCMY,modeInitial=False): # Pour le mode, True est le PA et False la CM
		self.PA=Afficheur(afficheurPAX,afficheurPAY,"PA",)
		self.CM=Afficheur(afficheurCMX,afficheurCMY,"CM")
		self.mode=modeInitial
		if self.mode:self.CM.changerCouleur(GRIS)
		else:self.PA.changerCouleur(GRIS)
	def afficheurChangerMode(self,afficheurNouveauMode): # Ne change que l'afficheur, pas le mode reel
		if afficheurNouveauMode: # Si le mode de conduite voulu est le PA
			self.mode=True # Changer en PA
			self.PA.changerCouleur("black")
			self.CM.changerCouleur(GRIS)
		else: # Si le mode de conduite voulu est la CM
			self.mode=False # Changer en CM
			self.PA.changerCouleur(GRIS)
			self.CM.changerCouleur("black")
	def afficheurRaffraichir(self): # Raffraichir l'affichage du mode de conduite, notamment apres un arrêt en station
		self.PA.ecrire()
		self.CM.ecrire()
		
class AfficheurVitesse():
	def __init__(self,afficheurX,afficheurY):self.afficheur=Afficheur(afficheurX,afficheurY)
	def raffraichir(self):
		vitesseEcrire=str(int(vitesse))
		if vitesse<limiteVitesse:self.afficheur.ecrire(vitesseEcrire,ecrireCouleur="black")
		elif int(vitesse)==limiteVitesse:self.afficheur.ecrire(vitesseEcrire,ecrireCouleur="yellow")
		else:self.afficheur.ecrire(vitesseEcrire,ecrireCouleur="red")
		
portesX=30 # Coordonnées derniere porte
portesY=195
portesCouleurInterieur="white"
portesCouleurExterieur="blue"
def porteOuvrir(deplacement,ouverture):
	fill_rect(portesX+deplacement-int(ouverture/2),portesY,int(ouverture),20,portesCouleurInterieur)
def portesOuvrir():
	ouverture=0
	for i in range(1100):
		ouverture+=0.02
		for j in range(0,241,40):porteOuvrir(j,ouverture)
def porteAvertisseur(deplacement):fill_rect(portesX+deplacement-3,portesY,6,6,"red")
def portesAvertisseur():
	for i in range(0,241,40):porteAvertisseur(i)
def porteFermer(deplacement,fermeture):
	fill_rect(portesX+deplacement-11,portesY,int(fermeture/2),20,portesCouleurExterieur)
	fill_rect(portesX+deplacement+11-int(fermeture/2),portesY,11,20,portesCouleurExterieur)
def portesFermer():
	fermeture=0
	for i in range(600):
		fermeture+=0.04
		for j in range(0,241,40):porteFermer(j,fermeture)
		
def PauseVoyant():
  fill_rect(0,0,6,15,'red')
  fill_rect(9,0,6,15,'red')
def DepauseVoyant():fill_rect(0,0,15,15,BLANCC)

cranManipulateur=0 # Cran du manipulateur : multiplicateur de traction/freinage minimum -1 (freinage), maximum 1 (traction)
xManipulateur=210
yManipulateur=130
def raffraichirManipulateur(cran):
	multiplicateurTaille=24
	fill_rect(xManipulateur,yManipulateur-multiplicateurTaille,35,multiplicateurTaille*2+10,BLANCC)
	fill_rect(xManipulateur,yManipulateur,20,10,"black")
	taille=int(abs(cran)*multiplicateurTaille)
	if cran>=0:
		fill_rect(xManipulateur+5,yManipulateur-taille,10,taille+10,"grey")
		fill_rect(xManipulateur+5,yManipulateur-taille,30,10,"black")
	else:
		fill_rect(xManipulateur+5,yManipulateur+10,10,taille,"gray")
		fill_rect(xManipulateur+5,yManipulateur+taille,30,10,"black")
	

# Ecran Octys VB2
limiteVitesseAfficheur=Afficheur(150,100,afficheurCouleurInitiale="green",afficheurCouleurFondInitiale="blue")
couleurFondVB2=(230,230,230)
def initialiserAffichageVB2():
	fill_rect(limiteVitesseAfficheur.x-35,limiteVitesseAfficheur.y-15,90,80,couleurFondVB2)
	fill_rect(limiteVitesseAfficheur.x-33,limiteVitesseAfficheur.y-13,86,76,"blue")
	fill_rect(limiteVitesseAfficheur.x-32,limiteVitesseAfficheur.y-12,84,74,couleurFondVB2)
	fill_rect(limiteVitesseAfficheur.x-5,limiteVitesseAfficheur.y-5,30,28,"green")
	fill_rect(limiteVitesseAfficheur.x-28,limiteVitesseAfficheur.y+28,76,10,"black")
	raffraichirVB2("00",0)
	raffraichirPortesVB2("green")
def raffraichirVB2(limiteAfficher,vitesseAfficher):
	limiteVitesseAfficheur.ecrire(limiteAfficher)
	vitesseAfficher=int(vitesseAfficher)
	fill_rect(limiteVitesseAfficheur.x-26,limiteVitesseAfficheur.y+30,int(0.9*vitesseAfficher),6,"green")
	fill_rect(limiteVitesseAfficheur.x-26+int(0.9*vitesseAfficher),limiteVitesseAfficheur.y+30,72-int(0.9*vitesseAfficher),6,couleurFondVB2)
def raffraichirPortesVB2(couleur):
	fill_rect(limiteVitesseAfficheur.x+32,limiteVitesseAfficheur.y+42,20,20,couleur)
	draw_string("D",limiteVitesseAfficheur.x+37,limiteVitesseAfficheur.y+43,"black",couleur)
	
prochaineLimiteVitesseAfficheur=Afficheur(110,50,str(prochaineLimiteVitesse[1]))
prochaineLimiteVitesseDistanceAfficheur=Afficheur(110,25,str(int(prochaineLimiteVitesse[0])))
def raffraichirProchaineLimiteVitesse():
	if prochaineLimiteVitesse[1]<limiteVitesse:prochaineLimiteVitesseAfficheur.changerCouleur("red")
	else:prochaineLimiteVitesseAfficheur.changerCouleur("green")
	
prochainFeuDistanceAfficheur=Afficheur(10,50,str(int(prochainFeu[0])))
prochainArretDistanceAfficheur=Afficheur(260,60,str(int(prochainArret[0])))

vitesseAfficheur=AfficheurVitesse(155,20)
fuAfficheur=Afficheur(200,50,afficheurCouleurInitiale=GRIS,afficheurTexteInitial="FU")
vacmaAfficheur=Afficheur(188,25,afficheurTexteInitial="VACMA")
defautAfficheur=Afficheur(185,10,afficheurTexteInitial="Defaut")

PorteCarre('red')
BLANC()
PA=False
Defaut=""
afficheurModeConduite=AfficheurModeConduite(60,25,60,50,False)
fill_rect(0,180,320,40,'white')
initialiserAffichageVB2()
raffraichirManipulateur(cranManipulateur)
while not is_pressed("backspace"):
  vitesseAfficheur.raffraichir()
  if prochainFeu[1]:
    fill_rect(10,20,10,20,'red')
    fill_rect(20,20,10,20,'white')
  else:
    fill_rect(10,20,10,20,'white')
    fill_rect(20,20,10,20,'green')
  raffraichirVB2(str(limiteVitesse),vitesse)
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
  raffraichirProchaineLimiteVitesse()
  prochaineLimiteVitesseAfficheur.ecrire(str(prochaineLimiteVitesse[1]))
  prochaineLimiteVitesseDistanceAfficheur.ecrire(str(int(prochaineLimiteVitesse[0])))
  if prochainArret[0]<100:
    if is_pressed("o"):ouverturePortesDifferee=200
    else:ouverturePortesDifferee-=1
    if prochainArret[1]:
      fill_rect(270,30,8,8,'white')
      fill_rect(260,43,8,8,'white')
      fill_rect(280,43,8,8,'white')
    else:
      fill_rect(270,30,8,8,'black')
      fill_rect(260,43,8,8,'black')
      fill_rect(280,43,8,8,'black')
  else:fill_rect(260,30,28,21,BLANCC)
  prochainArretDistanceAfficheur.ecrire(str(int(prochainArret[0])))
  prochainFeuDistanceAfficheur.ecrire(str(int(prochainFeu[0])))
  if ouverturePortesDifferee>0 and prochainArret[0]<20 and vitesse<0.01:
    PorteCarre('green')
    raffraichirPortesVB2("yellow")
    sleep(0.5)
    portesOuvrir()
    while not is_pressed("f"):
      if prochainArret[1] and randrange(0,80000)==0:
        fill_rect(270,30,8,8,'black')
        fill_rect(260,43,8,8,'black')
        fill_rect(280,43,8,8,'black')
    PorteCarre('yellow')
    portesAvertisseur()
    sleep(2)
    portesFermer()
    sleep(1)
    PorteCarre('red')
    afficheurModeConduite.afficheurRaffraichir()
    print("Station, "+str(monotonic()))
    prochainArret[0]=-1
  if is_pressed("up") or is_pressed("down") or is_pressed("left") or is_pressed("right"):
  	if is_pressed("up") and int(cranManipulateur)<1:cranManipulateur+=0.1
  	elif is_pressed("down") and cranManipulateur>-1:cranManipulateur-=0.1
  	elif is_pressed("left"):cranManipulateur=-1
  	elif is_pressed("right"):cranManipulateur=0
  	if cranManipulateur<-1:cranManipulateur=-1
  	elif cranManipulateur>1:cranManipulateur=1
  	raffraichirManipulateur(cranManipulateur)
  if not FU and(not PA and cranManipulateur<0 and vitesse>0) or PA and (int(320-prochainArret[0])+int(arretDistance(vitesse))>=308 or (prochainFeu[1] and prochainFeu[0]-arretDistance(vitesse)<8) or (prochaineLimiteVitesse[1]<vitesse and prochaineLimiteVitesse[0]<=(10*(vitesse-prochaineLimiteVitesse[1])) or vitesse>limiteVitesse+2*vitessePlus)):
  	if PA:vitesse-=vitesseMoins
  	else:vitesse-=vitesseMoins*-cranManipulateur
  elif not FU and(not PA and cranManipulateur>0 or PA):
    if not DefautOP or (PA and vitesse) or (PA==False and Defaut!="PE") or (Defaut!="PE" and (PA and vitesse<=limiteVitesse-1))<=limiteVitesse:
    	if PA:vitesse+=vitessePlus
    	else:vitesse+=vitessePlus*cranManipulateur
  elif vitesse>0.0001 and not PA:vitesse-=0.0002
  if DefautOP and Defaut=="PE":vitesse-=0.01
  prochainArret[0]-=vitesse/155
  prochainFeu[0]-=vitesse/155
  prochaineLimiteVitesse[0]-=vitesse/155
  if prochainArret[0]<0:
  	prochainArret=[randrange(900,1600),faibleChance(),""]
  	initialiserAffichageVB2()
  	fill_rect(20,180,320,40,'white')
  if prochainFeu[0]<0:
    if prochainFeu[1] and AEAU[4]:
      FU=True
      print("[AEAU] FU active, "+str(monotonic()))
    if prochainArret[0]<580 and prochainArret[0]>500:prochainFeu=[prochainArret[0]-340,faibleChance()]
    elif prochainArret[0]<=550:prochainFeu=[prochainArret[0]+10,faibleChance()]
    else:prochainFeu=[randrange(150,250),faibleChance()]
  if prochaineLimiteVitesse[0]<0:
    limiteVitesse=prochaineLimiteVitesse[1]
    prochaineLimiteVitesse[1]=choice([40,50,60,70])
    prochaineLimiteVitesse[0]=randrange(500,800+([40,50,60,70].index(prochaineLimiteVitesse[1])*prochaineLimiteVitesse[1]))
  PorteCarre('red')
  if not DefautOP and randrange(0,6001)==0:
    DefautOP=True
    #Panne Electrique
    Defaut=choice(["PE"])
  elif DefautOP and randrange(0,101)==0:DefautOP=False
  if prochainFeu[1] and randrange(0,1000)==0:prochainFeu[1]=False
  if prochainArret[0]<500 and prochainArret[0]>480:fill_rect(260,90,30,30,'red')
  if is_pressed("esc"):
    if not FU and not is_pressed("esc"):print("FU active manuellement, "+str(monotonic()))
    FU=True
  if FU:vitesse-=(vitesseMoins*1.4)
  if FU:fuAfficheur.changerCouleur("black")
  else:fuAfficheur.changerCouleur(GRIS)
  if VACMA[0]:vacmaAfficheur.changerCouleur("red")
  else:
    if VACMA[4]:
      if vitesse>0:vacmaAfficheur.changerCouleur("green")
      else:vacmaAfficheur.changerCouleur("black")
    else:vacmaAfficheur.changerCouleur(GRIS)
  if DefautOP:defautAfficheur.changerCouleur("orange")
  else:defautAfficheur.changerCouleur(GRIS)
  if FU and is_pressed("esc") and is_pressed("enter"):FU=False
  if prochainArret[0]<330:
    prochainArretDistance=arretDistance(vitesse)
    if prochainArret[0]>320:fill_rect(0,180,320,40,'white')
    fill_rect(0,190,int(320-prochainArret[0]),30,'blue')
    if vitesse>8:fill_rect(int(320-prochainArret[0])+int(prochainArretDistance)-4,190,4,30,'white')
    fill_rect(int(320-prochainArret[0])+int(prochainArretDistance)+6,190,2,30,'white')
    fill_rect(int(320-prochainArret[0])+int(prochainArretDistance),190,4,30,'orange')
    fill_rect(302,220,19,2,'green')
    fill_rect(0,220,302,2,'red')
  if is_pressed("a") and is_pressed("d"):
    Commande=input("Commande ? ")
    if Commande=="def":exec(input("def eval ")+"="+input("def def eval "))
    elif Commande=="exec":exec(input("exec "))
    elif Commande=="ProchainFeuFerme":prochainFeu[1]=True
  if vitesse>0.1 and VACMA[4]:
    if is_pressed("control"):
      VACMA[1]+=1
      VACMA[2]=0
    else:
      VACMA[1]=0
      VACMA[2]+=1
  else:
    VACMA[1]=0
    VACMA[2]=0
  if VACMA[1]>99 or VACMA[2]>399:
    VACMA[0]=True
  else:VACMA[0]=False
  if VACMA[0]:VACMA[3]+=1
  else:VACMA[3]=0
  if VACMA[3]==150:
    FU=True
    print("[VACMA] FU active, "+str(monotonic()))
  if str(vitesse)[0]=="-":vitesse=0
  if vitesse>=71:
    if not FU:print("FU active, vitesse > 70, "+str(monotonic()))
    FU=True
  if prochainArret[0]>=330:
    #fill_rect(20,180,320,40,'white')
    fill_rect(0,190,20,30,'blue')
    fill_rect(0,220,320,2,'red')
    if prochainFeu[0]<130:
      if prochainFeu[1]:fill_rect(int((8+prochainFeu[0])*2.5),190,10,10,'red')
      else:fill_rect(int((8+prochainFeu[0])*2.5),190,10,10,'green')
      fill_rect(10+int((8+prochainFeu[0])*2.5),190,10,10,"white") # Effacer les anciens signaux
    else:fill_rect(20,190,10,10,"white")
    if prochaineLimiteVitesse[0]<330:
    	draw_string(str(prochaineLimiteVitesse[1]),int((8+prochaineLimiteVitesse[0])*2.5),200)
    	fill_rect(20+int((8+prochaineLimiteVitesse[0])*2.5),200,20,18,"white") # Effacer les anciens TIV
    else:fill_rect(20,200,20,18,"white")
    if prochainArret[0]<515:
      fill_rect(int((prochainArret[0]-320)*2.5),217,300,10,'black')
      draw_string(prochainArret[2],int((prochainArret[0]-300)*2.5),198)
    fill_rect(0,190,20,30,'blue')
  elif prochainArret[0]>322:fill_rect(0,180,320,40,BLANCC)
