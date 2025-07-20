import sys

if (len(sys.argv) < 3):
    print("EXEMPLO DE USO: python script.py <IP> <porta>")
    sys.exit(1) # sys.exit(1) encerra o programa com erro
else:
    ip = str(sys.argv[1])  # o IP é passado como argumento
    porta = int(sys.argv[2])  # a porta é passada como argumento

    print(f"Varrendo host {ip} na porta {porta}")
