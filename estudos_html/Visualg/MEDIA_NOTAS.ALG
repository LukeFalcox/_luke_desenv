Algoritmo "media_notas"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/04/2022
Var
// Se��o de Declara��es das vari�veis 
nota1 : Real
nota2 : Real
nota3 : Real
media: Real
media_fito : Real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
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