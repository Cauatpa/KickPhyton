n1 = int(input("Digite a sua nota: "))
n2 = int(input("Digite a sua nota: "))
n3 = int(input("Digite a sua nota: "))

media = (n1 + n2 + n3) / 3
print("sua media foi:", media)

if media >= 6:
    print("Vc foi aprovado!")
else:
    print("Vc foi reprovado!")