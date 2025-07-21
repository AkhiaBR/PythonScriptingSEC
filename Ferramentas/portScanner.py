import socket, sys

if (len(sys.argv) < 2):
    print("ERRO: Argumentos insuficientes.")
    print("EXEMPLO DE USO: python script.py <IP>")
    sys.exit(1)
else:
    ip = str(sys.argv[1])

    for porta in range(1, 65536):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao = mySocket.connect_ex((ip, porta))

        if (conexao == 0):
            print(f"Porta {porta} aberta no host {ip}")

        mySocket.close()

    sys.exit(0)