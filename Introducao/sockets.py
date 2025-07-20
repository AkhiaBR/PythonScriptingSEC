import socket # Importa o módulo socket para manipulação de conexões de rede
import sys

if (len(sys.argv) < 3):
    print("ERRO: Argumentos insuficientes.")
    print("EXEMPLO DE USO: python script.py <IP> <porta>")
    sys.exit(1)
else:
    ip = str(sys.argv[1])
    porta = int(sys.argv[2])
    
    # AF_INET indica que o socket usará o protocolo IPv4
    # SOCK_STREAM indica que o socket usará o protocolo TCP
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket
    # diferença entre mySocket.connect() e mySocket.connect_ex(): mySocket.connect() emite um erro se não conseguir conectar, enquanto mySocket.connect_ex() retorna 0 (sucesso) ou diferente de 0 (erro)
    conexao = mySocket.connect_ex((ip, porta)) # Tenta conectar ao socket criado

    if (conexao == 0): # Se a conexão for bem-sucedida
        print(f"Porta {porta} aberta no host {ip}")
    else:
        print(f"Porta {porta} fechada no host {ip}")

    mySocket.close() # Fecha o socket após a verificação
    sys.exit(0) # Encerra o programa com sucesso