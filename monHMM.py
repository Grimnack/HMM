import numpy as np
import random as r
class monHMM :
   "HMM par Matthieu Caron"
   def __init__(self,pi,transmat,symb,alpha) :
      self.p = pi
      self.t = transmat
      self.s = symb
      self.a = alpha
   
   
   def donneListePi(self) :
      "renvoie la liste des couples numero etat et probabilite de depart"
      longueur = len(self.p)
      i = 0
      res = [] 
      while i < longueur :
         res.append( (i,self.p[i] ) ) 
         i = i + 1
      return res
   
   #Ici c est cool car je sais plus ce que je voulais faire
   def donneListeSymb(self, etat) :
      longueur = len(self.a)
      i=0
      res = []
      while i < longueur :
         res.append( (self.a[i] , self.s[etat][i]) )
         i = i + 1
      return res
   
   def donneListeEtatSuivant ( self, etat ) :
      longueur = len(self.t) 
      i=0
      res = []
      while i < longueur :
         res.append((i,self.t[etat][i]))
         i = i + 1   
      return res
         
    
   def genereSequence(self, n) :
      "genere aleatoirement une sequence de taille n a partir d'un HMM"
      taille = 0
      observation = [] 
      #on se place d'abord dans l'etat initial 
      listeInit = self.donneListePi()
      etat = w_choice( listeInit )
      while taille < n :
         observation.append(w_choice(self.donneListeSymb(etat))) # ajoute une observation en fonction des probabilites d'apparition de symbole
         etat = w_choice(self.donneListeEtatSuivant(etat)) # change d'etat ou pas en fonction des probabilites de changement d'etat
         taille = taille + 1 
      return observation
   
   
   def alphaDonneIndice(self, alpha) :
      i = 0 
      while (self.a[i] != alpha ) :
         i = i + 1
      return i
   
   # pour i allant de 0 a n - 1 faire la somme des alpha[t][i] * self.t[i][j]
   def maSomme(self, tableau, n, j) :
      res = 0
      for i in range(n) :
         res = res + tableau[i] * self.t[i][j]
      return res
   
   def sommeFinale(tableau, n) :
      res = 0
      for i in range(n) :
         res = res + tableau[i]             
   # Alors tachons de comprendre ce qu'on fait
   def forwardAlpha (self,sequence) :    
      n = len(self.p)  
      t = 0 
      T = len(sequence)
      alpha = np.zeros(T,n)
      for i in range(n) :
         alpha[t][n] = self.p[i] * self.s[i][self.alphaDonneIndice(sequence[0])]
      while t < (T-1) :
         j = 0
         while j < n :
            alpha[t+1][j] = self.maSomme(alpha[t], n, j) * self.s[j][self.alphaDonneIndice(sequence[t+1])]
            j = j + 1
         t = t + 1
      res = sommeFinale(alpha[T-1], n)
      return res  
                               
   
   
   
   def backwardBeta () :
      
   def forwardBackward () :
   
   
   def viterbi () :
   
   
   
      
   

