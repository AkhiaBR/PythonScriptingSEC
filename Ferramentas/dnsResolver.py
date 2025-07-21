import sys, socket

host = sys.argv[1]

print(host,"--->",socket.gethostbyname(host))  # Obtém o IP do host fornecido