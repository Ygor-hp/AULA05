i=0
soma=0
alunos=int(input("Digite o numero de alunos: "))
while i < alunos:
    nota=float(input("notas dos alunos: "))
    soma=soma+nota
    i += 1
media=soma/nota
print(f"nota dos alunos da sala:{media}")

