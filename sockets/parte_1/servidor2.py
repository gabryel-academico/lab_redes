import SimpleHTTPServer
import SocketServer

PORT = 8080

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Lê o conteúdo do arquivo index.html
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Define o cabeçalho da resposta HTTP
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Envia o conteúdo do arquivo como resposta
        self.wfile.write(content)

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Servidor em execução na porta", PORT

httpd.serve_forever()
