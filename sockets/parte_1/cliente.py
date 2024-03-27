# -*- coding: utf-8 -*-
import urllib2

# URL do servidor web
url = 'http://192.0.2.10:8080/'

# Passos para testar o servidor
passos_teste = [
    "1. Abra um navegador web.",
    "2. Digite a URL {} na barra de endereços do navegador.".format(url),
    "3. Pressione Enter para acessar a página.",
    "4. Verifique se a página é exibida corretamente.",
    "5. Verifique se não há erros visíveis na página.",
]

# Exibir os passos
print("Para testar o servidor web da sua empresa, siga estes passos:")
for passo in passos_teste:
    print(passo)

# Requisição GET para obter a página
req = urllib2.Request(url)
response = urllib2.urlopen(req)

# Ler e exibir o conteúdo da página
pagina = response.read()
print("\nConteúdo da página:")
print(pagina)

