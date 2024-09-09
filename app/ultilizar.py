import random
import os
from django.utils import timezone


codigos = [1000,2000,3000,4000,5000,6000,7000,8800]

def Sortear(codigo):
    numero_aleatorio = random.randint(1000, 9999)
    for n in codigo:
        if numero_aleatorio == n:
            numero_aleatorio = random.randint(1000, 9999)
            Sortear(codigo)

    return  int(numero_aleatorio)

print(Sortear(codigos))

# def DD(req):
#     user_agent_str = req.META.get('HTTP_USER_AGENT', '')
#     user_agent = user_agents.parse(user_agent_str)
    
#     browser_info = {
#         'browser': user_agent.browser.family,  # Nome do navegador (Ex: Chrome, Firefox)
#         'browser_version': user_agent.browser.version_string,  # Versão do navegador
#         'os': user_agent.os.family,  # Nome do sistema operacional (Ex: Windows, Linux, Mac OS)
#         'os_version': user_agent.os.version_string,  # Versão do sistema operacional
#         'device': user_agent.device.family  # Nome do dispositivo (Ex: iPhone, PC)
#     }

#     ip = req.META.get('HTTP_X_FORWARDED_FOR')
#     if ip:
#         ip = ip.split(',')[0]  # Em caso de múltiplos IPs, pega o primeiro (IP real)
#     else:
#         ip = req.META.get('REMOTE_ADDR')  # Caso não tenha um proxy, pega o IP diretamente
    
#     print(browser_info)
#     print(ip)




# # Função para capturar o IP e User-Agent
# def get_client_info(request):
#     # Captura o IP
#     ip = request.META.get('HTTP_X_FORWARDED_FOR')
#     if ip:
#         ip = ip.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
    
#     # Captura o User-Agent
#     user_agent_str = request.META.get('HTTP_USER_AGENT', '')
#     user_agent = user_agents.parse(user_agent_str)
    
#     client_info = {
#         'ip': ip,
#         'browser': user_agent.browser.family,
#         'browser_version': user_agent.browser.version_string,
#         'os': user_agent.os.family,
#         'os_version': user_agent.os.version_string,
#         'device': user_agent.device.family,
#         'timestamp': timezone.now().strftime('%Y-%m-%d %H:%M:%S')  # Hora da captura
#     }
    
#     return client_info

# # Função para salvar os dados em um arquivo .txt
# def save_client_info_to_file(client_info):
#     # Caminho para salvar o arquivo (ajuste conforme o necessário)
#     file_path = os.path.join('dad', 'acessos.txt')

#     # Garante que o diretório 'logs' exista
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)

#     # Abre o arquivo no modo de append ('a') para adicionar novas entradas
#     with open(file_path, 'a') as file:
#         file.write(f"IP: {client_info['ip']}\n")
#         file.write(f"Browser: {client_info['browser']} {client_info['browser_version']}\n")
#         file.write(f"OS: {client_info['os']} {client_info['os_version']}\n")
#         file.write(f"Device: {client_info['device']}\n")
#         file.write(f"Timestamp: {client_info['timestamp']}\n")
#         file.write(f"{'-'*40}\n")  # Separador para visualização
#     print(f"Informações do usuário salvas em {file_path}")

# # View para capturar as informações e armazená-las
# def track_user_info(request):
#     client_info = get_client_info(request)
#     # Salva as informações no arquivo .txt
#     save_client_info_to_file(client_info)
#     # Retorna uma resposta JSON com as informações (opcional)
#     print(client_info)


def save_browser_os_info_to_file(client_info):
    file_path = os.path.join('logs', 'acessos.txt')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'a') as file:
        file.write(f"Browser: {client_info['browser']}\n")
        file.write(f"OS: {client_info['os']}\n")
        file.write(f"IP: {client_info['ip']}\n")
        file.write(f"Convidado: {client_info['cdg']}\n")
        file.write(f"User-Agent Raw: {client_info['user_agent_raw']}\n")
        file.write(f"Horario: {client_info['timestamp']}\n")
        file.write(f"{'-'*40}\n")

def get_browser_os_info(request, cdg):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
        # Captura o IP
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    browser = 'Desconhecido'
    os = 'Desconhecido'
    
    if 'Chrome' in user_agent:
        browser = 'Chrome'
    elif 'Firefox' in user_agent:
        browser = 'Firefox'
    elif 'Safari' in user_agent and 'Chrome' not in user_agent:
        browser = 'Safari'
    elif 'Edge' in user_agent:
        browser = 'Edge'
    elif 'MSIE' in user_agent or 'Trident' in user_agent:
        browser = 'Internet Explorer'
    
    if 'Windows' in user_agent:
        os = 'Windows'
    elif 'Mac OS' in user_agent or 'Macintosh' in user_agent:
        os = 'Mac OS'
    elif 'Linux' in user_agent:
        os = 'Linux'
    elif 'Android' in user_agent:
        os = 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        os = 'iOS'
    
    client_info = {
        'browser': browser,
        'os': os,
        'user_agent_raw': user_agent,
        'ip': ip,
        'cdg':cdg,
        'timestamp': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Salva as informações em um arquivo
    save_browser_os_info_to_file(client_info)
    print(client_info)