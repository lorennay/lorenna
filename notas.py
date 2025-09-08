notas=[0.0]*4
soma= 0.0
print("digite as quatro notas do aluno:",end="")
for i in range(4):
    valor=float(input("digite a nota{}:".format(i+1)))
    notas[i]=valor
    soma+=valor
media=soma/4.0
print(f"a media é: {media:.2}")
for i in range(4):
    print(notas[i])

