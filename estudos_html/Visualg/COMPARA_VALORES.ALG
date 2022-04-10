Algoritmo "compara_valores"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Márcio
// Descrição   : Compara dois valores digitados pelo usuário
// Autor(a)    : Guilherme Henrique e Luis Henrique
// Data atual  : 06/04/2022
Var
// Seção de Declarações das variáveis 
valor1 : inteiro
valor2 : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite o primeiro valor :")
leia(valor1)
escreva("Digite o segundo valor :")
leia(valor2)
se valor1 > valor2 entao
   escreva(valor1, " é maior do que ", valor2)
senao
se valor1 < valor2 entao
   escreva(valor1, " é menor do que ", valor2)
   senao
   escreva(valor1, " é igual a ", valor2)
   fimse
fimse
Fimalgoritmo