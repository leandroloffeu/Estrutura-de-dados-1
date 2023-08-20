#Leandro Loffeu Pereira Costa 202212089 - Ainda estou trabalhando no exercicio
# Dados fictícios de temperatura, umidade e pressão para um dia específico (vigésimo dia)
temperaturas = [25.5, 26.2, 25.7] 
umidades = [60, 62, 58] 
pressoes = [1010, 1012, 1015] 

# Função para calcular mínimos, máximos e médias
def calcular_estatisticas(valores):
    return min(valores), max(valores), sum(valores) / len(valores)

# Calcular estatísticas para temperatura, umidade e pressão
temperatura_minima, temperatura_maxima, temperatura_media = calcular_estatisticas(temperaturas)
umidade_minima, umidade_maxima, umidade_media = calcular_estatisticas(umidades)
pressao_minima, pressao_maxima, pressao_media = calcular_estatisticas(pressoes)

# Calcular a quantidade de ciclos (n) no dia
quantidade_ciclos = len(temperaturas)

# Imprimir os resultados
print("Valores para Temperatura:")
print(f"Mínima: {temperatura_minima}°C")
print(f"Máxima: {temperatura_maxima}°C")
print(f"Média: {temperatura_media}°C\n")

print("Valores para Umidade:")
print(f"Mínima: {umidade_minima}%")
print(f"Máxima: {umidade_maxima}%")
print(f"Média: {umidade_media}%\n")

print("Valores para Pressão:")
print(f"Mínima: {pressao_minima} hPa")
print(f"Máxima: {pressao_maxima} hPa")
print(f"Média: {pressao_media} hPa\n")

print(f"Quantidade de ciclos no dia: {quantidade_ciclos}")