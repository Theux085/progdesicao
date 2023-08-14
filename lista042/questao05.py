'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

est= input("Digite a sigla de um estado brasileiro: ")

regiao_sudeste = ["SP", "RJ", "MG", "ES"]

if est == "SP" or est == "RJ" or est == "MG" or est == "ES":
    print("O estado inserido está na região Sudeste.")
else:
    print("O estado inserido não está na região Sudeste.")

