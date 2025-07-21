import socket, sys

if (len(sys.argv) < 2):
    print("ERRO: Argumentos insuficientes.")
    print("EXEMPLO DE USO: python script.py <IP>")
    sys.exit(1)
else:
    ip = str(sys.argv[1])

    for porta in range(1, 1024):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao = mySocket.connect((ip, porta))
        banner = mySocket.recv(1024) # recebe o banner do serviço // 1024 é um tamanho considerado suficiente para a maioria da descrição de serviços (1 byte = 1 caractere)

        if banner:
            print(f"Porta {porta} aberta no host {ip} - Banner: {banner}")

        mySocket.close()

    sys.exit(0)