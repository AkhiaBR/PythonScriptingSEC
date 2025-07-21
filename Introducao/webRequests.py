import sys
import requests # importa a biblioteca requests (para fazer requisições HTTP)

if (len(sys.argv) < 2):
    print("ERRO: URL não informada")
    print("Uso: python webRequests.py <URL>")
    sys.exit(1)
else:
    site = requests.get(sys.argv[1]) # faz uma requisição GET para o site passado como argumento
    status = site.status_code # obtém o código de status da resposta

    if (status == 200): # verifica se o código de status é 200 (OK)
        print("PAGINA ATIVA")
    else:
        print("PAGINA INATIVA")

    sys.exit(0)