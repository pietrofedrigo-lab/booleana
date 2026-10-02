# Revisando a lógica booleana

# ---- Simulador de críterios Escolares ----

# 1. Dados de Exxemplo de aluno
nota_final = 7.5
frequencia = 0.85  # Frequencia em decimal (85%)
historico_ruim = False # Histórico ruim do aluno (True ou False)
eh_atleta = True # O aluno é atleta (True ou False)

print("=== Análise Cadastral do aluno ===")

#-------------
#Cenário 1: Operador AND (Aprovaçaõ regular)
#Critério: Nota maior ou igual a 7.0 E frequencia maior ou igual a 75%
#-------------

passou_por_media = nota_final >= 7.0
passou_por_frequencia = frequencia >= 0.75
aprovado_regular = passou_por_media and passou_por_frequencia


print(F"Passou por média: {passou_por_media}")
print(f"Passou por frequencia: {passou_por_frequencia}")
print(+"Aprovado Regular: {aprovado_regular}")


#-----------
#Cenário 2: Operador OR (Bolsa de Incentivo)
#Critério: Nota fantática (>=9.0) OU ser atleta da escola
#-----------
nota_fantastica = nota_final >= 9.0
eh_atleta = eh_atleta # já é um valor booleano
bolsa_incentivo = nota_fantastica or eh_atleta

print(f"Nota Fantástica: {nota_fantastica}")
print(f"É atleta: {eh_atleta}")
print(f"Bolsa de Incentivo: {bolsa_incentivo}")


#----------
#Cénario 3: Operador NOT (Ficha limpa)
#Critério: O aluno NÃO pode ter um histórico ruim para ser monitor
#----------


pode_ser_monitor = not historico_ruim
print(f"Elegível para monitar: {pode_ser_monitor}")


#------------
#Cenário 4: Misturando tudo (Aprovação de Aluno Atleta)
#Critério: (Nota >= 6.0 E presença >= 70%) E ser atleta
#------------

aprovacao_especial = (nota_final >= 6.0 and frequencia >= 0.70) and eh_atleta
print(f"4. Aprovado pelo critério especial de atleta? {aprovacao_especial}")