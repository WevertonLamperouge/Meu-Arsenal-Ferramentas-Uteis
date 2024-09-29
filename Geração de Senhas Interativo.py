import random
import os

def gerar_senha(palavras, numeros, caracteres, tamanho):
    # Escolher uma palavra aleatória da lista de palavras
    palavra = random.choice(palavras)
    
    # Garantir que a palavra escolhida esteja na senha
    senha = palavra
    
    # Calcular quantos caracteres adicionais são necessários
    caracteres_restantes = tamanho - len(palavra)
    
    # Criar uma lista com todos os elementos possíveis (números e caracteres especiais)
    elementos = numeros + list(caracteres)
    
    # Adicionar elementos aleatórios até atingir o tamanho desejado
    senha += ''.join(random.choice(elementos) for _ in range(caracteres_restantes))
    
    # Decidir aleatoriamente se a palavra ficará no início ou no final
    if random.choice([True, False]):
        return senha
    else:
        return senha[len(palavra):] + palavra

def main():
    print("Bem-vindo ao Gerador de Senhas Interativo!")

    palavras = input("Escolha as palavras usadas (separadas por espaço): ").split()
    # Remover espaços das palavras individualmente
    palavras = [palavra.strip() for palavra in palavras]
    
    numeros = input("Escolha os números usados (separados por espaço): ").split()
    caracteres = input("Escolha os caracteres especiais usados (sem espaços): ")
    tamanho = int(input("Escolha a quantidade de caracteres para cada senha: "))
    
    # Verificar se o tamanho é suficiente para incluir a maior palavra
    maior_palavra = max(palavras, key=len)
    if tamanho < len(maior_palavra):
        print(f"Erro: O tamanho da senha deve ser pelo menos {len(maior_palavra)} caracteres para incluir a maior palavra escolhida.")
        return

    quantidade = int(input("Escolha a quantidade mínima de senhas geradas: "))
    
    # Adicionando opção para escolher onde salvar a wordlist com exemplo
    salvar = input("Deseja salvar a wordlist? (s/n): ").lower() == 's'
    if salvar:
        print("Exemplo de caminho: /home/usuario/wordlist.txt ou C:\\Users\\Usuario\\wordlist.txt")
        caminho = input("Digite o caminho onde deseja salvar a wordlist: ")

    senhas = set()
    while len(senhas) < quantidade:
        senha = gerar_senha(palavras, numeros, caracteres, tamanho)
        senhas.add(senha)

    print("\nSenhas geradas:")
    for senha in senhas:
        print(senha)

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
