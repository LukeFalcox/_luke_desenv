Algoritmo "media_notas"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/04/2022
Var
// Seção de Declarações das variáveis 
nota1 : Real
nota2 : Real
nota3 : Real
media: Real
media_fito : Real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite a nota do primeiro trimestre : ")
leia(nota1)
escreva("Digite a nota do segundo trimestre : ")
leia(nota2)
escreva("Digite a nota do terceiro trimestre : ")
leia(nota3)
media <- (nota1 + nota2 + nota3) / 3
media_fito <- (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
escreval ("A media da FITO : ", media_fito)
escreval ("A media das outras escolas : ", media)

Fimalgoritmo