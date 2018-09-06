"""Quiz: Gerando mensagens Imagine que você é um professor que precisa enviar uma mensagem a todos os alunos,
lembrando-os das tarefas perdidas e atribuindo suas notas. Você possui todos os nomes, número de tarefas faltantes e
as notas em uma planilha e só deve inserir esses dados nos espaços reservados nesta mensagem que você criou: Hi [
inserir nome do aluno], This is a reminder that you have [inserir número de tarefas perdidas] assignments left to
submit before you can graduate. Your current grade is [inserir nota atual] and can increase to [inserir nota
potencial] if you submit all assignments before the due date. Você pode apenas copiar e colar esta mensagem para cada
aluno e inserir manualmente os valores apropriados em cada vez, mas, em vez disso, vai escrever um programa que faz
isso por você. Escreva um script que faz o seguinte:

1 - Pede 3 vezes uma entrada do usuário. Uma para obter uma lista de nomes, outra para obter uma lista de tarefas perdidas
e uma última vez para obter uma lista de notas. Utilize esta entrada para criar as listas names, assignments e grades.

2 - Use um loop para exibir a mensagem para cada aluno com os valores corretos.
A nota potencial é simplesmente a nota atual somada ao dobro do número de atividades perdidas."""

names = input("Entre com os nomes separados por virgula: ").title().split(",")
assignments = input("Insira o número de tarefas separadas por virgula: ").split(",")
grades = input("Entre com o grau separado por virgulas: ").split(",")
print(names)
print(assignments)
print(grades)

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
