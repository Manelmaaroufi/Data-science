poids=float(input('donner votre poids'))
taille=float(input('donner votre taille'))
Imc=poids/(taille*taille)
if Imc<20:
    print(Imc)
    print('vous etes maigre')
elif Imc<=25:
    print(Imc)
    print('votre Imc est ideal')
else:
    print(Imc)
    print('en surpoids et il te faut un regime')   


