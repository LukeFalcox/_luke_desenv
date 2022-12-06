#\033[0;33;40m ele deve ser usado no print

"""Codigos para estilos 
 0 significa sem estilo
 1 significa negrito
 4 significa sublinhado
 7 significa que ele vai inverter as configurações oque vai pra letra vai ficar no fundo e oque ficar n fundo vai ir para a letra
"""
"""Codigos para cores 
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo
36 ciano
37 cinza
"""
"""Codigos para fundos 
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 roxo
46 ciano
47 cinza
"""
print("\033[0;30;41mTeste")
print("\033[4;33;44mTeste")
print("\033[0;35;43mTeste")
print("\033[0;30;42mTeste")
print("\033[mTeste")
print("\033[7;30mTeste")
a = 5
b = 6
print("Os valores são \033[32{} e \033[31m{}".format(a, b))