import random
import os
import math

# Função para calcular o número de combinações possíveis
def calcular_combinacoes(posicoes_restantes, elementos_disponiveis, sem_repeticao):
    if sem_repeticao:
        # Usar permutação sem repetição
        if len(elementos_disponiveis) >= posicoes_restantes:
            return math.perm(len(elementos_disponiveis), posicoes_restantes)
        else:
            return 0  # Se não houver caracteres suficientes para preencher as posições sem repetição
    else:
        # Combinação com repetição
        return len(elementos_disponiveis) ** posicoes_restantes

# Função para gerar uma senha
def gerar_senha(palavras, numeros, caracteres, tamanho, sem_repeticao=False, embaralhar=False):
    palavra = random.choice(palavras)
    senha = palavra
    caracteres_restantes = tamanho - len(palavra)

    if caracteres_restantes < 0:
        raise ValueError("Erro: O tamanho da senha não pode ser menor que o comprimento da palavra escolhida.")

    elementos = numeros + list(caracteres)

    if sem_repeticao:
        elementos = list(set(elementos))
        if len(elementos) < caracteres_restantes:
            raise ValueError("Erro: Não há caracteres suficientes para gerar a senha sem repetição.")

    adicionais = ''.join(random.sample(elementos, caracteres_restantes) if sem_repeticao else random.choices(elementos, k=caracteres_restantes))

    if embaralhar:
        adicionais = ''.join(random.sample(adicionais, len(adicionais)))

    if random.choice([True, False]):
        return senha + adicionais
    else:
        return adicionais + senha

# Função principal do gerador de senhas
def main():
    # Banner do GEASS PassGenerator
    print("""
    *************************************
    *       GEASS PassGenerator         *
    *   Gere suas senhas para BruteForce*
    *************************************
    """)

    # Interação com o usuário
    palavras = input("Escolha as palavras usadas (separadas por espaço): ").split()
    palavras = [palavra.strip() for palavra in palavras]
    
    numeros = input("Escolha os números usados (separados por espaço): ").split()
    caracteres = input("Escolha os caracteres especiais usados (sem espaços): ")
    tamanho = int(input("Escolha a quantidade de caracteres para cada senha: "))
    
    maior_palavra = max(palavras, key=len)
    if tamanho < len(maior_palavra):
        print(f"Erro: O tamanho da senha deve ser pelo menos {len(maior_palavra)} caracteres para incluir a maior palavra escolhida.")
        return

    # Opções avançadas
    sem_repeticao = input("Deseja evitar repetição de caracteres? (s/n): ").lower() == 's'
    embaralhar = input("Deseja embaralhar os caracteres adicionais? (s/n): ").lower() == 's'

    # Cálculo de combinações possíveis
    caracteres_restantes = tamanho - len(maior_palavra)
    elementos_disponiveis = numeros + list(caracteres)
    combinacoes_possiveis = calcular_combinacoes(caracteres_restantes, elementos_disponiveis, sem_repeticao)

    # Exibir o número de combinações possíveis
    print(f"\nÉ possível gerar até {combinacoes_possiveis} senhas únicas com os parâmetros fornecidos.")

    # Oferecer opção de gerar a quantidade máxima ou uma quantidade específica
    opcao = int(input("\nDigite 1 para gerar a quantidade máxima ou 2 para gerar uma quantidade limitada: "))

    if opcao == 1:
        quantidade = combinacoes_possiveis
        print(f"\nGerando a quantidade máxima de {quantidade} senhas...\n")
    elif opcao == 2:
        quantidade = int(input(f"Quantas senhas deseja gerar (até {combinacoes_possiveis})? "))
        if quantidade > combinacoes_possiveis:
            print(f"\nLimite máximo atingido. Serão geradas {combinacoes_possiveis} senhas.\n")
            quantidade = combinacoes_possiveis
        else:
            print(f"\nGerando {quantidade} senhas...\n")
    else:
        print("Opção inválida. Processo cancelado.")
        return

    # Adicionando opção para salvar
    salvar = input("Deseja salvar a wordlist? (s/n): ").lower() == 's'
    caminho = ''
    if salvar:
        print("Exemplo de caminho: /home/usuario/wordlist.txt ou C:\\Users\\Usuario\\wordlist.txt")
        caminho = input("Digite o caminho onde deseja salvar a wordlist: ")
        if not os.path.isdir(os.path.dirname(caminho)):
            print(f"Erro: O caminho '{os.path.dirname(caminho)}' não existe.")
            return

    senhas = set()
    while len(senhas) < quantidade:
        try:
            senha = gerar_senha(palavras, numeros, caracteres, tamanho, sem_repeticao, embaralhar)
            senhas.add(senha)
        except ValueError as e:
            print(e)
            return

    print("\nSenhas geradas:")
    for senha in senhas:
        print(senha)

    # Salvar as senhas em arquivo
    if salvar:
        try:
            with open(caminho, 'w') as f:
                for senha in senhas:
                    f.write(senha + '\n')
            print(f"\nWordlist salva com sucesso em: {caminho}")
        except IOError:
            print(f"\nErro ao salvar a wordlist em: {caminho}")

if __name__ == "__main__":
    main()
