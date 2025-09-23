version=0.3
from ion import *
from time import *
from kandinsky import *
from random import *
def BLANC():fill_rect(0,0,320,222,BlancC)
BlancC=(240,240,240)
VACMA=[False,0,0,0,True]
#---
# Personnaliser l'experience de conduite :
VitessePlus=0.005 # Puissange d'acceleration (normal = 0.022)
VitesseMoins=0.08 # Puissance de freinage (normal = 0.04)
Rame="286" # Numero de la rame
Agent="---" # Identifiant agent
#VACMA[4]=False # Enlever le premier diese (#) pour desactiver la VACMA
#---
print("Bienvenue sur Metro Simulator Numworks !")
sleep(1) #0.2
NomsArrets=["Abbesses","Adrienne Bolland","Aeroport d'Orly","Aime Cesaire","Alesia","Alexandra David-Neel","Alexandre Dumas","Alma-Marceau","Anatole France","Angelique Compoint","Anna de Noailles","Anny Flore","Antony"]
FU=False
#[Distance,DSO?,Nom]
ProchainArret=[5,False,"Sortie du garage"]
#[Distance,Rouge?]
ProchainFeu=[10,False]
#[Distance,Limite]
ProchaineLimite=[10,50]
DefautOP=False
def Porte(PorteCouleur):fill_rect(155,50,10,10,PorteCouleur)
Limite=30
Vitesse=0
AEAU=[None,None,None,None,True]
Routes=[]
Aleatoire="0"
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
def BienvenueMenuA():BienvenuePasserMenu("Service","Train","Bienvenue")
def BienvenueMenuSecurites(BMSSecurite):
  BienvenuePasserMenu("A manip. avec prec.","Activer","Desactiver")
  while not keydown(KEY_FOUR):
    if keydown(KEY_TWO):
      eval(BMSSecurite)[4]=False
      print("["+BMSSecurite+"] activee, "+str(monotonic()))
      draw_string("Activer",10,130,'green')
      sleep(1.2)
      draw_string("Activer",10,130,'black')
    elif keydown(KEY_THREE):
      eval(BMSSecurite)[4]=False
      print("["+BMSSecurite+"] desactivee, "+str(monotonic()))
      draw_string("Desactiver",10,155,'green')
      sleep(1.2)
      draw_string("Desactiver",10,155,'black')
def PauseVoyant():
  fill_rect(0,0,6,15,'red')
  fill_rect(9,0,6,15,'red')
def DepauseVoyant():fill_rect(0,0,15,15,BlancC)

ProchainFeuLen=1
ProchainArretLen=1
ProchaineLimiteLen=6
Porte('red')
RouteOP=False
BLANC()
draw_string("PA",262,126,(245,245,245))
draw_string("CM",262,151)
PA=False
i=0
while not keydown(KEY_BACKSPACE):
  if int(Vitesse)<Limite:draw_string(str(int(Vitesse)),155,20)
  elif int(Vitesse)==Limite:draw_string(str(int(Vitesse)),155,20,'yellow')
  else:draw_string(str(int(Vitesse)),155,20,'red')
  if ProchainFeu[1]:
    fill_rect(10,30,10,20,'red')
    fill_rect(20,30,10,20,'white')
  else:
    fill_rect(10,30,10,20,'white')
    fill_rect(20,30,10,20,'green')
  draw_string(str(Limite),75,30)
