import sys
import urllib.request # importa a biblioteca urllib (para fazer requisições HTTP)

if (len(sys.argv) < 2):
    print("ERRO: URL não informada")
    print("Uso: python webRequests.py <URL>")
    sys.exit(1)
else:
    site = urllib.request.urlopen(sys.argv[1]) # faz uma requisição GET para o site passado como argumento
    server = site.info() # obtém as informações do servidor

    if (site.getcode() == 200): # verifica se o código de status é 200 (OK)
        print("PAGINA ATIVA")
        print(server["Server"]) # imprime o cabeçalho 'Server' dentro da variável server
    else:
        print("PAGINA INATIVA")

    sys.exit(0)
