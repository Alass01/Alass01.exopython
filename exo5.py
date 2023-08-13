# Demander à l'utilisateur d'insérer des nombres
n = int(input("Combien de nombres voulez-vous insérer ? "))
numbers = []

for i in range(n):
    num = int(input("Insérez le nombre: "))
    numbers.append(num)

# Afficher les nombres divisibles par 5
print("Les nombres divisibles par 5 sont :")
for num in numbers:
    if num % 5 == 0:
        print(num)
    
