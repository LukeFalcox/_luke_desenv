Algoritmo "compara_valores"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : M�rcio
// Descri��o   : Compara dois valores digitados pelo usu�rio
// Autor(a)    : Guilherme Henrique e Luis Henrique
// Data atual  : 06/04/2022
Var
// Se��o de Declara��es das vari�veis 
valor1 : inteiro
valor2 : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Digite o primeiro valor :")
leia(valor1)
escreva("Digite o segundo valor :")
leia(valor2)
se valor1 > valor2 entao
   escreva(valor1, " � maior do que ", valor2)
senao
se valor1 < valor2 entao
   escreva(valor1, " � menor do que ", valor2)
   senao
   escreva(valor1, " � igual a ", valor2)
   fimse
fimse
Fimalgoritmo