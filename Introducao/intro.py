print("Hello, World!")

# Python interpreta o tipo das variáveis automaticamente (não é necessário declarar o tipo):
ip = "192.168.7.1" # str
porta = 80 # int
versao = 1.1 # float

# Exibindo as variáveis com f-strings
print("PROGRAMA")
print(f"Versão: {versao}")
print(f"Varrendo host {ip} na porta {porta}")

# Exibindo as variáveis com método parecido ao printf do C
print("PROGRAMA (Print diferente)")
print("Varrendo host: %s na porta %d" %(ip, porta))

# mostrando o tipo de cada variável
print("Tipos das variáveis:")
print("IP - ",type(ip))
print("Porta - ",type(porta))
print("Versão - ",type(versao))

