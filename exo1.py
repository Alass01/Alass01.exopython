tab = []
inverse_tab = tab[::-1]
for i in range(5):
    value = int(input("inserer vos valeur : "))
    tab.append(value)
    print (tab)
print("la liste de vos valeur est : ",tab)

print("l'inverse de la liste est : ", inverse_tab)


def inversTableau(liste):
    return liste[::-1]
tab = [1,45,85,74,48,1,0,]
result_inves = inversTableau(tab)
print('inverse = ',result_inves)