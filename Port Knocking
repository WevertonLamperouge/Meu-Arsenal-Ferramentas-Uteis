import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

# Função para exibir o banner
def exibir_banner():
    print(f"""{Fore.CYAN}
    *************************************
    *        GEASS PortKnocking         *
    *    Ferramenta de Port Knocking    *
    *************************************
    {Style.RESET_ALL}""")

# Solicitar a faixa de IPs do usuário
def solicitar_ips():
    while True:
        ip_input = input("Digite o endereço IP ou faixa de IP (ex: 172.16.1.0/24): ")
        try:
            ipaddress.IPv4Network(ip_input, strict=False)
            return ip_input
        except ValueError:
            print("Faixa de IP inválida. Tente novamente.")

# Solicitar as portas a serem testadas
def solicitar_portas():
    while True:
        porta_input = input("Digite as portas para testar (separadas por espaço): ")
        try:
            portas = [int(porta) for porta in porta_input.split() if 1 <= int(porta) <= 65535]
            if portas:
                return portas
            else:
                print("Por favor, insira portas válidas entre 1 e 65535.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números inteiros.")

# Solicitar a porta de knock
def solicitar_porta_knock():
    while True:
        try:
            porta_knock = int(input("Digite a porta de knock a ser verificada: "))
            if 1 <= porta_knock <= 65535:
                return porta_knock
            else:
                print("Por favor, insira uma porta válida entre 1 e 65535.")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")

# Função para realizar ping nas portas usando hping3
def ping_portas(ip, portas):
    for porta in portas:
        try:
            subprocess.run(["hping3", "-S", "-c", "1", "-p", str(porta), str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.SubprocessError:
            print(f"{Fore.RED}Erro ao tentar ping na porta {porta} em {ip}{Style.RESET_ALL}")

# Função para verificar a porta knock usando wget
def verificar_porta_knock(ip, porta_knock):
    try:
        resultado_knock = subprocess.run(["wget", f"{str(ip)}:{porta_knock}", "-O", "/dev/null"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if resultado_knock.returncode == 0:
            print(f"{ip} Porta {porta_knock} " + Fore.GREEN + "Aberta" + Style.RESET_ALL)
        else:
            print(f"{ip} Porta {porta_knock} Não Aberta")
    except subprocess.SubprocessError:
        print(f"{Fore.RED}Erro ao verificar a porta knock {porta_knock} em {ip}{Style.RESET_ALL}")

# Função que realiza o ping e verificação de portas em uma faixa de IP
def realizar_ping(faixa_ip, portas, porta_knock):
    ip_list = ipaddress.IPv4Network(faixa_ip, strict=False)
    with ThreadPoolExecutor(max_workers=10) as executor:
        for ip in ip_list.hosts():
            print(f"{ip} - Testando portas {portas}, verificando knock na porta {porta_knock} ", end="")
            executor.submit(ping_portas, ip, portas)
            executor.submit(verificar_porta_knock, ip, porta_knock)

# Função principal
def main():
    exibir_banner()  # Exibe o banner GEASS PortKnocking

    faixa_ip = solicitar_ips()  # Solicita a faixa de IP
    portas = solicitar_portas()  # Solicita as portas a serem testadas
    porta_knock = solicitar_porta_knock()  # Solicita a porta knock

    print(f"Iniciando teste de portas para faixa de IP {faixa_ip}")
    realizar_ping(faixa_ip, portas, porta_knock)  # Inicia a verificação

if __name__ == "__main__":
    main()
