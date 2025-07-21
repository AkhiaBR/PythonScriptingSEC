import socket

print("Interagindo com FTP SERVER")

ip = str(input("Digite o IP do servidor: "))
porta = 21

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((ip, porta))
banner = mySocket.recv(1024)  # Recebe o banner do serviço FTP
print(banner)

print("Enviando comando USER")
mySocket.send("USER akhia\r\n") # Envia o comando USER # \r\n é necessário para indicar o fim do comando
banner = mySocket.recv(1024)  # Recebe a resposta do servidor
print(banner)

print("Enviando comando PASS")
mySocket.send("PASS akhia\r\n") # Envia o comando PASS
banner = mySocket.recv(1024)
print(banner)