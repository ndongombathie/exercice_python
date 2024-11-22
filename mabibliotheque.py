#fonction pour calculer le total des ventes
def TotalVente(montant,typeTransaction):
    vente=0
    if(typeTransaction=='vente'):
      vente+=montant
    return vente

#fonction pour calculer le total des remboursement
def TotalRembouresement(montant,typeTransaction):
    Rembouresement=0
    if(typeTransaction=='remboursement'):
        Rembouresement+=montant
    return Rembouresement
        
def TotalAchat(montant,typeTransaction):
    Achat=0
    if(typeTransaction=='achat de stock'):
     Achat+=montant
    return Achat
        
def TotalEspece(montant,ModeTransaction):
    Espece=0
    if(ModeTransaction=='especes'):
        Espece+=montant
    return Espece

def TotalCarte(montant,ModeTransaction):
    carte=0
    if(ModeTransaction=='carte'):
        carte+=montant
    return carte
        
def Taxe(totalVente):
    return totalVente*(10/100)

#la depense pour chaque jour
def Depenses():
    return 5000+10000+2000

def Profit(TotalVente,TotalRememboursement,TotalAchat,Depense,TotalEspece,Taxe):
    perte=(TotalVente-TotalRememboursement-TotalAchat-Depense+TotalEspece)-Taxe
    return perte

#les fonctions d'affichage ChaqueJour() et SurLaPeriode()

# Affichage des detail pour chaque jour
def ChaqueJour(j,vente,remboursement,stock,espece,carte,profit):
    print(f"les totaux du jour {j+1}")
    print(f"Total des vente apres taxe : {vente+Taxe(vente)}")
    print(f"Total des rembouresement : {remboursement}")
    print(f"Total des achats de stock {stock}")
    print(f"Total des depenses reccurente {Depenses()}")
    print(f"Total des paiement en espece : {espece}")
    print(f"Total des paiement par carte : {carte}")
    print(f"le Profit ou la perte : {profit}")
    
#Affichage des details sur toute la periode
def SurLaPeriode(nbrJour,vente,remboursement,stock,espece,carte,profit):
    print(f"les totaux sur la periode des {nbrJour} jour")
    print(f"Total des vente apres taxe : {Taxe(vente)*nbrJour}")
    print(f"Total des rembouresement : {remboursement*nbrJour}")
    print(f"Total des achats de stock :{stock*nbrJour}")
    #la depense sur toute la periode
    print(f"Total des depenses reccurente {Depenses()*nbrJour}")
    print(f"Total des paiement en espece : {espece*nbrJour}")
    print(f"Total des paiement par carte : {carte*nbrJour}")
    print(f"profit ou la perte : {profit*nbrJour}")