#Tablette Bienvenue
  if keydown(KEY_SIX) and (keydown(KEY_ONE) or keydown(KEY_TWO) or keydown(KEY_THREE)):
    BienvenueMenuA()
    while not keydown(KEY_FOUR):
      if keydown(KEY_ONE):
        BienvenuePasserMenu("Agent","Demarrer service","Fin service")
        while not keydown(KEY_FOUR):
          if keydown(KEY_ONE):
            BienvenuePasserMenu("Connexion","Deconnexion",Agent)
            while not keydown(KEY_FOUR):pass
            BienvenuePasserMenu("Agent","Demarrer service","Fin service")
          elif keydown(KEY_TWO):
            print("Service demarre a "+str(monotonic()))
            draw_string("Demarrer service",10,130,'green')
            sleep(1)
            BienvenuePasserMenu("Agent","Demarrer service","Fin service")
          elif keydown(KEY_THREE):
            print("Service termine a "+str(monotonic()))
            draw_string("Fin service",10,155,'green')
            sleep(1)
            BienvenuePasserMenu("Agent","Demarrer service","Fin service")
        BienvenueMenuA()
      elif keydown(KEY_TWO):
        BienvenuePasserMenu("Securites","Informations","Electronique embarquee")
        while not keydown(KEY_FOUR):
          if keydown(KEY_ONE):
            BienvenuePasserMenu("VACMA","AEAU","")
            while not keydown(KEY_FOUR):
              if keydown(KEY_ONE):BienvenueMenuSecurites("VACMA")
              elif keydown(KEY_TWO):BienvenueMenuSecurites("AEAU")
        BienvenueMenuA()
      elif keydown(KEY_THREE):
        BienvenuePasserMenu("Metro Simulator Numworks","Redemarrer la simulation","version "+str(version))
        while not keydown(KEY_FOUR):pass
        BienvenuePasserMenu("Service","Train","Bienvenue")
  if keydown(KEY_EXP) and keydown(KEY_LEFTPARENTHESIS):
    if not PA:print("PA active, "+str(monotonic()))
    PA=True
    VACMA[4]=False
    draw_string("PA",262,126)
    draw_string("CM",262,151,(245,245,245))
  elif keydown(KEY_LOG) and keydown(KEY_SEVEN):
    if PA:print("PA desactive, "+str(monotonic()))
    PA=False
    VACMA[4]=True
    draw_string("PA",262,126,(245,245,245))
    draw_string("CM",262,151)
  if ProchaineLimite[1]<Limite:draw_string(str(ProchaineLimite[1]),75,55,'red')
  else:draw_string(str(ProchaineLimite[1]),75,55,'green')
  draw_string(str(int(ProchaineLimite[0])),75,80)
  if ProchainArret[0]<100:
    if ProchainArret[1]:
      fill_rect(270,30,8,8,'white')
      fill_rect(260,43,8,8,'white')
      fill_rect(280,43,8,8,'white')
    else:
      fill_rect(270,30,8,8,'black')
      fill_rect(260,43,8,8,'black')
      fill_rect(280,43,8,8,'black')
  else:fill_rect(260,30,28,21,BlancC)
  draw_string(str(int(ProchainArret[0])),260,60)
  draw_string(str(int(ProchainFeu[0])),10,60)
  if keydown(KEY_FIVE) and ProchainArret[0]<20 and Vitesse<0.01:
    Porte('green')
    sleep(2)
    while not keydown(KEY_FIVE):
      if ProchainArret[1] and randrange(0,20001)==0:
        fill_rect(270,30,8,8,'black')
        fill_rect(260,43,8,8,'black')
        fill_rect(280,43,8,8,'black')
    Porte('yellow')
    sleep(5)
    Porte('red')
    ProchainArret=[randrange(900,1600),choice([False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True])]
    if RouteOP:
      Arret+=1
      ProchainArret=RouteActuelle[Arret]
    BLANC()
    print("Station, "+str(monotonic()))
    i=0
  if (keydown(KEY_DOWN) and Vitesse>0) or (PA and ((ProchainArret[0]<335 and Vitesse>40) or (ProchainArret[0]<430 and Limite==70 and Vitesse>40) or ProchainArret[0]<=137 or (ProchaineLimite[1]<Vitesse and ProchaineLimite[0]<=(10*(Vitesse-ProchaineLimite[1]))) or Vitesse>Limite+2*VitessePlus or ProchainFeu[1])):Vitesse-=VitesseMoins
  elif keydown(KEY_UP) or PA:
    if not DefautOP or (PA and Vitesse)<=Limite:Vitesse+=VitessePlus
    elif (PA==False and Defaut!="PE") or (Defaut!="PE" and (PA and Vitesse<=Limite-1)):Vitesse+=VitessePlus
  elif Vitesse>0.0001 and not PA:Vitesse-=0.0002
  if DefautOP and Defaut=="PE":Vitesse-=0.01
  ProchainArret[0]-=Vitesse/155
  ProchainFeu[0]-=Vitesse/155
  ProchaineLimite[0]-=Vitesse/155
  if ProchainArret[0]<0:ProchainArret=[randrange(900,1600),choice([False,False,False,False,False,False,False,False,False,False,False,True])]
  if ProchainFeu[0]<0:
    if ProchainFeu[1] and AEAU[4]:
      FU=True
      print("[AEAU] FU active, "+str(monotonic()))
    ProchainFeu=[randrange(330,500),choice([False,False,False,False,False,False,False,False,False,False,False,False,False,True])]
    if ProchainFeu[0] and PA:print("[PA] Feu rouge detecte.")
  if ProchaineLimite[0]<0:
    Limite=ProchaineLimite[1]
    ProchaineLimite[1]=choice([40,50,60,70])
    ProchaineLimite[0]=randrange(500,800+([40,50,60,70].index(ProchaineLimite[1])*ProchaineLimite[1]))
    if ProchaineLimite[1] and PA:print("[VACMA] Feu rouge detecte.")
  if len(str(int(ProchainFeu[0])))<ProchainFeuLen:fill_rect(10,60,30,30,BlancC)
  ProchainFeuLen=len(str(int(ProchainFeu[0])))
  if len(str(int(ProchaineLimite[0])))<ProchaineLimiteLen:fill_rect(75,80,40,17,BlancC)
  ProchaineLimiteLen=len(str(int(ProchaineLimite[0])))
  if len(str(int(ProchainArret[0])))<ProchainArretLen:fill_rect(260,60,40,30,BlancC)
  ProchainArretLen=len(str(int(ProchainArret[0])))
  Porte('red')
  if not DefautOP and randrange(0,6001)==0:
    DefautOP=True
    #Panne Electrique
    Defaut=choice(["PE"])
  elif DefautOP and randrange(0,101)==0:DefautOP=False
  if ProchainFeu[1] and randrange(0,1000)==0:ProchainFeu[1]=False
  if ProchainArret[0]<500 and ProchainArret[0]>480:fill_rect(260,90,30,30,'red')
  if keydown(KEY_SHIFT):
    if not FU and not keydown(KEY_EXE):print("FU active manuellement, "+str(monotonic()))
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
  if FU and keydown(KEY_SHIFT) and keydown(KEY_EXE):FU=False
  if ProchainArret[0]<321:
    fill_rect(0,180,320,40,'white')
    fill_rect(0,190,int(320-ProchainArret[0]),30,'blue')
    AffichageArriveeSimVitesse=Vitesse
    AffichageArriveeDistance=0
    for AffichageArriveeIteration in range(int(AffichageArriveeSimVitesse)):
      AffichageArriveeSimVitesse-=0.04
      AffichageArriveeDistance+=AffichageArriveeSimVitesse/12
    fill_rect(int(320-ProchainArret[0])+int(AffichageArriveeDistance),190,4,30,'orange')
    fill_rect(302,220,19,2,'green')
    fill_rect(0,220,302,2,'red')
  if keydown(KEY_ALPHA) and keydown(KEY_LOG):
    Commande=input("Commande ? ")
    if Commande=="CreaCarte":
      print("Entree en mode creation de carte...\nPressez BAKSPACE pour quitter et enregistrer")
      sleep(2)
      DistanceCreaCarte=0
      VitesseCreaCarte=0
      CreaCarteCarte=[]
      while not keydown(KEY_BACKSPACE):
        if keydown(KEY_DOWN) and VitesseCreaCarte>0:VitesseCreaCarte-=0.04
        elif keydown(KEY_UP):VitesseCreaCarte+=0.012
        elif VitesseCreaCarte>0.0001:VitesseCreaCarte-=0.0002
        draw_string(str(VitesseCreaCarte),0,0)
        draw_string(str(DistanceCreaCarte),0,30)
        DistanceCreaCarte+=VitesseCreaCarte/160
        if keydown(KEY_FIVE):
          CreaCarteCarte.append(int(DistanceCreaCarte))
          print(DistanceCreaCarte)
          DistanceCreaCarte=0
          sleep(0.5)
          while not keydown(KEY_FIVE):pass
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
      ProchainArret[0]=RouteActuelle[0]
      Arret=0
      BLANC()
    elif Commande=="AppendRoute":Routes.append(eval(input("AppendRoute ? ")))
    elif Commande=="def":exec(input("def eval ")+"="+input("def def eval "))
    elif Commande=="TestPA0":
      PA=True
      Vitesse=70
      Limite=70
      ProchainArret[0]=10000
      ProchainFeu[0]=10000
      ProchaineLimite=[400,40]
    elif Commande=="TestPA1":
      PA=True
      Vitesse=70
      Limite=70
      VACMA[4]=False
      ProchainArret[0]=700
      ProchainFeu[0]=10000
      ProchaineLimite[0]=10000
    elif Commande=="TestAF0":
      PA=True
      Vitesse=70
      Limite=60
      ProchainArret[0]=750
    i=0
  if Vitesse>0.1 and VACMA[4]:
    if keydown(KEY_ALPHA):
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
  if i==0:
    BLANC()
    BienvenueAfficherMenu("Service","Train","Bienvenue")
    if PA:
      draw_string("PA",262,126)
      draw_string("CM",262,151,(245,245,245))
    else:
      draw_string("PA",262,126,(245,245,245))
      draw_string("CM",262,151)
    fill_rect(260,90,30,30,BlancC)
    if len(ProchainArret)>2:ProchainArret[2]=choice(NomsArrets)
    else:ProchainArret.append(choice(NomsArrets))
    Acquitter=False
    i=1
  if (ProchainArret[0]<700 and len(ProchainArret)<3) or (PA and randrange(0,10000)==0):Acquitter=True
  if Acquitter:draw_string("Acquitter",40,5,'red')
  else:draw_string("Acquitter",40,5,BlancC)
  if ProchainArret[0]>=330:
    fill_rect(0,180,320,40,'white')
    fill_rect(0,190,20,30,'blue')
    fill_rect(0,220,320,2,'red')
    if ProchainFeu[0]<185:
      if ProchainFeu[1]:fill_rect(int((15+ProchainFeu[0])*2.5),190,10,10,'red')
      else:fill_rect(int((15+ProchainFeu[0])*2.5),190,10,10,'green')
    if ProchaineLimite[0]<330:draw_string(str(ProchaineLimite[1]),int((15+ProchaineLimite[0])*2.5),200)
    if ProchainArret[0]<515:
      fill_rect(int((ProchainArret[0]-320)*2.5),217,300,10,'black')
      draw_string(ProchainArret[2],int((ProchainArret[0]-300)*2.5),198)
  elif ProchainArret[0]>322:fill_rect(0,180,320,40,BlancC)
  if keydown(KEY_TANGENT):i=0
  Aleatoire=str(randrange(0,1000))
