from mabibliotheque import *
vente=remboursement=stock=espece=carte=profit=solde=0
nbrJour= int(input("donner le nombre de jours pour lesquels les transactions doivent être traitées. "))
for j in range(nbrJour):
    print(f"Jour numero {j+1} ")
    nbTransaction=int(input("donner le nombre de transactions effectuées. "))
    for i in range(nbTransaction):
        print(f"transaction numero {i+1}")
        montant=int(input("le montant de la transaction. \n > "))
        while(montant<0):
            print("le montant doit etre positif ")
            montant=int(input("le montant de la transaction. \n > "))
        type=str(input("donner le type de transaction (vente, remboursement, achat de stock). \n >"))
        mode=str(input("donner le mode de paiement (espèces ou carte).\n >"))
        vente+=TotalVente(montant,type)
        remboursement+=TotalRembouresement(montant,type)
        stock+=TotalAchat(montant,type)
        espece+=TotalEspece(montant,mode)
        carte+=TotalCarte(montant,mode) 
    solde+=espece
    """ Tv=carte-vente
    vente+=Tv """
    profit=Profit(vente,remboursement,stock,Depenses(),espece,Taxe(vente))

    ChaqueJour(j,vente,remboursement,stock,espece,carte,profit)
    
print("+++++++++++++++++ Sur toute la periode ++++++++++++++++++++++++++")

SurLaPeriode(nbrJour,vente,remboursement,stock,espece,carte,profit)