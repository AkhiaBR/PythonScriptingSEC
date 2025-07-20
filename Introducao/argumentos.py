import sys # permite acessar os argumentos da linha de comando
import os # permite executar comandos do sistema

# Exibe os argumentos passados na linha de comando
print(f"Varrendo host {sys.argv[1]} na porta {sys.argv[2]}")

print("Verificando portas abertas: ")
os.system(f"netstat -nltp")